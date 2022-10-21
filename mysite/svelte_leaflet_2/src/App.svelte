<script>
	import LeafletMap from './map/LeafletMap.svelte'
	import MapControls from './MapControls.svelte'

	import * as L from 'leaflet';
    // import {LeafletMap, TileLayer} from 'svelte-leafletjs';
    import { onDestroy, onMount } from 'svelte';
    import { watchResize } from "svelte-watch-resize";
	import { setContext } from 'svelte';

	import * as topojson from 'topojson-client';
	import { scaleSqrt } from 'd3-scale';
	// import MapControls from './MapControls.svelte';

	import topoData from '../data/topo.json';
	import msaData from '../data/msas.json';
	import flowsData from '../data/flows.json';

	let map;
	// show that we are getting the map fromo LeafletMap.svelte
	$: map, console.log('map', map)

	const initialBounds = L.latLngBounds([24, -126], [50, -66]);

	const features = topojson.feature(topoData, 'msas');
	console.log(features);

	let geojsons = new Map();
	for (let g of features.features) {
	  	geojsons.set(g.properties.CBSAFP, g);
	}

	let msas = new Map();
	for (let msa of msaData) {
		let geojson = geojsons.get(msa.id);
		let net = msa.totalIncoming - msa.totalOutgoing;
  
		msas.set(msa.id, {
			...msa,
			name: geojson.properties.NAME,
			net,
			netAsPercent: (100 * net) / msa.population,
			feature: geojson,
			outgoing: [],
			incoming: [],
		});
	}

	for (let [source, dest, count] of flowsData) {
		let sourceMsa = msas.get(source);
		let destMsa = msas.get(dest);
		if (!sourceMsa || !destMsa) {
			continue;
		}
	
		if (count > 0) {
			sourceMsa.outgoing.push({ id: dest, count });
			destMsa.incoming.push({ id: source, count });
		} else {
			count = -count;
			sourceMsa.incoming.push({ id: dest, count });
			destMsa.outgoing.push({ id: source, count });
		}
	}

	for (let msa of msas.values()) {
		msa.outgoing.sort((a, b) => b.count - a.count);
		msa.incoming.sort((a, b) => b.count - a.count);
	}

	console.log('msas', msas);

	const sortSettings = {
		all: {
			sort: (a, b) => b.netAsPercent - a.netAsPercent,
			limit: (list) => list,
		},
		largeNetPercent: {
			sort: (a, b) => b.netAsPercent - a.netAsPercent,
			limit: (list) => list.slice(0, 20).concat(list.slice(-20)),
		},
		largeNet: {
			sort: (a, b) => b.net - a.net,
			limit: (list) => list.slice(0, 20).concat(list.slice(-20)),
		},
	};

	let filterSetting = 'all';
	let activeMsas = [];
	$: {
		let sortedMsas = Array.from(msas.values()).sort(
			sortSettings[filterSetting].sort
		);
		activeMsas = sortSettings[filterSetting].limit(sortedMsas);
	}

	let countField = 'netAsPercent';
	$: colorBounds = activeMsas.reduce(
		(acc, msa) => {
			return {
			min: Math.min(acc.min, msa[countField]),
			max: Math.max(acc.max, msa[countField]),
			};
		},
		{ min: Infinity, max: -Infinity }
	);

	$: posColorScale = scaleSqrt()
		.domain([0, colorBounds.max])
		.range(['hsl(30, 100%, 80%)', 'hsl(30, 100%, 30%)']);
	$: negColorScale = scaleSqrt()
		.domain([0, -colorBounds.min])
		.range(['hsl(240, 100%, 80%)', 'hsl(240, 100%, 30%)']);
  
	$: netToColor = net => {
		if (net > 0) {
			return posColorScale(net);
		} else if (net < 0) {
			return negColorScale(-net);
		} else {
			return 'green';
		}
	};

	let clickMsa
	let hoverMsa
  
	let hoveringInList = false;
	$: infoMsa = hoverMsa || clickMsa;
	$: listMsa = hoveringInList ? clickMsa : infoMsa;
  
	let loaded = false;

	function linesForMsa(map, msa, n) {
		if (map || msa) {
			return [];
		}
  
		let centroidLatLng = L.latLng(msa.centroid[1], msa.centroid[0]);
	
		let incomingLines = msa.incoming.slice(0, n).map((flow) => {
			let source = msas.get(flow.id);
			let sourcePoint = L.latLng(source.centroid[1], source.centroid[0]);
			let path = makeLineCoordinates(map, sourcePoint, centroidLatLng, true);
			let percentOfMax = flow.count / msa.incoming[0].count;
			return {
				id: `${msa.id}:${source.id}`,
				path,
				color: 'hsl(30, 100%, 40%)',
				animationSpeed: 1000 + (1 - percentOfMax) * 3000 + 'ms',
			};
		});
  
		let outgoingLines = msa.outgoing.slice(0, n).map((flow) => {
			let dest = msas.get(flow.id);
			let destPoint = L.latLng(dest.centroid[1], dest.centroid[0]);
			let path = makeLineCoordinates(map, centroidLatLng, destPoint, false);
			let percentOfMax = flow.count / msa.outgoing[0].count;
			return {
				id: `${dest.id}:${msa.id}`,
				path,
				color: 'blue',
				animationSpeed: 1000 + (1 - percentOfMax) * 3000 + 'ms',
			};
		});
  
	  	return [...incomingLines, ...outgoingLines];
	}

	let topNFlows
	let lines = [];
	$: {
		// getMap will sometimes not be set yet, so we have to check
		// both for `map` and for `getMap` being set before trying to call it.
		if (map) {
				lines = [
				...linesForMsa(map, clickMsa, topNFlows),
				...(hoverMsa && hoverMsa !== clickMsa
					? linesForMsa(map, hoverMsa, topNFlows)
					: []),
				];
		}
	}
	$: lines, console.log('lines', lines)

	$: hasLines = new Set(lines.flatMap((l) => l.id.split(':')));
	let showLines = true;
  
	$: allShownMsas = Array.from(
		new Set([...hasLines, ...activeMsas.map((m) => m.id)]),
		(id) => msas.get(id)
	);
  
