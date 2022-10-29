<script>
    import L from "leaflet";
    import { setContext, onMount } from "svelte";

    export let initialBounds;
  
    let mapContainer;
    export let map = L.map(L.DomUtil.create("div"), {
        center: [35, -100],
        zoom: 4,
        maxBounds: initialBounds,
        minZoom: 4,
    });
    setContext("leafletMapInstance", map);
  
    L.tileLayer("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png ", {
      attribution:
        'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>',
    }).addTo(map);
  
    onMount(() => {
      mapContainer.appendChild(map.getContainer());
      map.getContainer().style.width = "100%";
      map.getContainer().style.height = "100%";
      map.invalidateSize();
    });

</script>

<div class="w-full h-[950px]" bind:this="{mapContainer}">
    <slot {map} />
</div>