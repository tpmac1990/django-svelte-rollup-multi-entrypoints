<script>
    import {
        createEventDispatcher,
        getContext,
        setContext,
        onDestroy,
    } from 'svelte';
    import * as L from 'leaflet';
    import flush from 'just-flush';
  
    export let latLngs;
    export let color;
    export let weight;
    export let opacity;
    export let pane;
    export let lineCap;
    export let lineJoin;
    export let fill;
    export let fillColor;
    export let className;
    export let dashArray;
    export let dashOffset;
    export let fillOpacity;
    export let fillRule;
    export let interactive = true;
    export let style;
  
    const dispatch = createEventDispatcher();
  
    let layerPane = pane || getContext('pane');
  
    let layerGroup = getContext('layerGroup')();
    export let line = new L.Polyline(
        latLngs,
        flush({
            interactive,
            className,
            pane: layerPane,
        })
    )
        .on('click', (e) => dispatch('click', e))
        .on('mouseover', (e) => dispatch('mouseover', e))
        .on('mouseout', (e) => dispatch('mouseout', e))
        .addTo(layerGroup);
  
    setContext('layer', () => line);
  
    $: lineStyle = flush({
        color,
        className,
        weight,
        opacity,
        dashArray,
        dashOffset,
        lineCap,
        lineJoin,
        fill,
        fillColor,
        fillOpacity,
        fillRule,
    });
  
    onDestroy(() => {
        line.remove();
    });
  
    $: if (style) {
        line.getElement()?.setAttribute('style', style);
    }
  
    $: line.setStyle(lineStyle);
  
    $: {
        line.setLatLngs(latLngs);
        line.redraw();
    }
</script>

<slot />
  