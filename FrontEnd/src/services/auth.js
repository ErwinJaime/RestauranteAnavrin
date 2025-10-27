// frontend/src/services/auth.js
import api from './api'

export function login(correo, password) {
  return api.post('login/', { correo, password })
}

export function registro(nombre, correo, password, password2) {
  return api.post('registro/', { 
    nombre, 
    correo, 
    password,
    password2  // ⚠️ AGREGAR esto - el backend ahora lo requiere
  })
}

export function googleLogin(googleToken) {
  return api.post('google-login/', { token: googleToken })
}

// ✅ NUEVAS funciones útiles
export function obtenerPerfil() {
  return api.get('perfil/')
}

export function actualizarPerfil(data) {
  return api.put('perfil/actualizar/', data)
}