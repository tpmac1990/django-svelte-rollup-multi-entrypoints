<script>
    import { getContext, setContext } from 'svelte'

    import ContextSubComponent from "./ContextSubComponent.svelte";

    const userDetails = getContext('user-details')

    // overwrite the context
    const userDetailsChange = { username: 'xyz@example.com', islogin: 'no' };
    setContext('user-details', userDetailsChange )
    
</script>

<table class="mb-4">
    <tr>
        <td class="font-medium pr-4">User Name:</td>
        <td>{ userDetails.username }</td>
    </tr>
    <tr>
        <td class="font-medium pr-4">User Login Status:</td>
        <td>{ userDetails.islogin }</td>
    </tr>
</table>
<ContextSubComponent />