</script>


<section class="mt-10 mb-4 bg-slate-100 p-10">
	<h2 class="text-2xl mb-4 text-slate-600">Leaflet</h2>
	<p>create a leaflet map initially in a detached DOM (better method)</p>
	<div class="grid grid-cols-1">
		<LeafletMap bind:map={map}>
			<MapControls
					{initialBounds}
					{msas}
					{infoMsa}
					bind:showLines
					bind:topNFlows
					bind:filterSetting />
		</LeafletMap>
	</div>
</section>
  
  






<!-- <script>
	// https://stackoverflow.com/questions/62374265/svelte-with-leaflet
	import * as L from 'leaflet';
    import {LeafletMap, TileLayer} from 'svelte-leafletjs';
    import { onDestroy, onMount } from 'svelte';
    import { watchResize } from "svelte-watch-resize";
	import { setContext } from 'svelte';

	import * as topojson from 'topojson-client';
	import { scaleSqrt } from 'd3-scale';
	import MapControls from './MapControls.svelte';

	import topoData from '../data/topo.json';
	import msaData from '../data/msas.json';
	import flowsData from '../data/flows.json';

    let map;

	setContext("leafletMapInstance", () => map);

    const tileUrl = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
    const tileLayerOptions = {
        minZoom: 0,
        maxZoom: 20,
        maxNativeZoom: 19,
        attribution: "© OpenStreetMap contributors",
    };

	const initialBounds = L.latLngBounds([50.513, 294.038], [22.918, 231.987]);

    const mapOptions = {
		center: [38, 263],
        zoom: 5,
		maxBounds: initialBounds,
		minZoom: 4
    };

	onDestroy(() => {
		if (map) map.getMap().remove();
	});

    let map_width = '1' 

	function clickHandler() {
		map_width = map_width === '1' ? '2' : '1'
	}

    function resizeMap(){
        // required to spread the map over the larger area.
        map.getMap().invalidateSize();
    }

    const polygon1 = [[1.2605024,103.804856],[1.2595155,103.8058001],[1.2572416,103.8080317],[1.2555254,103.808418],[1.2549247,103.8096625],[1.2527365,103.8122374],[1.2507629,103.8157565],[1.2486177,103.8189322],[1.2460862,103.8224942],[1.2419673,103.8262707],[1.2378055,103.8309485],[1.2371619,103.8328797],[1.2374194,103.8341242],[1.2383204,103.8351113],[1.2383204,103.8356263],[1.238063,103.8371712],[1.2398221,103.8398749],[1.241195,103.841334],[1.2435977,103.8437373],[1.2460004,103.8454539],[1.2487035,103.8477713],[1.2523075,103.8492304],[1.2535517,103.8473851],[1.2536805,103.845883],[1.2531227,103.844381],[1.2528653,103.8425786],[1.2541953,103.8420636],[1.2540666,103.8404757],[1.2545386,103.838287],[1.2538092,103.8371283],[1.2537234,103.8350684],[1.255225,103.8321501],[1.2550534,103.829189],[1.2556112,103.8254124],[1.2581855,103.8233954],[1.2601591,103.8198763],[1.2608027,103.8168294],[1.2596443,103.8136965],[1.2605024,103.804856]];

    const polygonData = {
        polygon: polygon1,
        color: "#ff0000",
        fillColor: "#ff0000",
        popupMsg: "Sentosa",
        tooltipMsg: "Sentosa"
    }

    onMount(() => {
		console.log('help')
	});
    $: map, console.log(map)

	const features = topojson.feature(topoData, 'msas');
	console.log(features);

	let geojsons = new Map();
	for (let g of features.features) {
	  	geojsons.set(g.properties.CBSAFP, g);
	}

	let msas = new Map();
	for (let msa of msaData) {
		let geojson = geojsons.get(msa.id);
		let net = msa.totalIncoming - msa.totalOutgoing;
  
		msas.set(msa.id, {
			...msa,
			name: geojson.properties.NAME,
			net,
			netAsPercent: (100 * net) / msa.population,
			feature: geojson,
			outgoing: [],
			incoming: [],
		});
	}

	for (let [source, dest, count] of flowsData) {
		let sourceMsa = msas.get(source);
		let destMsa = msas.get(dest);
		if (!sourceMsa || !destMsa) {
			continue;
		}
	
		if (count > 0) {
			sourceMsa.outgoing.push({ id: dest, count });
			destMsa.incoming.push({ id: source, count });
		} else {
			count = -count;
			sourceMsa.incoming.push({ id: dest, count });
			destMsa.outgoing.push({ id: source, count });
		}
	}

	for (let msa of msas.values()) {
		msa.outgoing.sort((a, b) => b.count - a.count);
		msa.incoming.sort((a, b) => b.count - a.count);
	}

	console.log('msas', msas);

	const sortSettings = {
	  all: {
			sort: (a, b) => b.netAsPercent - a.netAsPercent,
			limit: (list) => list,
	  },
	  largeNetPercent: {
			sort: (a, b) => b.netAsPercent - a.netAsPercent,
			limit: (list) => list.slice(0, 20).concat(list.slice(-20)),
	  },
	  largeNet: {
			sort: (a, b) => b.net - a.net,
			limit: (list) => list.slice(0, 20).concat(list.slice(-20)),
	  },
	};

	let filterSetting = 'all';
	let activeMsas = [];
	$: {
		let sortedMsas = Array.from(msas.values()).sort(
			sortSettings[filterSetting].sort
		);
		activeMsas = sortSettings[filterSetting].limit(sortedMsas);
	}

	let countField = 'netAsPercent';
	$: colorBounds = activeMsas.reduce(
		(acc, msa) => {
			return {
			min: Math.min(acc.min, msa[countField]),
			max: Math.max(acc.max, msa[countField]),
			};
		},
		{ min: Infinity, max: -Infinity }
	);

	$: posColorScale = scaleSqrt()
		.domain([0, colorBounds.max])
		.range(['hsl(30, 100%, 80%)', 'hsl(30, 100%, 30%)']);
	$: negColorScale = scaleSqrt()
		.domain([0, -colorBounds.min])
		.range(['hsl(240, 100%, 80%)', 'hsl(240, 100%, 30%)']);
  
	$: netToColor = net => {
		if (net > 0) {
			return posColorScale(net);
		} else if (net < 0) {
			return negColorScale(-net);
		} else {
			return 'green';
		}
	};

	let clickMsa
	let hoverMsa
  
	let hoveringInList = false;
	$: infoMsa = hoverMsa || clickMsa;
	$: listMsa = hoveringInList ? clickMsa : infoMsa;
  
	let loaded = false;

	function linesForMsa(map, msa, n) {
		if (map || msa) {
			return [];
		}
  
		let centroidLatLng = L.latLng(msa.centroid[1], msa.centroid[0]);
	
		let incomingLines = msa.incoming.slice(0, n).map((flow) => {
			let source = msas.get(flow.id);
			let sourcePoint = L.latLng(source.centroid[1], source.centroid[0]);
			let path = makeLineCoordinates(map, sourcePoint, centroidLatLng, true);
			let percentOfMax = flow.count / msa.incoming[0].count;
			return {
				id: `${msa.id}:${source.id}`,
				path,
				color: 'hsl(30, 100%, 40%)',
				animationSpeed: 1000 + (1 - percentOfMax) * 3000 + 'ms',
			};
		});
  
		let outgoingLines = msa.outgoing.slice(0, n).map((flow) => {
			let dest = msas.get(flow.id);
			let destPoint = L.latLng(dest.centroid[1], dest.centroid[0]);
			let path = makeLineCoordinates(map, centroidLatLng, destPoint, false);
			let percentOfMax = flow.count / msa.outgoing[0].count;
			return {
				id: `${dest.id}:${msa.id}`,
				path,
				color: 'blue',
				animationSpeed: 1000 + (1 - percentOfMax) * 3000 + 'ms',
			};
		});
  
	  	return [...incomingLines, ...outgoingLines];
	}

	let topNFlows
	let lines = [];
	$: {
		// getMap will sometimes not be set yet, so we have to check
		// both for `map` and for `getMap` being set before trying to call it.
		if (map){
			let m = map.getMap();
			if (m) {
					lines = [
					...linesForMsa(m, clickMsa, topNFlows),
					...(hoverMsa && hoverMsa !== clickMsa
						? linesForMsa(m, hoverMsa, topNFlows)
						: []),
					];
			}
		}
	}
	$: lines, console.log('lines', lines)

	$: hasLines = new Set(lines.flatMap((l) => l.id.split(':')));
	let showLines = true;
  
	$: allShownMsas = Array.from(
		new Set([...hasLines, ...activeMsas.map((m) => m.id)]),
		(id) => msas.get(id)
	);
    
</script>


<section class="mt-10 mb-4 bg-slate-100 p-10">
	<h2 class="text-2xl mb-4 text-slate-600">Leaflet</h2>
	<p>leaflet map with markers, popups, polygon & invalidatesize</p>
    <button 
        class="text-white px-5 py-3 mt-3 text-lg bg-sky-800 hover:bg-slate-500"
        on:click={clickHandler}
    >Resize map</button>
    <div class="grid grid-cols-{map_width}">
        <div class="h-[800px] w-full" use:watchResize={resizeMap}>
            <LeafletMap bind:this={map} options={mapOptions} >
				<MapControls
					{initialBounds}
					{msas}
					{infoMsa}
					bind:showLines
					bind:topNFlows
					bind:filterSetting />
            </LeafletMap>
        </div>
    </div>
</section> -->