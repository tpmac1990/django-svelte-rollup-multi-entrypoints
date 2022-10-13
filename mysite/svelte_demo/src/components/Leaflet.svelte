<script>
    import {LeafletMap, TileLayer} from 'svelte-leafletjs';
    import { onDestroy } from 'svelte';
    import { watchResize } from "svelte-watch-resize";
    import MapMarker from './LeafletMapMarker.svelte'

    let map;

    const tileUrl = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
    const tileLayerOptions = {
        minZoom: 0,
        maxZoom: 20,
        maxNativeZoom: 19,
        attribution: "© OpenStreetMap contributors",
    };

    const mapOptions = {
        center: [1.364917, 103.822872],
        zoom: 10,
    };

	onDestroy(() => {
		if (map) map.getMap().remove();
	});

    let map_width = '2' 

	function clickHandler() {
		map_width = map_width === '1' ? '2' : '1'
	}

    function resizeMap(){
        // required to spread the map over the larger area.
        map.getMap().invalidateSize();
    }
</script>


<section class="mt-10 mb-4 bg-slate-100 p-10">
	<h2 class="text-2xl mb-4 text-slate-600">Leaflet</h2>
	<p>leaflet map with markers, popups & invalidatesize</p>
    <button 
        class="text-white px-5 py-3 mt-3 text-lg bg-sky-800 hover:bg-slate-500"
        on:click={clickHandler}
    >Resize map</button>
    <div class="grid grid-cols-{map_width}">
        <div class="h-[300px] w-full" use:watchResize={resizeMap}>
            <LeafletMap bind:this={map} options={mapOptions}>
                <TileLayer url={tileUrl} options={tileLayerOptions}/>
                <MapMarker latLng={[1.282375, 103.864273]} msg="this is a message" />
                <MapMarker latLng={[1.382375, 103.764273]} msg="this is another message" />
            </LeafletMap>
        </div>
    </div>
</section>