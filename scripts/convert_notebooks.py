#!/usr/bin/env python3
"""Notebook publishing pipeline (ARCHITECTURE.md / ADR-007).

Converts notebooks/{strategies,blog}/*.ipynb to gitignored markdown in
src/content/<collection>/generated-<slug>.md, with extracted images in a
co-located generated-<slug>/ asset folder.

Contract:
- First cell of every notebook is a RAW cell holding YAML frontmatter; it is
  validated here against the collection schema and the build fails with a
  clear message if invalid — bad metadata never reaches production.
- Notebooks are NEVER executed: outputs publish exactly as saved.
- Empty cells and code cells whose first line starts with `# HIDE` are
  stripped before conversion.
- Outputs larger than 1 MB raise a warning (downsize the figure).
- Generated files carry a `<!-- GENERATED ... -->` header and the
  `generated-` filename prefix that .gitignore excludes; the URL slug is
  kept clean via the `slug` frontmatter override.
"""

import base64
import re
import sys
from datetime import date, datetime
from pathlib import Path

try:
    import nbformat
    import yaml
    from nbconvert import MarkdownExporter
    from traitlets.config import Config
except ImportError as exc:  # noqa: BLE001 - report the missing dependency clearly
    sys.exit(
        f"convert_notebooks: missing dependency ({exc}).\n"
        "Install with: pip install nbconvert nbformat pyyaml "
        "(locally: .venv/bin/pip install nbconvert nbformat pyyaml)"
    )

ROOT = Path(__file__).resolve().parent.parent
NOTEBOOK_DIRS = {
    "strategies": ROOT / "notebooks" / "strategies",
    "blog": ROOT / "notebooks" / "blog",
}
CONTENT_DIR = ROOT / "src" / "content"

CATEGORIES = {"trend", "mean reversion", "optimization", "risk", "infra"}
STATUSES = {"idea", "researching", "backtested", "paper-trading"}
ONE_MB = 1_000_000

# Mirrors the zod schemas in src/content/config.ts (field -> required).
SCHEMA_FIELDS = {
    "blog": {
        "title": True,
        "description": True,
        "date": True,
        "tags": False,
        "draft": False,
    },
    "strategies": {
        "title": True,
        "description": True,
        "category": True,
        "tags": False,
        "status": True,
        "date": True,
        "updated": False,
        "repo": False,
        "draft": False,
    },
}


