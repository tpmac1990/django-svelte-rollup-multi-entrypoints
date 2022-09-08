<script>
	export let csrfToken;

	// import GlobalStyles from '../../common/src/GlobalStyles.svelte';

	import { onMount } from 'svelte';
	import { getTodoList } from "./todo";

	// let pokemonDetail = {};
	let todos

	// Get the data from the api, after the page is mounted.
	onMount(async () => {
		const res = await getTodoList(csrfToken);
		todos = res;
	});
</script>

<!-- <GlobalStyles /> -->

<main>
	<h1 class='text-2xl underline'>Bye Ma Car World!</h1>
	<p>{csrfToken}</p>
	<p>{todos}</p>
</main>

<style>
	p {
		color: green;
	}
	
</style>