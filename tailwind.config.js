/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./mysite/polls/src/*.{html,js,svelte}",
    "./mysite/other/src/*.{html,js,svelte}",
    // Error: both lines below cause an infinite reload loop
    // "./mysite/**/*.{html,js,svelte}",
    // "./mysite/*/src/*.svelte"
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}