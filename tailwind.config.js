/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    // "./mysite/polls/src/*.{html,js,svelte}",
    "./mysite/other/**/*.{html,js,svelte}",
    "./mysite/sform/**/*.{html,js,svelte}",
    "./mysite/polls/**/*.{html,js,svelte}",
    "./mysite/htmx_todo/**/*.{html,js,svelte}",
    "./mysite/htmx_lookup/**/*.{html,js,svelte}",
    "./mysite/common/**/*.{html,js,svelte}",
    "./mysite/registration/**/*.{html,js,svelte}",
    "./mysite/htmx_form/**/*.{html,js,svelte}",
    // Error: both lines below cause an infinite reload loop
    // "./mysite/**/*.{html,js,svelte}",
    // "./mysite/*/src/*.svelte"
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}