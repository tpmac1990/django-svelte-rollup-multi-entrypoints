import {writable} from 'svelte/store';

const pets = [
		{name: 'Runny', animal: 'dog', color: 'black', bought: false},
		{name: 'Jumpy', animal: 'rabit', color: 'brown', bought: false},
		{name: 'Barky', animal: 'dog', color: 'brown', bought: false},
		{name: 'Meowy', animal: 'cat', color: 'brown', bought: false}
	];

function createPetstore() {
	// this custom store extends the writable store, so we extract the features of the writable store we want to use
	// anything that implement 'subscribe' correctly is a store
	// 'set' will allow you to set the value of the store in the component using $<store_name> = <value>.
	const { subscribe, set, update } = writable(pets);	
	return {
		subscribe, // forgetting to include this will throw an error that it isn't a store
		set, // probably should't include this
		brownAnimals: () => pets.filter(pet => pet.color === 'brown'),
		// on:click={()=>petStore.buy(index)}
		buy: (index) => update(pets => {
			pets[index].bought = true;
			return pets;
		}),
		// on:click={()=>petStore.reset()}
		reset: () => update(pets => {
			return pets.map(pet => ({...pet, bought: false}))
		})		
	};	
}
export const petStore = createPetstore();