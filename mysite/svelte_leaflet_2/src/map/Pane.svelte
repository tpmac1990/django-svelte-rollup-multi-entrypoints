<script>
    import { getContext, setContext } from 'svelte';
  
    export let name;
    export let z;
  
    const map = getContext('leafletMapInstance');
  
    let pane = map.createPane(name);
    pane.style.zIndex = z;
    setContext('pane', pane);
    
</script>
  
<slot />