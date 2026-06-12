# DESIGN.md — visual identity & voice

The agent implements this file literally. Where DESIGN.md and personal taste conflict,
DESIGN.md wins. Where DESIGN.md is silent, choose the quieter option.

## Brand essence
A personal research notebook by a working quant/data scientist. Warm, grounded,
honest. Closer to a well-typeset journal than a startup landing page. The reader
should feel they're being shown around by a person, not pitched to by a brand.

## Color tokens
Palette source: forest green · honey yellow · pale sage · warm taupe.

### Light mode (default)
```css
--bg:            #FBFBF8;   /* page background, warm off-white */
--surface:       #FFFFFE;   /* cards */
--band:          #E9EEEB;   /* footer band, soft sage block */
--text:          #2F3A33;   /* headings/body strong — green-charcoal */
--text-2:        #565B53;   /* body */
--text-muted:    #9C8C79;   /* taupe — labels, dates, tags */
--hairline:      #DDE3DF;   /* dividers */
--card-border:   #D6DEDA;   /* pale sage */
--btn-border:    #C9BBA9;   /* taupe outline buttons */
--accent:        #41604F;   /* forest green — primary buttons, links, eyebrow */
--accent-text:   #E9F0EC;   /* text on accent */
--badge-green-bg:#E4ECE7;  --badge-green-fg:#2C4438;   /* status: backtested/validated */
--badge-honey-bg:#FFEFC4;  --badge-honey-fg:#6B5210;   /* status: daily driver / live */
--badge-taupe-bg:#EDE3D8;  --badge-taupe-fg:#5F4C38;   /* status: researching / idea */
```

### Dark mode (prefers-color-scheme: dark, toggle overrides)
```css
--bg:            #20261F;   /* deep green-charcoal, NOT pure black */
--surface:       #2A3128;
--band:          #262D25;
--text:          #E4E8E1;
--text-2:        #B9C0B6;
--text-muted:    #A89682;
--hairline:      #394137;
--card-border:   #394137;
--btn-border:    #5A5247;
--accent:        #FFCF5C;   /* accent FLIPS to honey in dark mode */
--accent-text:   #3A2D08;
/* badge pairs: keep light-bg/dark-fg pairs from light mode — they read as
   chips and remain legible on dark surfaces */
```

## Color rules
1. Honey yellow is NEVER body/link text and never a thin meaningful border in light
   mode (fails contrast on light bg). Backgrounds-with-dark-text only — except in
   dark mode where it serves as the accent.
2. One filled element per view: the primary CTA. Everything else outline or text.
3. Status badges are the only place semantic color appears. Mapping is fixed:
   green = validated (backtested), honey = in active use (daily driver / live),
   taupe = in progress (researching / idea). Never invent new badge colors.
4. All text/background pairs must pass WCAG AA. When unsure, darken the foreground.

## Typography
- Display/headings: "Source Serif 4" (self-host via @fontsource), weight 500.
- Body/UI: "Inter" (@fontsource-variable/inter), weights 400/500 only.
- Labels, dates, tags, code: "JetBrains Mono" (@fontsource), 400/500.
- Mono usage is the signature: section labels (12px, letter-spacing 0.05em,
  lowercase), dates, tech tags, nav wordmark, footer. Lowercase for these labels
  is a deliberate style choice; normal sentence case everywhere else.
- Body 16px/1.65. h1 32px, h2 24px, h3 18px. Never bold above weight 500.
- No font weights 600+; no italics except blockquotes.

## Components
- Buttons: 13px, 7px 14px padding, radius 8px. Primary = filled accent.
  Secondary = transparent with --btn-border.
- Cards: --surface bg, 0.5–1px --card-border, radius 12px, 16px padding.
  Card = badge, title (14–15px/500), 1–2 line description, mono tech-tag line.
- Status badge: mono 11px, 3px 9px padding, radius 8px, lowercase.
- Recent-posts list: plain rows (title left, mono date right) with hairline
  separators. Never cards, never thumbnails.
- Footer: --band background, mono 11.5px, copyright left / links right.
- Hover affordance: underline or border-color shift only. No lifts, no shadows,
  no scale transforms.

## Landing page (5 zones, in order — copy is approved, use verbatim)
1. Nav: mono wordmark "roy yang" left; about · projects · strategies · blog ·
   theme toggle right.
2. Hero (max-width ~580px):
   - eyebrow (mono, accent): "notes on markets, machine learning & ai agents"
   - h1 (serif): "Hi, I'm Roy."
   - p1: "I've spent 13 years working with data in banking and insurance — and I
     still get a kick out of building things. Evenings and weekends, I tinker with
     trading systems and AI agent tooling on my Mac."
   - p2: "This site is where I share what I'm building and what I learn along the
     way — including the dead ends and the bugs that taught me the most."
   - actions: [my cv](primary, /Roy_Yang_CV.pdf) · github · linkedin · say hello
3. "things i've built": 3 cards (QuantPulse · Agentic coding framework · Local AI
   infrastructure) with status badges backtested / daily driver / researching.
4. "recent notes": latest 3 posts as plain dated rows.
5. Footer band: "© <year> roy yang · toronto" / "github · linkedin · rss".

## Voice & tone (applies to all site copy the agent writes or edits)
- First person, conversational, specific. Write like explaining to a colleague
  over coffee.
- Lead with the interesting thing, not the credential. "How backtests lie to you"
  beats "An analysis of point-in-time correctness."
- Honest about status and limitations; failures and dead ends are content, not
  embarrassments.
- Banned phrases: "passionate about", "leveraging", "cutting-edge", "transform
  your", "comprehensive guide", "in today's fast-paced world", and any sentence
  that could appear on any other person's site unchanged.
- No emoji anywhere on the site.

## Do-not list (hard)
No stock photos · no gradients/mesh/particle backgrounds · no animated typing ·
no skill progress bars · no carousels · no scrolljacking · no testimonials ·
no newsletter modal · no cookie-banner-style popups · no shadows beyond a
functional focus ring · no third-party fonts loaded from Google's CDN at runtime
(self-host via @fontsource).

## Imagery
Charts/figures from notebooks are the site's imagery. Style matplotlib output to
match: warm white figure bg (#FBFBF8), green-charcoal text, forest/honey/sage/taupe
as the categorical cycle. Ship a small `royplot.mplstyle` in the repo (Phase 4)
so every published figure matches the site automatically.
