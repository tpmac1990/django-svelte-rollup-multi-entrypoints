# Django/svelte project with multiple entry points
This project displays how to create a django project with multiple entry points for svelte components with hot reloading.
This allows an application to be built with the django template system, and then selectively use svelte components
in any given template. Rollup is used as the bundler rather than webpack.

## Run project
run django server:
`source venv/bin/activate`
`python3 manage.py runserver`
goto `localhost:8000`
run svelte server:
`npm install`
`npm run dev`

