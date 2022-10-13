<script>

    import {Marker, Popup} from 'svelte-leafletjs';

    export let latLng;
	export let msg;

</script>


<Marker latLng={latLng}>
    <Popup>{msg}</Popup>
</Marker>