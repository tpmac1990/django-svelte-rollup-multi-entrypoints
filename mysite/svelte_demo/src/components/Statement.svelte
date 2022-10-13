<script>
	let count = 0;

	$: if (count >= 10) {
		alert('count is dangerously high!');
		count = 9;
	}

	function handleClick() {
		count += 1;
	}
</script>

<section class="mt-10 mb-4 bg-slate-100 p-10">
	<h2 class="text-2xl mb-4 text-slate-600">Statement</h2>
	<p>$: reactivity if statment to trigger alert when count reaches 10</p>
	<button 
		class="text-white px-5 py-3 mt-3 text-lg bg-sky-800 hover:bg-slate-500"
		on:click={handleClick}
	>
	Clicked {count} {count === 1 ? 'time' : 'times'}
	</button>
</section>

