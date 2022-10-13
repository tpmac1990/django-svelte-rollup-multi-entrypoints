<script>

    import { setContext } from 'svelte'

    const userDetails = { username: 'abc@example.com', islogin: 'yes' };

    setContext('user-details', userDetails )

    import ContextComponent from "./ContextComponent.svelte";

</script>


<section class="mt-10 mb-4 bg-slate-100 p-10">
	<h2 class="text-2xl mb-4 text-slate-600">Context</h2>
	<p class="my-3">Use context to manage state</p>
	<ContextComponent />
</section>