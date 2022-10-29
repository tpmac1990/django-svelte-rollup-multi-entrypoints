<script>
	import LeafletMap from './map/LeafletMap.svelte'
	import MapControls from './MapControls.svelte'

	import * as L from 'leaflet';
	import * as topojson from 'topojson-client';
	import { scaleSqrt } from 'd3-scale';
	import GeoJson from './map/GeoJson.svelte';
	import Pane from './map/Pane.svelte';
	import Curve from './map/Curve.svelte';
	import makeLineCoordinates from './map/curves';

	import topoData from '../data/topo.json';
	import msaData from '../data/msas.json';
	import flowsData from '../data/flows.json';

	let map;

	const initialBounds = L.latLngBounds([15, -166], [67, -65]);

	const features = topojson.feature(topoData, 'msas');

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
		if (!map || !msa) {
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

	$: hasLines = new Set(lines.flatMap((l) => l.id.split(':')));
	let showLines = true;
  
	$: allShownMsas = Array.from(
		new Set([...hasLines, ...activeMsas.map((m) => m.id)]),
		(id) => msas.get(id)
	);
  
</script>

<svelte:head>
	<link rel="stylesheet" href="https://unpkg.com/leaflet@1.6.0/dist/leaflet.css"
            integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ=="
            crossorigin=""/>
</svelte:head>


<section class="mb-4 bg-slate-100 p-10 h-[calc(100vh-80px)]">
	<h2 class="text-red-500 uppercase text-6xl font-thin my-4">Leaflet Demo</h2>
	<p class="mb-4">Leaflet map showing migration within USA</p>
	<div class="grid grid-cols-5">
		<div class="col-span-4">
			<LeafletMap {initialBounds} bind:map={map}>
				<MapControls
						{initialBounds}
						{infoMsa}
						bind:showLines
						bind:topNFlows
						bind:filterSetting
				/>
				{#each allShownMsas as msa (msa.id)}
					<GeoJson
						geojson={msa.feature}
						fillOpacity={0.6}
						fillColor={netToColor(msa[countField])}
						weight={hasLines.has(msa.id) ? 2 : 0}
						color="black"
						on:click={() => (clickMsa = msa)}
						on:mouseover={() => {
							hoverMsa = msa;
							hoveringInList = false;
						}}
						on:mouseout={() => {
							if (hoverMsa === msa) {
								hoverMsa = undefined;
							}
						}} 
					/>
				{/each}

				<Pane name="linePane" z={450} >
					{#if showLines}
						{#each lines as line}
							<Curve
								path={line.path}
								color={line.color}
								className="animate-dash-offset"
								dashArray="8 10"
								style="--animation-speed:{line.animationSpeed}"
								interactive={false} 
							/>
						{/each}
					{/if}
				</Pane>
			</LeafletMap>
		</div>
		<!-- numbers for top ten sources and destinations -->
		<div
			class="col-span-1 w-full text-base ml-4"
		>
			{#if listMsa}
				<div class="px-2 pb-2 border border-sky-700 mb-4">
					<p class="font-medium text-gray-800 py-2 border-b border-sky-700 w-full mb-2">Top Sources</p>
					{#each listMsa.incoming.slice(0, 10) as msa}
						<!-- svelte-ignore a11y-mouse-events-have-key-events -->
						<p
							class="hover:text-indigo-600 cursor-pointer"
							on:click={() => (clickMsa = msas.get(msa.id))}
							on:mouseover={() => {
								hoverMsa = msas.get(msa.id);
								hoveringInList = true;
							}}
							on:mouseout={() => (hoverMsa = null)}>
							<span class="truncate">{msas.get(msa.id).name}</span>
							<span class="whitespace-no-wrap">: {msa.count}</span>
						</p>
					{/each}
				</div>

				<div class="px-2 pb-2 border border-sky-700">
					<p class="font-medium text-gray-800 py-2 border-b border-sky-700 w-full mb-2">Top Destinations</p>
					{#each listMsa.outgoing.slice(0, 10) as msa}
						<!-- svelte-ignore a11y-mouse-events-have-key-events -->
						<p
							class="hover:text-indigo-600 cursor-pointer"
							on:mouseover={() => {
								hoverMsa = msas.get(msa.id);
								hoveringInList = true;
							}}
							on:mouseout={() => (hoverMsa = null)}
							on:click={() => (clickMsa = msas.get(msa.id))}>
							<span class="truncate">{msas.get(msa.id).name}</span>
							<span class="whitespace-no-wrap">: {msa.count}</span>
						</p>
					{/each}
				</div>
			{/if}
		</div>
	</div>
</section>
  