import svelte from 'rollup-plugin-svelte';
import commonjs from '@rollup/plugin-commonjs';
import resolve from '@rollup/plugin-node-resolve';
// import livereload from 'rollup-plugin-livereload';
import { terser } from 'rollup-plugin-terser';
// import css from 'rollup-plugin-css-only';
import styles from "rollup-plugin-styles";
import del from 'rollup-plugin-delete'
import sveltePreprocess from 'svelte-preprocess';
import outputManifest from 'rollup-plugin-output-manifest';
import json from "@rollup/plugin-json";
var path = require("path");

const production = !process.env.ROLLUP_WATCH;
const public_dir = path.resolve(__dirname, 'mysite/svelte/public/')

function serve() {
	let server;

	function toExit() {
		if (server) server.kill(0);
	}

	return {
		writeBundle() {
			if (server) return;
			server = require('child_process').spawn('npm', ['run', 'start', '--', '--dev'], {
				stdio: ['ignore', 'inherit', 'inherit'],
				shell: true
			});

			process.on('SIGTERM', toExit);
			process.on('exit', toExit);
		}
	};
}

export default {
	input: {
        main: path.resolve(__dirname, 'mysite/polls/src/main.js'),
        other: path.resolve(__dirname, 'mysite/other/src/other.js'),
		svelte_demo: path.resolve(__dirname, 'mysite/svelte_demo/src/main.js'),
		// leaflet: path.resolve(__dirname, 'mysite/svelte_leaflet/src/main.js'),
		leaflet_2: path.resolve(__dirname, 'mysite/svelte_leaflet_2/src/main.js'),
		// output: path.resolve(__dirname, 'mysite/common/src/output.css')
    },
    output: {
        sourcemap: false,
        format: 'esm',
        dir: path.resolve(public_dir, 'build/'),
		entryFileNames: `[name]${production && '.[hash]' || ''}.js`,
		// // using '[name].[hash].js' in development breaks hot-reload
        chunkFileNames: `[name]${production && '-[hash]' || ''}.js`,
		assetFileNames: "[name]-[hash][extname]", // .css file
    },
	plugins: [
		del({ targets: path.resolve(public_dir, 'build/*{.,-}*.{js,css}') }), // only delete chunk files, other files will be over written
		svelte({
			compilerOptions: {
				// enable run-time checks when not in production
				dev: !production
			},
			// This tells svelte to run some preprocessing
			preprocess: sveltePreprocess({
				postcss: true,  // And tells it to specifically run postcss!
				babel: {
					presets: [
							[
								'@babel/preset-env',
								{
									targets: {
										node: 'current'
									}
								}
							]
						],
					},
			}),
		}),
		// create a manifest file to match file names with their hash equivalents
		outputManifest({fileName: path.resolve('mysite', 'manifest.json')}),
		// we'll extract any component CSS out into
		// a separate file - better for performance
		// css({ output: `bundle.css` }),
		styles({
			mode: ["extract", "bundle.css"],
		}),

		// If you have external dependencies installed from
		// npm, you'll most likely need these plugins. In
		// some cases you'll need additional configuration -
		// consult the documentation for details:
		// https://github.com/rollup/plugins/tree/master/packages/commonjs
		resolve({
			browser: true,
			dedupe: ['svelte']
		}),
		commonjs(),
		
		// Converts .json files to ES6 modules
		json(),

		// In dev mode, call `npm run start` once
		// the bundle has been generated
		!production && serve(),

		// Watch the `public` directory and refresh the
		// browser on changes when not in production
		// NOTE: no need for livereload as django_browser_reload will trigger a reload on change.
		// !production && livereload(public_dir),

		// If we're building for production (npm run build
		// instead of npm run dev), minify
		production && terser()
	],
	watch: {
		clearScreen: false
	}
};
