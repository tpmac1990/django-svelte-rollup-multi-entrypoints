<script>
	import Animals from './CustomStoreAnimal.svelte';
	import {petStore} from '../stores/Petstore.js';	

    // // uncommenting this will overwrite the store. This is possible because 'set' was exported form the store
    // $petStore = []
</script>


<section class="mt-10 mb-4 bg-slate-100 p-10">
	<h2 class="text-2xl mb-4 text-slate-600">Custom store</h2>
    <p>custom store to include custom functions</p>
	<Animals {petStore} />
    <button 
        class="mt-6 w-20 text-white text-lg bg-cyan-600 hover:bg-slate-500"
        on:click={()=>petStore.reset()}
    >
        Reset
    </button>
</section>
