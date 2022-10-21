<script context="module">
    import * as L from 'leaflet';
    class Control extends L.Control {
        // el;
        constructor(
            el,
            position
        ) {
            super({ position });
            this.el = el;
        }
    
        onAdd() {
            return this.el;
        }
    
        onRemove() {}
    }

    // TODO: I need to add onDestroy 

</script>


  
<script>
    import { getContext, onDestroy } from 'svelte';
  
    let classNames;
    export { classNames as class };
  
    export let position;
    /** The control instance created by this component */
    export let control;
  
    let map = getContext('leafletMapInstance');
    function createControl(container) {
        control = new Control(container, position).addTo(map);
    }
</script>
  
<div class="hidden">
    <div use:createControl class={classNames}>
        {#if control}
            <slot {control} />
        {/if}
    </div>
</div>