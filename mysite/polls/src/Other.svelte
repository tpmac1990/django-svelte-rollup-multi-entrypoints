<script>
	export let questions;
	export let other;

	import Tailwindcss from './Tailwind.svelte';
</script>

<Tailwindcss />

<main>
	<h1>Bye Ma Car World!</h1>
	<p>find a list below:</p>
	<p>{other}</p>
	<ul>
		{#each questions as prop}
			<li>{prop.question_text}</li>
		{/each}
	</ul>
	<div class="text-2xl font-bold underline">
		<span>hello</span>
		<span>tailwind</span>
		<span>css</span>
	</div>
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