<script>
	import SlotSub from './SlotSub.svelte';
</script>


<section class="mt-10 mb-4 bg-slate-100 p-10">
	<h2 class="text-2xl mb-4 text-slate-600">Slot</h2>
	<p>provide a slot within an element</p>
	<SlotSub>
        <h2>Hello!</h2>
        <p>This is a SlotSub. It can contain anything. The border is on the parent element</p>
    </SlotSub>
</section>