<script>
    import * as L from 'leaflet';
    import flush from 'just-flush';
    import {
        getContext,
        setContext,
        onDestroy,
        createEventDispatcher,
    } from 'svelte';
  
    const dispatch = createEventDispatcher();
    
    let pane;
    
    export let geojson;
    export let color;
    export let fillColor;
    export let fillOpacity;
    export let weight;
  
    const map = getContext("leafletMapInstance")
    let layerPane = pane || getContext('pane');
    export let layer = L.geoJSON(geojson, flush({ pane: layerPane }))
        .on('mouseover', (e) => dispatch('mouseover', e))
        .on('mouseout', (e) => dispatch('mouseout', e))
        .on('click', (e) => dispatch('click', e))
        .addTo(map);
  
    setContext('layer', () => layer);
  
    onDestroy(() => {
        layer.remove();
    });
  
    $: layerStyle = flush({ color, fillColor, fillOpacity, weight });
    $: layer.setStyle(layerStyle);
</script>

<slot />