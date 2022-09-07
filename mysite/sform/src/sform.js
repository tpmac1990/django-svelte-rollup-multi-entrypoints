import Sform from './Sform.svelte';

const sform = new Sform({
	target: document.body,
	props: window.props
});

export default sform;