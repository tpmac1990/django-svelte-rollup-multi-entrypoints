# Django/svelte/htmx/alpine.js/hyperscript project with multiple entry points

## Stack
Centered around Django, this setup is designed to use django as much as possible. Where django alone is not sufficient, such as in the case of asynchronous tasks, htmx is the next choice, and finally when htmx does not cut it, then svelte is available. 
Here, Svelte uses Rollup as its bundler. It allows for multiple-entry points, so svelte apps can be extended from any django template.
This is setup with tailwind which can be used within both django templates and svelte components. Styling within svelte components and django templates is also possible. No attempt has been made to include sass. It is best to use tailwind as all css compiles to a single file, and tailwind will ensure that file size is kept as small as possible.

### Hot-reloading
Hot-reloading: Hot-reloading is activated in both svelte components and django templates. In Django this uses the `django-browser-reload` package.
To get hot-reloading to play ball across the stack while allowing the use of tailwind in both django and svelte, it was
necessary to alter the setup. Whenever a styling change is made, a new hashed css file is generated. This file is then imported into base django template and svelte components.
Note: remember to add new apps to the `tailwind.config.js` file so css changes are implemented.
`https://www.youtube.com/watch?v=RUVLnECJNrw`
`https://dev.to/ardc_overflow/setting-up-svelte-and-tailwind-with-minimal-extra-dependencies-1g5a`

### Managing hash files
I have not found a bundle tracker like `django-webpack-loader` for django-rollup. The closest I have gotten is `rollup-plugin-output-manifest` which spits out a `manifest.json` file with an object linking the name to their name.hash match, but this only generates the js files. It also does not provide a django package to load the hash files into a template. 
Solution: Use `rollup-plugin-output-manifest` to generate the js hash files, then use `rollup-plugin-styles` to output a hash css file. I created a template tag here `common/templatetags/hash_static.py` to load these files into django templates. E.g.
`{% load hash_static %}`
`{% hash_static 'build/bundle.css' %}`
This template tag uses the manifest.json file to lookup the equivalent js hash file. The css has file is not recorded here, but there is only one, so it looks for the only css file with the provided name.
rollup-plugin-output-manifest: `https://github.com/shuizhongyueming/rollup-plugin-output-manifest/tree/master/packages/main`
rollup-plugin-styles: `https://www.npmjs.com/package/rollup-plugin-styles`

### TODO
1. make image app to show how to deal with media (s3)
2. make elastic search app
3. setup postgis
4. minimise css
5. figure out deployment
6. testing

## s3 media file storage
`https://www.youtube.com/watch?v=nzLMA9WZqMM`
`https://stackoverflow.com/questions/67285752/django-static-files-uploaded-to-folder-in-amazon-s3-that-cant-be-found`
`https://django-storages.readthedocs.io/en/latest/`
`https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html`

## Python debugging in Docker container
There are two methods for debugging:
1. pdb
2. vs-code debugging

### pdb
use `import pdb; pdb.set_trace()` to insert a breakpoint in python code. Start the server with `docker-compose up`, then in a separate terminal run `docker attach app` with app being the container name. This terminal will allow interaction with the debugger.
It should also be possible to use `run` with `docker-compose run --rm app`, but I haven't tested this.
To make this function, I added the following to docker-compose:
```
stdin_open: true
tty: true
```
`breakpoint()` does not work. I am still trying to figure out why.

### vs-code debugging
Start the server with `docker-compose up`.
Place a `red-dot` debugger marker on the line of python code to inspect, then start the debugger with `Run > start debugger`. It should also be possible to start it with `F5`, but it doesn't work yet. Run the code and it will pause at the breakpoint. The debug panel on the left will show all active variables and the `DEBUG CONSOLE` in the terminal will allow you to interact using python.
To make this function, I added the following:
requirements.txt:
```
debugpy==1.6.3
```
docker-compose.yml
```
ports:
    - 3000:3000 
```
settings.py
```
# I have also seen this placed in manage.py 
if DEBUG:
    if os.environ.get('RUN_MAIN') or os.environ.get('WERKZEUG_RUN_MAIN'):
        import debugpy
        debugpy.listen(("0.0.0.0", 3000))
```
launch.json
```
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Run Django",
            "type": "python",
            "request": "attach", # attach to a existing docker container
            "pathMappings": [
                {
                    "localRoot": "${workspaceFolder}/mysite",
                    "remoteRoot": "/mysite"
                } # get these values from docker-compose volumes: - ./mysite:/mysite
            ],
            "port": 3000,
            "host": "127.0.0.1",
        }
    ]
}
```

Links:
`https://testdriven.io/blog/django-debugging-vs-code/`
`https://stackoverflow.com/questions/55956715/how-to-run-pdb-inside-a-docker-container`
`https://github.com/Microsoft/PTVS/issues/1057#issuecomment-421549892`
`https://medium.com/djangotube/dajngo-docker-compose-with-postgres-and-vs-code-debug-example-4875c6666674`




## Run project
run django server:
`source venv/bin/activate`
`python manage.py runserver`
goto `localhost:8000`
run svelte server:
`npm install`
`npm run dev`



## Run dev with Docker
`docker-compose build`
`docker-compose up`
This will start the svelte server, but it is slow. For quicker development comment out the node container in docker-compose.yml
and start the node server locally with `npm run dev`



