import axios from "axios";

const api = axios.create({
    baseURL: "http://127.0.0.1:3000/api",
    headers: {
        'Content-Type': 'application/json',
    },
});

// Add interceptor to handle responses better
api.interceptors.response.use(
    (response) => {
        return response;
    },
    (error) => {
        if (error.response) {
            console.error('API Error:', error.response.data);
            console.error('Status:', error.response.status);
        } else if (error.request) {
            console.error('No response received:', error.request);
        } else {
            console.error('Request error:', error.message);
        }
        return Promise.reject(error);
    }
);

export default api;