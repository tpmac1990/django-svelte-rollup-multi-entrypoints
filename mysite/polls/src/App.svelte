<script>

	let name = 'world'
	export let questions;
	export let question_text;

	import '../../common/src/styles.css';

	import { count } from '../../svelte/store/stores.js';
	import { other_count } from '../../svelte/store/counter.js';

	let countValue;

	count.subscribe(value => {
		countValue = value;
	});

	function increment() {
		count.update(n => n + 1);
	}
	function decrement() {
		count.update(n => n - 1);
	}
	function reset() {
		count.set(0);
	}
</script>


<main>
	<h1 class='underline'>Hello Ma DA {name}!</h1>
	<p class=''>Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn how to build Svelte apps.</p>

	<!-- lazy loading -->
	{#await import("./Nested.svelte") then Module}
		<Module.default question_text={question_text} />
	{/await}

	<ul>
		{#each questions as prop}
			<li>{prop.question_text}</li>
		{/each}
	</ul>

	<div class='my-5'>
		<h2 class='text-2xl'>The count is {countValue}</h2>
		<button on:click={increment}>+</button>
		<button on:click={decrement}>-</button>
		<button on:click={reset}>reset</button>
		<br/>
	</div>

	<h2>The count is {$other_count}</h2>
	<button on:click={other_count.increment}>+</button>
	<button on:click={other_count.decrement}>-</button>
	<button on:click={other_count.reset}>reset</button>
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