<script>
    // equals undefined by default to solver error "<ComponentName> was created without expected prop 'segment'"
    import { getContext } from 'svelte';
    import { getInitialHobbies, postHobby, deleteHobby } from "../api/hobby";

    let { csrfToken } = getContext('csrfToken')
    
    let hobby
    let hobbies
    let hobbyForm
    let keys
    let formValues
    let resp

    // load the form
    async function handleClick() {
        hobby = await getInitialHobbies(csrfToken);
        hobbyForm = hobby.form.fields
        hobbies = hobby.hobbies
        keys = Object.keys(hobbyForm)
        formValues = hobby.form.initial
    }

    async function handleFormSubmit(e){
        e.preventDefault()
        resp = await postHobby(csrfToken, formValues)
        hobbies = resp.hobbies
        console.log(resp.msg)
        formValues = hobby.form.initial
        // bodyFormData = new FormData();
        // bodyFormData.append('name', name);
    }

    async function deleteHandler(id){
        resp = await deleteHobby(csrfToken, id)
        // drop the hobby using filter instead of pass a new hobbies object in the response
        hobbies = hobbies.filter(hobby => {
            return hobby.id !== id
        })
        console.log(resp.msg)
    }

</script>

<section class="mt-10 mb-4 bg-slate-100 p-10">
	<h2 class="text-2xl mb-4 text-slate-600">Fetch data</h2>
	<p>Use axios api to fetch data from django view</p>
	<button 
		class="text-white px-5 py-3 mt-3 text-lg bg-sky-800 hover:bg-slate-500"
		on:click={handleClick}
	>
	Get Hobby form
	</button>
    {#if hobbyForm}
        <h2 class="text-xl pl-2 py-1">Hobby form</h2>
        <form on:submit={handleFormSubmit}>
            {#each keys as key }
                <label for="hobby-form-{key}" >{hobbyForm[key].label}</label>
                {#if hobbyForm[key].input_type == 'text' }
                    <input id="hobby-form-{key}" name="hobby-form-{key}" type="text" bind:value={formValues[key]} />
                {:else}
                    <input id="hobby-form-{key}" name="hobby-form-{key}" type="checkbox" bind:checked={formValues[key]} />
                {/if }
            {/each}
            <br>
            <input type="submit" value="Submit" /> 
        </form>
    {/if}
    <br>
    {#if hobbies}
        <h2 class="text-xl pl-2 py-1">Existing Hobbies</h2>
        <table class="table-auto w-full">
            <tr>
                <th class="border border-1 border-sky-700"></th>
                <th class="border border-1 border-sky-700">Name</th>
                <th class="border border-1 border-sky-700">Comment</th>
                <th class="border border-1 border-sky-700"></th>
            </tr>
            {#each hobbies as hobby, i (hobby.id)}
                <tr class="h-10">
                    <td class="border border-1 border-sky-700">{i+1}</td>
                    <td class="border border-1 border-sky-700 px-2">{hobby.name}</td>
                    <td class="border border-1 border-sky-700 px-2">{hobby.comment}</td>
                    <td class="border border-1 border-sky-700 px-2 text-xl hover:text-red-400" on:click={deleteHandler(hobby.id)}>x</td>
                </tr>
            {/each}
        </table>
    {/if}
</section>