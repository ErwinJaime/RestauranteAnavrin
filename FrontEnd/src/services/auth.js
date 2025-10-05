import api from './api';

export function login(correo, password) {
  return api.post('/login/', { correo, password })
}

export function registro(nombre, correo, password) {
  return api.post('/registro/', { nombre, correo, password })
}
