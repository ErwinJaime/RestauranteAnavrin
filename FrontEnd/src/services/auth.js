// frontend/src/services/auth.js
import api from './api'

// ========== AUTENTICACIÓN BÁSICA ==========

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

export function googleLogin(googleToken) {
  return api.post('google-login/', { token: googleToken })
}

// ========== VERIFICACIÓN 2FA ==========

export function verificarCodigo(usuarioId, codigo) {
  return api.post('verificar-codigo/', {
    usuario_id: usuarioId,
    codigo: codigo
  })
}

export function reenviarCodigo(usuarioId) {
  return api.post('reenviar-codigo/', {
    usuario_id: usuarioId
  })
}

export function verificarUsuarioExistente(correo) {
  return api.post('verificar-existente/', {
    correo: correo
  })
}

// ========== PERFIL ==========

export function obtenerPerfil() {
  return api.get('perfil/')
}

export function actualizarPerfil(data) {
  return api.put('perfil/actualizar/', data)
}