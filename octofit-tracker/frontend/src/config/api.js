const BASE_API_URL = import.meta.env.VITE_BASE_API_URL || '';

export const getApiUrl = (endpoint) => {
    // Ensure BASE_API_URL and endpoint are properly separated with a slash
    const baseWithTrailingSlash = BASE_API_URL.endsWith('/') 
        ? BASE_API_URL 
        : `${BASE_API_URL}/`;
    
    // Remove leading slash from endpoint if present
    const cleanEndpoint = endpoint.startsWith('/') 
        ? endpoint.substring(1) 
        : endpoint;
    
    return `${baseWithTrailingSlash}${cleanEndpoint}/`;
};