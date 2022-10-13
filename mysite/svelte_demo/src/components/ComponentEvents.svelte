<script>
	import ComponentEventsInner from './ComponentEventsInner.svelte';

	function handleMessage(event) {
		alert(event.detail.text);
	}
</script>


<section class="mt-10 mb-4 bg-slate-100 p-10">
	<h2 class="text-2xl mb-4 text-slate-600">Component Events</h2>
	<p>dispatch event from child component</p>
    <ComponentEventsInner on:message={handleMessage}/>
</section>