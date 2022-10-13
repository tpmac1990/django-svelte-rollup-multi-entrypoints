<script>
	let count = 0;

	function incrementCount() {
		count += 1;
	}
</script>

<section class="mt-10 mb-4 bg-slate-100 p-10">
	<h2 class="text-2xl mb-4 text-slate-600">Simple Counter</h2>
	<p>simple on click event counter</p>
	<button 
		class="text-white px-5 py-3 mt-3 text-lg bg-sky-800 hover:bg-slate-500"
		on:click={incrementCount}
	>
		Clicked {count} {count === 1 ? 'time' : 'times'}
	</button>
</section>
