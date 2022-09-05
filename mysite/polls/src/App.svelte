<script>

	let name = 'world'
	export let questions;
	export let question_text;

	import GlobalStyles from '../../common/src/GlobalStyles.svelte';
</script>

<GlobalStyles />

<main>
	<h1 class=''>Hello Ma DA {name}!</h1>
	<p>Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn how to build Svelte apps.</p>

	<!-- lazy loading -->
	{#await import("./Nested.svelte") then Module}
		<Module.default question_text={question_text} />
	{/await}

	<ul>
		{#each questions as prop}
			<li>{prop.question_text}</li>
		{/each}
	</ul>
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