def slugify(stem: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", stem.lower()).strip("-")
    return slug or "untitled"


def validate_frontmatter(collection: str, meta: dict, origin: str) -> list[str]:
    """Return a list of human-readable problems (empty = valid)."""
    problems = []
    fields = SCHEMA_FIELDS[collection]

    for field, required in fields.items():
        if required and field not in meta:
            problems.append(f"missing required field '{field}'")
    for field in meta:
        if field not in fields:
            problems.append(f"unknown field '{field}' (schema is a contract — see CLAUDE.md rule 5)")

    for field in ("title", "description"):
        if field in meta and not isinstance(meta[field], str):
            problems.append(f"'{field}' must be a string")
    for field in ("date", "updated"):
        if field in meta and not isinstance(meta[field], (date, datetime)):
            problems.append(f"'{field}' must be a YAML date (e.g. 2026-06-15)")
    if "tags" in meta and (
        not isinstance(meta["tags"], list)
        or any(not isinstance(t, str) for t in meta["tags"])
    ):
        problems.append("'tags' must be a list of strings")
    if "draft" in meta and not isinstance(meta["draft"], bool):
        problems.append("'draft' must be true or false")
    if collection == "strategies":
        if "category" in meta and meta["category"] not in CATEGORIES:
            problems.append(f"'category' must be one of {sorted(CATEGORIES)}")
        if "status" in meta and meta["status"] not in STATUSES:
            problems.append(f"'status' must be one of {sorted(STATUSES)}")
        if "repo" in meta and not str(meta.get("repo", "")).startswith("https://"):
            problems.append("'repo' must be an https URL")

    return [f"{origin}: {p}" for p in problems]


def extract_frontmatter(nb, origin: str):
    """Pull the YAML frontmatter from the leading raw cell. Returns (meta, errors)."""
    if not nb.cells or nb.cells[0].cell_type != "raw":
        return None, [
            f"{origin}: first cell must be a RAW cell containing YAML frontmatter "
            "(see the template in KICKOFF.md)"
        ]
    source = nb.cells[0].source.strip()
    match = re.fullmatch(r"---\s*\n(.*?)\n---\s*", source, flags=re.DOTALL)
    if not match:
        return None, [
            f"{origin}: frontmatter raw cell must be fenced with '---' lines"
        ]
    try:
        meta = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        return None, [f"{origin}: frontmatter is not valid YAML — {exc}"]
    if not isinstance(meta, dict):
        return None, [f"{origin}: frontmatter must be a YAML mapping"]
    return meta, []


def strip_cells(nb):
    """Drop the frontmatter cell, empty cells, and `# HIDE`-tagged code cells."""
    kept = []
    for cell in nb.cells[1:]:
        source = cell.source.strip()
        if not source:
            continue
        if cell.cell_type == "code" and source.splitlines()[0].strip().startswith("# HIDE"):
            continue
        kept.append(cell)
    nb.cells = kept
    return nb


def clean_generated(collection_dir: Path) -> None:
    """Remove previous generated output so deleted notebooks leave no stale pages."""
    if not collection_dir.exists():
        return
    for path in collection_dir.glob("generated-*"):
        if path.is_dir():
            for child in sorted(path.rglob("*"), reverse=True):
                child.unlink()
            path.rmdir()
        else:
            path.unlink()


def convert(notebook_path: Path, collection: str) -> list[str]:
    origin = notebook_path.relative_to(ROOT)
    nb = nbformat.read(notebook_path, as_version=4)

    meta, errors = extract_frontmatter(nb, str(origin))
    if errors:
        return errors
    errors = validate_frontmatter(collection, meta, str(origin))
    if errors:
        return errors

    slug = slugify(notebook_path.stem)
    asset_dir_name = f"generated-{slug}"

    config = Config()
    config.MarkdownExporter.preprocessors = [
        "nbconvert.preprocessors.ExtractOutputPreprocessor"
    ]
    exporter = MarkdownExporter(config=config)
    body, resources = exporter.from_notebook_node(
        strip_cells(nb),
        resources={"output_files_dir": asset_dir_name, "unique_key": "output"},
    )

    out_dir = CONTENT_DIR / collection
    out_dir.mkdir(parents=True, exist_ok=True)

    for rel_name, payload in resources.get("outputs", {}).items():
        target = out_dir / rel_name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(payload)
        if len(payload) > ONE_MB:
            print(
                f"convert_notebooks: WARNING {origin}: output {rel_name} is "
                f"{len(payload) / ONE_MB:.1f} MB — consider downsizing the figure",
                file=sys.stderr,
            )

    # Make image references explicitly relative so Astro resolves and
    # optimizes them from the markdown file's location.
    body = body.replace(f"]({asset_dir_name}/", f"](./{asset_dir_name}/")

    frontmatter = dict(meta)
    frontmatter["slug"] = slug  # Astro reserved field: clean URL despite generated- filename
    header = (
        f"<!-- GENERATED from {origin} — do not edit; "
        "edit the notebook or scripts/convert_notebooks.py -->"
    )
    document = "---\n{fm}---\n\n{header}\n\n{body}".format(
        fm=yaml.safe_dump(frontmatter, sort_keys=False, allow_unicode=True),
        header=header,
        body=body.strip() + "\n",
    )
    (out_dir / f"generated-{slug}.md").write_text(document, encoding="utf-8")
    print(f"convert_notebooks: {origin} -> src/content/{collection}/generated-{slug}.md")
    return []


def main() -> int:
    all_errors = []
    converted = 0
    for collection, nb_dir in NOTEBOOK_DIRS.items():
        clean_generated(CONTENT_DIR / collection)
        if not nb_dir.exists():
            continue
        for notebook_path in sorted(nb_dir.glob("*.ipynb")):
            errors = convert(notebook_path, collection)
            if errors:
                all_errors.extend(errors)
            else:
                converted += 1

    if all_errors:
        print("convert_notebooks: FAILED — fix the notebook frontmatter:", file=sys.stderr)
        for error in all_errors:
            print(f"  - {error}", file=sys.stderr)
        return 1
    print(f"convert_notebooks: {converted} notebook(s) converted")
    return 0


if __name__ == "__main__":
    sys.exit(main())
