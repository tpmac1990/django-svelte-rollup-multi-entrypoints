import Api from "../Api"; // Implementations for all the calls.

// Get list of clubs from django view
export const getClubs = async (csrfToken) => {
    try {
      const response = await Api.get("/svelte-demo/clubs", csrfToken);
      return response.clubs;
    } catch (error) {
      console.error(error);
    }
};