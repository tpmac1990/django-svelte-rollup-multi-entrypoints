<script>
    // equals undefined by default to solver erro "<ComponentName> was created without expected prop 'segment'"
    export let csrfToken = undefined;
    import { getHobbies } from "../api/hobby";

    let hobbies

    async function handleClick() {
        hobbies = await getHobbies(csrfToken);
        console.log(hobbies)
    }

</script>

<section class="mt-10 mb-4 bg-slate-100 p-10">
	<h2 class="text-2xl mb-4 text-slate-600">Fetch data</h2>
	<p>Use axios api to fetch data from django view</p>
	<button 
		class="text-white px-5 py-3 mt-3 text-lg bg-sky-800 hover:bg-slate-500"
		on:click={handleClick}
	>
	Get Clubs
	</button>
    <!-- {#if clubs}
        <h2 class="text-xl pl-2 py-1">Clubs list</h2>
        <ul class="border border-1 border-sky-600 py-1 pl-2">
            {#each clubs as club }
                <li class="py-1">{club.name}</li>
            {/each}
        </ul>
    {/if} -->
</section>