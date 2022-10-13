<script>
	let numbers = [1, 2, 3, 4];

	// make sure 'numbers is changed'
	function addNumber() {
		numbers = [...numbers, numbers.length + 1];
	}

	// 'numbers' value change will trigger this reactivity
	$: sum = numbers.reduce((t, n) => t + n, 0);
</script>

<section class="mt-10 mb-4 bg-slate-100 p-10">
	<h2 class="text-2xl mb-4 text-slate-600">Updating arrays and objects</h2>
	<p>$: reactivity while updating arrays and objects</p>
	<button 
		class="text-white px-5 py-3 mt-3 text-lg bg-sky-800 hover:bg-slate-500"
		on:click={addNumber}
	>
	Add a number
	</button>
	<p>{numbers.join(' + ')} = {sum}</p>
</section>

