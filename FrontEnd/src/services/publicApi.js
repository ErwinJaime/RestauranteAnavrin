// services/publicAPI.js
import axios from 'axios'

// Detectar entorno y usar la baseURL correcta
const baseURL = process.env.VUE_APP_API_BASE_URL || 'http://127.0.0.1:8000/api/usuarios/'

console.log('🌍 BaseURL usada en publicAPI:', baseURL)

const publicAPI = axios.create({
  baseURL,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json'
  }
})

// NO tiene interceptor de token - completamente público

// ========== ENDPOINTS PÚBLICOS ==========

// PRODUCTOS (públicos)
export function listarProductosPublicos(params = {}) {
  return publicAPI.get('productos/', { params })
}

export function obtenerProductoPublico(id) {
  return publicAPI.get(`productos/${id}/`)
}

// RESEÑAS (públicas)
export function listarResenasProductoPublico(productoId) {
  return publicAPI.get(`productos/${productoId}/resenas/`)
}
export function listarResenasPublicas() {
  return publicAPI.get('resenas/publicas/')
}

// AUTENTICACIÓN (públicas)
export function registroUsuario(data) {
  return publicAPI.post('registro/', data)
}

export function loginUsuario(data) {
  return publicAPI.post('login/', data)
}

export function googleLogin(data) {
  return publicAPI.post('google-login/', data)
}