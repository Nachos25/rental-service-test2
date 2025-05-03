import axios from 'axios';

const apiClient = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000/api/v1',
  headers: {
    'Content-Type': 'application/json',
  },
});

// Interceptor для добавления токена авторизации
apiClient.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export default {
  // Квартиры
  getApartments(params = {}) {
    return apiClient.get('/apartments/', { params });
  },
  
  getApartment(slug) {
    return apiClient.get(`/apartments/${slug}/`);
  },
  
  createApartment(data) {
    return apiClient.post('/apartments/', data);
  },
  
  updateApartment(slug, data) {
    return apiClient.put(`/apartments/${slug}/`, data);
  },
  
  deleteApartment(slug) {
    return apiClient.delete(`/apartments/${slug}/`);
  },
  
  // Аутентификация
  login(credentials) {
    return apiClient.post('/users/token/', credentials);
  },
}; 