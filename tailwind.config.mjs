/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,ts,md,mdx}'],
  theme: {
    extend: {
      colors: {
        // DESIGN.md tokens — values live as CSS variables in src/styles/global.css
        bg: 'var(--bg)',
        surface: 'var(--surface)',
        band: 'var(--band)',
        text: 'var(--text)',
        'text-2': 'var(--text-2)',
        'text-muted': 'var(--text-muted)',
        hairline: 'var(--hairline)',
        'card-border': 'var(--card-border)',
        'btn-border': 'var(--btn-border)',
        accent: 'var(--accent)',
        'accent-text': 'var(--accent-text)',
      },
      fontFamily: {
        serif: ['"Source Serif 4"', 'Georgia', 'serif'],
        sans: ['"Inter Variable"', 'Inter', 'system-ui', 'sans-serif'],
        mono: ['"JetBrains Mono"', 'ui-monospace', 'monospace'],
      },
    },
  },
  plugins: [],
};
