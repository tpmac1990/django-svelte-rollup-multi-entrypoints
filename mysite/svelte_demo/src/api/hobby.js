import Api from "../Api"; // Implementations for all the calls.

// Get list of clubs from django view
export const getInitialHobbies = async (csrfToken) => {
    try {
      const response = await Api.get("/svelte-demo/hobbies/", csrfToken);
      return response;
    } catch (error) {
      console.error(error);
    }
};

export const postHobby = async (csrfToken, data) => {
  try {
    const response = await Api.post("/svelte-demo/hobbies/", csrfToken, data);
    return response;
  } catch (error) {
    console.error(error);
  }
};

export const deleteHobby = async (csrfToken, id) => {
  try {
    const response = await Api.delete(`/svelte-demo/hobbies/${id}/`, csrfToken);
    return response;
  } catch (error) {
    console.error(error);
  }
};

