<script>
	import { count } from '../stores/writablestore.js';

	let countValue;

    // subscribe to get the value from 'writablestore'
	count.subscribe(value => {
		countValue = value;
	});

    // update & reset are methods available with writable stores
    function decrement() {
		count.update(n => n - 1);
	}
    function increment() {
		count.update(n => n + 1);
	}
    function reset() {
		count.set(0);
	}

</script>


<section class="mt-10 mb-4 bg-slate-100 p-10">
	<h2 class="text-2xl mb-4 text-slate-600">Writable store</h2>
	<p>Use 'writable' store to manage 'count' value</p>
    <p class="text-xl my-2">The count is {countValue}</p>
    <button 
        class="text-white px-5 py-3 mt-3 text-lg bg-sky-800 hover:bg-slate-500"
        on:click={decrement}>
        -
    </button>
    <button 
        class="text-white px-5 py-3 mt-3 text-lg bg-sky-800 hover:bg-slate-500"
        on:click={increment}>
        +
    </button>
    <button 
        class="text-white px-5 py-3 mt-3 text-lg bg-sky-800 hover:bg-slate-500"
        on:click={reset}>
        reset
    </button>
</section>