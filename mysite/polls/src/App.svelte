<script>
	// non-dynamic import of nested component
	// import Nested from './Nested.svelte';
	export let name;
</script>

<main>
	<h1>Hello Ma DA {name}!</h1>
	<p>Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn how to build Svelte apps.</p>
	<!-- <Nested/> -->
	{#await import("./Nested.svelte") then Module}
		<Module.default />
	{/await}
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>