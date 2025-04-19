const BASE_API_URL = import.meta.env.VITE_BASE_API_URL;

export const getApiUrl = (endpoint) => {
    return `${BASE_API_URL}${endpoint}/`;
};