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

## setup

### Tailwind
A slightly different setup is required so tailwind css is incorporated within svelte livereload
https://www.youtube.com/watch?v=RUVLnECJNrw
https://dev.to/ardc_overflow/setting-up-svelte-and-tailwind-with-minimal-extra-dependencies-1g5a


## To implement
- state management
- api style calls


## Issues

### bundle tracker
I have not found a bundle tracker like `django-webpack-loader` for django-rollup. The closest I have gotten is 
`rollup-plugin-output-manifest` which spits out a `manifest.json` file with an object linking the name to their name.hash 
match. 
https://github.com/shuizhongyueming/rollup-plugin-output-manifest/tree/master/packages/main 
this may justify using webpack to utilize: https://github.com/django-webpack/django-webpack-loader

### css/tailwind livereload
css changes associated with tailwind are not being applied in the browser if no changes have been made for around 10 minutes. Livereload
appears to be working, so it is likely a cache issue. Clearing browser cache or restarting svelte server in a current fix.

### infinite reload
The addition of Tailwind and its required `tailwind.config.js` file has created an issue with livereload. Using regex in the `content`
paths can cause an infinite reload loop on the dev server. 
This works:
>"./mysite/polls/src/*.{html,js,svelte}"
this does not:
>"./mysite/*/src/*.{html,js,svelte}"

### default port 8080 always taken
This may just require a restart. The svelte dev server never connects to port 8080 as it is always taken.

### Broken pipe, django server
A `Broken pipe from ('127.0.0.1', 51428)` error occurs on the django server when I pass data to svelte using the `window` object with `window.props`. 
Found this explanation: 
>I understand that a 'broken pipe' error occurs when the browser sends a request but does not wait for the response and closes the connection.
It does not seem to create any problems.




### packages
https://www.npmjs.com/package/rollup-plugin-output-manifest
https://www.npmjs.com/package/rollup-plugin-styles using this one at the moment as it doesn't build a bundle.css file.
https://www.npmjs.com/package/rollup-plugin-css-only.
Not sure of a way to create a hash for the css file and add it to the manifest file to prevent caching