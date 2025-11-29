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
    password2
  })
}

// ✅ NUEVAS funciones para 2FA
export function verificarCodigo(usuario_id, codigo) {
  return api.post('verificar-codigo/', { 
    usuario_id, 
    codigo 
  })
}

export function reenviarCodigo(usuario_id) {
  return api.post('reenviar-codigo/', { 
    usuario_id 
  })
}

export function googleLogin(googleToken) {
  return api.post('google-login/', { token: googleToken })
}

export function obtenerPerfil() {
  return api.get('perfil/')
}

export function actualizarPerfil(data) {
  return api.put('perfil/actualizar/', data)
}