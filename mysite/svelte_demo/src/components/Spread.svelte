<script>
	import App from '../../../svelte_leaflet_2/src/App.svelte';
import SpreadInfo from './SpreadInfo.svelte';

	const pkg = {
		name: 'svelte',
		version: 3,
		speed: 'blazing',
		website: 'https://svelte.dev'
	};
</script>

<section class="mt-10 mb-4 bg-slate-100 p-10">
	<h2 class="text-2xl mb-4 text-slate-600">Spread</h2>
	<p>pass values in an object as a spread (...obj)</p>
    <SpreadInfo {...pkg}/>
    <!-- <SpreadInfo name={pkg.name} version={pkg.version} speed={pkg.speed} website={pkg.website}/> -->
</section>