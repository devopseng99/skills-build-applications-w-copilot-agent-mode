export const API_CONFIG = {
    BASE_URL: 'https://congenial-space-happiness-4pxppj9gg37rr9-8000.app.github.dev/',
    VERSION: 'v1'
};

export const getApiUrl = (endpoint) => `${API_CONFIG.BASE_URL}api/${API_CONFIG.VERSION}/${endpoint}/`;