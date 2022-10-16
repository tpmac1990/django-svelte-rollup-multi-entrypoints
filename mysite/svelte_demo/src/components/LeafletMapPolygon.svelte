<script>

    import {Polygon, Popup, Tooltip} from 'svelte-leafletjs';

    export let polygon
    export let color
    export let fillColor
    export let popupMsg
    export let tooltipMsg

</script>


<Polygon latLngs={polygon} color={color} fillColor={fillColor}>
    <Popup>{popupMsg}</Popup>
    <Tooltip>{tooltipMsg}</Tooltip>
</Polygon>