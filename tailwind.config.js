/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    // "./mysite/polls/src/*.{html,js,svelte}",
    "./mysite/other/**/*.{html,js,svelte}",
    "./mysite/polls/**/*.{html,js,svelte}",
    "./mysite/htmx_todo/**/*.{html,js,svelte}",
    "./mysite/htmx_lookup/**/*.{html,js,svelte}",
    "./mysite/common/**/*.{html,js,svelte}",
    "./mysite/registration/**/*.{html,js,svelte}",
    "./mysite/htmx_form/**/*.{html,js,svelte}",
    "./mysite/alpine/**/*.{html,js,svelte}",
    "./mysite/hyperscript/**/*.{html,js,svelte}",
    "./mysite/svelte_demo/**/*.{html,js,svelte}",
    "./mysite/htmx_fragments/**/*.{html,js,svelte}",

    // // "./mysite/svelte_leaflet/**/*.{html,js,svelte}",
    "./mysite/svelte_leaflet_2/**/*.{html,js,svelte}",
    // Error: both lines below cause an infinite reload loop
    // "./mysite/**/*.{html,js,svelte}",
    // "./mysite/*/src/*.svelte"
  ],
  theme: {
    extend: {
      // 'animation' & 'keyframes' set the dash length and animation for the leaflet curve line
      // --dash-length '18' needs to be equal to the sum of the Curve dashArray
      animation: {
        'dash-offset': 'dash-offset var(--animation-speed, 2s) linear infinite',
      },
      keyframes: {
        'dash-offset': {
          from: {
            'stroke-dashoffset': 'var(--dash-length, 18)',
          },
          to: {
            'stroke-dashoffset': '0',
          },
        },
      },
    },
  },
  plugins: [],
}