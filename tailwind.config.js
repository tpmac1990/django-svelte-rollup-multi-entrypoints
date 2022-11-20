/** @type {import('tailwindcss').Config} */

function content() {
  apps = [
    "alpine",
    "common",
    "htmx_form",
    "htmx_fragments",
    "htmx_lookup",
    "htmx_todo",
    "hyperscript",
    "images",
    "other",
    "polls",
    "registration",
    "svelte_demo",
    "svelte_leaflet",
    "svelte_leaflet_2",
  ]
  return apps.map(app => `./mysite/${ app }/**/*.{html,js,svelte}`)
  // It would be easier to use the below line, but it throws an infinite reload loop. I think it is related to 
  //  the svelte/public directory where the css file is built
  // "./mysite/**/*.{html,js,svelte}",
  // crispy / tailwind_forms suggest this is required. But it doesn't seem to be adding anything 
  // "./venv/lib/crispy_tailwind/**/*.{html,py,js}"
  // pySitePackages + "crispy_tailwind/**/*.{html,py,js}",
}


module.exports = {
  content: content(),
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
  plugins: [
    require('@tailwindcss/forms'),
  ],
}