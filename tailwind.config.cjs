/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  darkMode: 'class', // Pure white theme strictly enforced; no dark class applied
  theme: {
    extend: {
      colors: {
        brand: {
          50: '#fef2f2',
          100: '#fee2e2',
          200: '#fecaca',
          700: '#b91c1c',
          800: '#991b1b',
          900: '#7f1d1d', // Dark Red / Burgundy for legal titles
          950: '#450a0a',
        },
        legal: {
          red: '#8b0000',
          darkred: '#7f1d1d',
          charcoal: '#111827',
          gray: '#374151',
          border: '#e5e7eb',
          bg: '#ffffff',
        }
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', '-apple-system', 'Segoe UI', 'sans-serif'],
        serif: ['Merriweather', 'Georgia', 'Cambria', 'Times New Roman', 'serif'],
        mono: ['JetBrains Mono', 'Courier New', 'monospace'],
      },
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
};
