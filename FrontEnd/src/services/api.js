import axios from 'axios'
import router from '@/routers'

const baseURL = process.env.VUE_APP_API_BASE_URL 
  ? `${process.env.VUE_APP_API_BASE_URL}/`
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

// ✅ AGREGAR: Interceptor para manejar tokens expirados
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    if (error.response?.status === 401) {
      // Token expirado - limpiar y redirigir
      localStorage.removeItem('access_token')
      localStorage.removeItem('refresh_token')
      localStorage.removeItem('user')
      router.push('/')
    }
    return Promise.reject(error)
  }
)

export default api