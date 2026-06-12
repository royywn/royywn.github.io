import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import sitemap from '@astrojs/sitemap';

// site/base per ADR-002: user site at https://royywn.github.io, base '/'
export default defineConfig({
  site: 'https://royywn.github.io',
  base: '/',
  output: 'static',
  integrations: [
    tailwind({ applyBaseStyles: false }),
    sitemap(),
  ],
});
