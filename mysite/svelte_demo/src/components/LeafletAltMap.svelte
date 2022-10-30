<script>
    import L from "leaflet";
    import { setContext, onMount } from "svelte";

    export let size;
  
    let mapContainer;
    let map = L.map(L.DomUtil.create("div"), {
        center: [1.364917, 103.822872],
        zoom: 10,
    });
    setContext("leafletMapInstance", map);
  
    // // putting this here loads the tile layer quicker
    // L.tileLayer("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png ", {
    //   attribution:
    //     'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>',
    // }).addTo(map);
  
    onMount(() => {
      mapContainer.appendChild(map.getContainer());
      map.getContainer().style.width = "100%";
      map.getContainer().style.height = "100%";
      map.invalidateSize();
    });

    $: if (size){
      map.invalidateSize();
    }

</script>
  <svelte:head>
    <link
      rel="stylesheet"
      href="https://unpkg.com/leaflet@1.6.0/dist/leaflet.css"
      integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ=="
      crossorigin=""
    />
  </svelte:head>

<div class="w-full h-[400px]" bind:this="{mapContainer}">
    <slot></slot>
</div>