// frontend/src/services/api.js
import axios from 'axios'
import router from '@/routers'

const baseURL = process.env.VUE_APP_API_BASE_URL 
  ? `${process.env.VUE_APP_API_BASE_URL}/`
  : 'http://127.0.0.1:8000/api/usuarios/'

const api = axios.create({
  baseURL: baseURL,
  timeout: 10000 // 10 segundos timeout
})

// Interceptor de requests - agregar token
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('access_token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

// Interceptor de responses - manejar errores de autenticación
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config

    // Token expirado o no autorizado
    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true
      
      // Intentar refrescar el token
      const refreshToken = localStorage.getItem('refresh_token')
      
      if (refreshToken) {
        try {
          const response = await axios.post(`${baseURL}token/refresh/`, {
            refresh: refreshToken
          })
          
          const newAccessToken = response.data.access
          localStorage.setItem('access_token', newAccessToken)
          
          // Reintentar la petición original con el nuevo token
          originalRequest.headers.Authorization = `Bearer ${newAccessToken}`
          return api(originalRequest)
        } catch (refreshError) {
          // Si el refresh falla, limpiar y redirigir
          console.error('Error al refrescar token:', refreshError)
          localStorage.removeItem('access_token')
          localStorage.removeItem('refresh_token')
          localStorage.removeItem('user')
          router.push('/')
          return Promise.reject(refreshError)
        }
      } else {
        // No hay refresh token, limpiar y redirigir
        localStorage.removeItem('access_token')
        localStorage.removeItem('refresh_token')
        localStorage.removeItem('user')
        router.push('/')
      }
    }
    
    return Promise.reject(error)
  }
)

export default api