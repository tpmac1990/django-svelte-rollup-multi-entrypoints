import Other from './Other.svelte';

const other = new Other({
	target: document.body,
	props: {
		name: 'world'
	}
});

export default other;