### Frameworks / Libraries / bundler
django
htmx
hyperscript
alpine.js
svelte
tailwind
rollup

#### Svelte
https://dev.to/lukocastillo/svelte-3-how-to-connect-your-app-with-a-rest-api-axios-2h4e

Need to add `import '../../common/src/styles.css';` in the `<script>` tag to only one of the svelte components so changes
to the css will trigger livereload. I'm still not sure this is the best setup.




# Apps

## HX_Films / htmx_lookup

### Links
sortable: `https://github.com/SortableJS/Sortable`
django-widget-tweaks: `https://pypi.org/project/django-widget-tweaks/`
trigger with django-htmx:  `https://django-htmx.readthedocs.io/en/latest/http.html#django_htmx.http.trigger_client_event`
template fragments: `https://pypi.org/project/django-render-block/`

### Summary
An app to create a list of films. Existing Films can be searched for, or if they don't exist then they can be added. The users film list
    can be sorted using drag and drop. The results are paginated and more can be displayed by clicking the `More` button.
Uses: htmx
demonstrates: hx-swap-oob, hx-push-url, hx-trigger, django-render-block

### Setup
load database table from fixtures:
`python manage.py loaddata films.json`

### Features
hx-trigger (trigger another event): manages the total user film count. 
django-render-block: total film count is updated using a fragment within films.html rather than its own partial file.
hx-push-url: pushes the url to the film detail page. This would generally be easier to use the django method as a url
    still needs to be declared in urls.py
hx-swap-oob: disables the `More` button when there are no more films to display.

### Issues
triggering another event with `hx-trigger`: It doesn't seem possible to update using hx-trigger within a block that is 
updating from the original call. It would make sense to update this value with the original call as it lies with in it. 
Something that caught me out. 



## HX_Todo / htmx_todo

### Links
django-htmx: `https://django-htmx.readthedocs.io/en/latest/`
hyperscript: `https://hyperscript.org/`

### Summary
A basic todo app. Items can be added, removed and marked as complete. A single end-point was used for all htmx calls from which I utilised the django-htmx package to determine the call type. While this is useful, It is probably cleaner to use mulitple end-points.
hyperscript used to clear `new-todo` input after submitting.
Uses: htmx/ hyperscript

### Setup
load database table from fixtures:
`python manage.py loaddata todos.json`

### Issues
Trying to manage all htmx calls in the one end-point.



## Registration

### Summary
A basic registration app. Mostly plain django with one htmx feature to check the validity of the username
Uses: htmx



## HX_Form / htmx_form

### Links
django-render-block: `https://pypi.org/project/django-render-block/`

### Summary
Basic django form app which highlights the clean use of fragments, rather then the use of partials. There is only one template
in this app. All htmx calls re-use fragments from within the htmx_form/index.html file.
Uses: htmx
demonstrates: django-render-block



## Alpine

### Links
docs: `https://alpinejs.dev/`
tut: `https://www.youtube.com/watch?v=r5iWCtfltso`
mask plugin: `https://alpinejs.dev/plugins/mask`

### Summary
A bunch if small elements to demonstrate the various uses of Alpine.js. All code can be managed inside the html file like htmx, but it can also be coupled with other js files. This demonstrates; toggling, transitions, component & global level state management, for loops, conditionals, referencing elements, loading partials with axios. 
Uses: Alpine
demonstrates: events, transitions, state, masks


## Svelte leaflet

### Links
docs: `https://alpinejs.dev/`
tut: `https://www.youtube.com/watch?v=r5iWCtfltso`
mask plugin: `https://alpinejs.dev/plugins/mask`

### Summary
markers & lines app: `https://svelte.dev/repl/62271e8fda854e828f26d75625286bc3?version=3.50.1`
markers & lines app 2: `https://svelte.dev/repl/36a84bbe2cf74c899ada6380e6e632d8?version=3.29.7`
leaflet / svelte hackbuddy demo: `https://www.youtube.com/watch?v=-klB-EocorE&t=770s`
leaflet / svelte hackbuddy demo repo: `https://github.com/dimfeld/svelte-leaflet-demo/blob/master/full/src/App.svelte`
danial imfeld twitter: `https://twitter.com/dimfeld`
loading leaflet using onMount example: `https://dev.to/khromov/using-leaflet-with-sveltekit-3jn1`
leaflet / svelte with get/setcontext: `https://stackoverflow.com/questions/62374265/svelte-with-leaflet`
`https://gis.stackexchange.com/questions/302180/leaflet-invalidate-size-is-not-a-function-undefined`
svelte-leaflet docs: `https://ngyewch.github.io/svelte-leaflet/components/Popup`
my react-leaflet example: `https://github.dev/tpmac1990/atlas-prod/blob/main/src/components/map/MapContent.js`



## Issues

### infinite reload
The addition of Tailwind and its required `tailwind.config.js` file has created an issue with livereload. Using regex in the `content`
paths can cause an infinite reload loop on the dev server. 
This works:
>"./mysite/polls/**/*.{html,js,svelte}"
this does not:
>"./mysite/**/*.{html,js,svelte}"

### Broken pipe, django server
A `Broken pipe from ('127.0.0.1', 51428)` error occurs on the django server when I pass data to svelte using the `window` object with `window.props`. 
Found this explanation: 
>I understand that a 'broken pipe' error occurs when the browser sends a request but does not wait for the response and closes the connection.
It does not seem to create any problems.