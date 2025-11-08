import axios from 'axios'
import router from '@/routers'

// Lee automáticamente la variable según el entorno (.env o .env.production)
const baseURL = process.env.VUE_APP_API_BASE_URL

const api = axios.create({
  baseURL: baseURL,
  timeout: 10000
})

// Interceptor de requests - agrega token
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('access_token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error) => Promise.reject(error)
)

// Interceptor de responses - manejar errores de autenticación
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config

    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true
      const refreshToken = localStorage.getItem('refresh_token')

      if (refreshToken) {
        try {
          const response = await axios.post(`${baseURL}token/refresh/`, {
            refresh: refreshToken
          })

          const newAccessToken = response.data.access
          localStorage.setItem('access_token', newAccessToken)

          originalRequest.headers.Authorization = `Bearer ${newAccessToken}`
          return api(originalRequest)
        } catch (refreshError) {
          localStorage.clear()
          router.push('/')
          return Promise.reject(refreshError)
        }
      } else {
        localStorage.clear()
        router.push('/')
      }
    }

    return Promise.reject(error)
  }
)

export default api
