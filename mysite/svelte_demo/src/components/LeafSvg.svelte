<script>
    import {LeafletMap, TileLayer} from 'svelte-leafletjs';
    import { onDestroy } from 'svelte';
    import MapMarker from './LeafSvgMarker.svelte'

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

</script>


<section class="mt-10 mb-4 bg-slate-100 p-10">
	<h2 class="text-2xl mb-4 text-slate-600">Leaflet Div marker</h2>
	<p>create custom marker from div/css/svg</p>
    <div class="h-[300px] w-full">
        <LeafletMap bind:this={map} options={mapOptions}>
            <TileLayer url={tileUrl} options={tileLayerOptions}/>
            <MapMarker latLng={[1.282375, 103.864273]} msg="this is a message" />
            <MapMarker latLng={[1.382375, 103.764273]} msg="this is another message" />
        </LeafletMap>
    </div>
</section>