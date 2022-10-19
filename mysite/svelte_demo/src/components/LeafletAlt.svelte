<script>
  // https://svelte.dev/repl/ad50c394a01241adb37438dc1891595d?version=3.23.2
  // https://stackoverflow.com/questions/62374265/svelte-with-leaflet
	import LeafletAltMap from './LeafletAltMap.svelte'
	import LeafletAltMarker from './LeafletAltMarker.svelte'
  import LeafletAltTiles from "./LeafletAltTiles.svelte"

  let size = '2'

  function clickHandler() {
		size = size === '1' ? '2' : '1'
	}

</script>


<section class="mt-10 mb-4 bg-slate-100 p-10">
	<h2 class="text-2xl mb-4 text-slate-600">Leaflet</h2>
	<p>create a leaflet map initially in a detached DOM (better method)</p>
  <button 
      class="text-white px-5 py-3 mt-3 text-lg bg-sky-800 hover:bg-slate-500"
      on:click={clickHandler}
  >Resize map</button>
  <div class="grid grid-cols-{size}">
    <LeafletAltMap size={size}>
      <LeafletAltTiles />
      <LeafletAltMarker lat=1.282375 lng=103.864273></LeafletAltMarker>
      <LeafletAltMarker lat=1.382375 lng=103.764273></LeafletAltMarker>
    </LeafletAltMap>
  </div>
</section>

