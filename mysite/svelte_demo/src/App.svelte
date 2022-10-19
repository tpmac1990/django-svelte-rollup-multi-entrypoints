<script>

	import { setContext } from 'svelte';

	import '../../common/src/styles.css';

	export let csrfToken; // only here to hide error in console
	setContext('csrfToken', {'csrfToken': csrfToken});

</script>


<main class="container mx-auto my-6 pb-20 max-w-xl">
	<h1 class="text-red-500 uppercase text-6xl font-thin my-4">Svelte demo</h1>
	
	<!-- TODO -->
	<!-- {#await import("./components/LeafMultiFeature.svelte") then LeafMultiFeature}
		<LeafMultiFeature.default />
	{/await} -->

	
	
	<!-- need to add edit method -->
	<!-- {#await import("./components/FormSubmit.svelte") then FormSubmit}
		<FormSubmit.default />
	{/await} -->

	<!-- {#await import("./components/ApiCall.svelte") then ApiCall}
		<ApiCall.default />
	{/await} -->

	<!-- {#await import("./components/LeafSvg.svelte") then LeafSvg}
		<LeafSvg.default />
	{/await} -->

	{#await import("./components/LeafletAlt.svelte") then LeafletAlt}
		<LeafletAlt.default />
	{/await}

	<!-- {#await import("./components/Leaflet.svelte") then Leaflet}
		<Leaflet.default />
	{/await} -->

	<!-- {#await import("./components/Slot.svelte") then Slot}
		<Slot.default />
	{/await}

	{#await import("./components/Context.svelte") then Context}
		<Context.default />
	{/await}

	{#await import("./components/WritableStore.svelte") then WritableStore}
		<WritableStore.default />
	{/await}

	{#await import("./components/CustomStore.svelte") then CustomStore}
		<CustomStore.default />
	{/await}

	{#await import("./components/CounterSimple.svelte") then CounterSimple}
		<CounterSimple.default />
	{/await}

	{#await import("./components/Declaration.svelte") then Declaration}
		<Declaration.default />
	{/await}

	{#await import("./components/Statement.svelte") then Statement}
		<Statement.default />
	{/await}

	{#await import("./components/ArraysAndObjects.svelte") then ArraysAndObjects}
		<ArraysAndObjects.default />
	{/await}
	
	{#await import("./components/Spread.svelte") then Spread}
		<Spread.default />
	{/await}

	{#await import("./components/EventModifier.svelte") then EventModifier}
		<EventModifier.default />
	{/await}

	{#await import("./components/ComponentEvents.svelte") then ComponentEvents}
		<ComponentEvents.default />
	{/await} -->

</main>
    