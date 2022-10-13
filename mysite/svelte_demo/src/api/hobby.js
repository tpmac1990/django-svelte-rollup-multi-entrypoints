import Api from "../Api"; // Implementations for all the calls.

// Get list of clubs from django view
export const getHobbies = async (csrfToken) => {
    try {
      const response = await Api.get("/svelte-demo/hobbies", csrfToken);
      return response;
    } catch (error) {
      console.error(error);
    }
};