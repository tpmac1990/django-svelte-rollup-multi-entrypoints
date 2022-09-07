// pokemon.js
// Implementations for all the calls for the pokemon endpoints.
import Api from "../../svelte/api/Api";

// Method to get a list of all Pokemon
export const getTodoList = async (csrfToken) => {
    try {
      const response = await Api.get("/todo", csrfToken);
      return response.html;
    } catch (error) {
      console.error(error);
    }
};

// // Get a pokemon details by name
// export const getTodoByName = async(name) => {
//     try {
//       const response = await Api.get(`/pokemon/${name}`);
//       return response;
//     } catch (error) {
//       console.error(error);
//     }
// };