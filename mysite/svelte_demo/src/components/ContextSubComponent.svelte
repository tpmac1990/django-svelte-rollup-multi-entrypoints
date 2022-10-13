<script>
    import { getContext } from 'svelte'

    const userDetails = getContext('user-details')

</script>

<table>
    <tr>
        <td class="font-medium pr-4">User Name:</td>
        <td>{ userDetails.username }</td>
    </tr>
    <tr>
        <td class="font-medium pr-4">User Login Status:</td>
        <td>{ userDetails.islogin }</td>
    </tr>
</table>