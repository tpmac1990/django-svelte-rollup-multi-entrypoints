<script>
	export let petStore;
	
</script>

{#each $petStore as {name, color, animal, bought}, index}
	<div class="flex flex-wrap border mt-2 px-4 border-sky-700 items-center h-16">
		<div class="flex-auto">
            {name} is a {color} {animal}. 
        </div>
		{#if bought}
			<b class="pr-6 text-lg text-emerald-600">Sold</b>
		{:else}
			<button 
                class="mt-2 w-20 text-white text-lg bg-sky-800 hover:bg-slate-500"
                on:click={()=>petStore.buy(index)}
            >Buy</button>
		{/if}
	</div>
{/each}
