<script>

    import {Marker, DivIcon, Popup} from 'svelte-leafletjs';

    export let latLng;
	export let msg;

</script>

<!-- add to css file to hide default white square -->
<!-- .leaflet-div-icon {
    width: 0 !important;
    height: 0 !important;
} -->

<Marker latLng={latLng}>
    <Popup>{msg}</Popup>
    <DivIcon>
        <div class="w-4 h-4 bg-red-600 rounded-full border border-2 border-white"></div>
        <!-- <svg>
            <polygon points="12,0 24,12 12,24 0,12" fill=#ef4444 stroke=lime stroke-width=1 />
            <line x1="12" y1="0" x2="12" y2="24" stroke-width=1 stroke="black" />
            <line x1="0" y1="12" x2="24" y2="12" stroke-width=1 stroke="black" />
        </svg> -->
    </DivIcon>
</Marker>