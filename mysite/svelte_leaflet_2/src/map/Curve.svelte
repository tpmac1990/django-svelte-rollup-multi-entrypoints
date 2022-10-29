<script>
    // https://github.com/elfalem/Leaflet.curve
    import { curve } from './leaflet.curve';
  
    import {
      createEventDispatcher,
      getContext,
      setContext,
      onDestroy,
    } from 'svelte';
    import flush from 'just-flush';
  
    export let path;
    export let color;
    export let className;
    export let dashArray;
    export let interactive = true;
    export let style;

    let weight;
    let opacity;
    let pane;
    let lineCap;
    let lineJoin;
    let fill;
    let fillColor;
    let dashOffset;
    let fillOpacity;
    let fillRule;
  
    const dispatch = createEventDispatcher();
  
    let layerPane = pane || getContext('pane');
  
    let map = getContext('leafletMapInstance');
    // @ts-ignore
    export let line = curve(
        path,
        flush({
            interactive,
            className,
            pane: layerPane,
        })
    )
        .on('click', (e) => dispatch('click', e))
        .on('mouseover', (e) => dispatch('mouseover', e))
        .on('mouseout', (e) => dispatch('mouseout', e))
        .addTo(map);
  
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
        line.getElement().setAttribute('style', style);
    }
  
    $: line.setStyle(lineStyle);
  
    $: {
        // @ts-ignore
        line.setPath(path);
        line.redraw();
    }
</script>
  
<slot />
  