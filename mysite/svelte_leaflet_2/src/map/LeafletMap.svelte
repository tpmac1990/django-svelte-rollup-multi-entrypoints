<script>
    import L from "leaflet";
    import { setContext, onMount } from "svelte";
  
    let mapContainer;
    export let map = L.map(L.DomUtil.create("div"), {
        center: [1.364917, 103.822872],
        zoom: 10,
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

<div class="w-full h-[800px]" bind:this="{mapContainer}">
    <slot></slot>
</div>