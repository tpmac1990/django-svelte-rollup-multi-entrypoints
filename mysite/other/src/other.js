import Other from './Other.svelte';

const other = new Other({
	target: document.body,
	props: window.props
});

export default other;