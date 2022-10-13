<script>
	import { createEventDispatcher } from 'svelte';

	const dispatch = createEventDispatcher();

	function sayHello() {
		dispatch('message', {
			text: 'Hello!'
		});
	}
</script>

<button 
    class="text-white px-5 py-3 mt-3 text-lg bg-sky-800 hover:bg-slate-500"
    on:click={sayHello}
>
	Click to say hello
</button>