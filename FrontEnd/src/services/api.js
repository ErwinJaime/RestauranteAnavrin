import axios from 'axios'

const baseURL = process.env.VUE_APP_API_BASE_URL 
  ? `${process.env.VUE_APP_API_BASE_URL}/`  // Asegura que termine en /
  : 'http://127.0.0.1:8000/api/usuarios/'

const api = axios.create({
  baseURL: baseURL
})

api.interceptors.request.use((config) => {
  const token = localStorage.getItem('access_token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

export default api