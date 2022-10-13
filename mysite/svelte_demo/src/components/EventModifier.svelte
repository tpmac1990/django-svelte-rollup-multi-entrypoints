<script>
	function handleClick() {
		alert('no more alerts')
	}
</script>

<section class="mt-10 mb-4 bg-slate-100 p-10">
	<h2 class="text-2xl mb-4 text-slate-600">Event Modifier</h2>
	<p>alert only occurs on first click</p>
    <button 
        class="text-white px-5 py-3 mt-3 text-lg bg-sky-800 hover:bg-slate-500"
        on:click|once={handleClick}
    >
        Click me
    </button>
</section>