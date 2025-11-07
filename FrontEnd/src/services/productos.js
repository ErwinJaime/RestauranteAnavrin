// frontend/src/services/productos.js
import api from './api'

// ========== PRODUCTOS ==========

// Listar todos los productos (público)
export function listarProductos(params = {}) {
  return api.get('productos/', { params })
}

// Obtener un producto específico
export function obtenerProducto(id) {
  return api.get(`productos/${id}/`)
}

// Crear nuevo producto (solo admin)
export function crearProducto(data) {
  // Si hay imagen, usar FormData
  if (data.imagen instanceof File) {
    const formData = new FormData()
    formData.append('nombre', data.nombre)
    formData.append('ingredientes', data.ingredientes)
    formData.append('precio', data.precio)
    formData.append('categoria', data.categoria)
    formData.append('disponible', data.disponible)
    formData.append('imagen', data.imagen)
    
    return api.post('productos/crear/', formData, {
      headers: { 'Content-Type': 'multipart/form-data' }
    })
  }
  
  return api.post('productos/crear/', data)
}

// Actualizar producto (solo admin)
export function actualizarProducto(id, data) {
  // Si hay imagen nueva, usar FormData
  if (data.imagen instanceof File) {
    const formData = new FormData()
    formData.append('nombre', data.nombre)
    formData.append('ingredientes', data.ingredientes)
    formData.append('precio', data.precio)
    formData.append('categoria', data.categoria)
    formData.append('disponible', data.disponible)
    formData.append('imagen', data.imagen)
    
    return api.put(`productos/${id}/actualizar/`, formData, {
      headers: { 'Content-Type': 'multipart/form-data' }
    })
  }
  
  return api.put(`productos/${id}/actualizar/`, data)
}

// Eliminar producto (solo admin)
export function eliminarProducto(id) {
  return api.delete(`productos/${id}/eliminar/`)
}

// ========== PEDIDOS ==========

// Listar mis pedidos
export function listarMisPedidos(params = {}) {
  return api.get('pedidos/', { params })
}

// Listar todos los pedidos (solo admin)
export function listarTodosPedidos(params = {}) {
  return api.get('pedidos/todos/', { params })
}

// Obtener un pedido específico
export function obtenerPedido(id) {
  return api.get(`pedidos/${id}/`)
}

// Crear nuevo pedido
export function crearPedido(data) {
  return api.post('pedidos/crear/', data)
}

// Actualizar pedido (cantidad y dirección)
export function actualizarPedido(id, data) {
  return api.put(`pedidos/${id}/actualizar/`, data)
}

// Cambiar estado del pedido (solo admin)
export function cambiarEstadoPedido(id, estado) {
  return api.patch(`pedidos/${id}/estado/`, { estado })
}

// Cancelar pedido
export function cancelarPedido(id) {
  return api.delete(`pedidos/${id}/cancelar/`)
}

// ========== RESEÑAS ==========

// Listar reseñas de un producto (público)
export function listarResenasProducto(productoId) {
  return api.get(`productos/${productoId}/resenas/`)
}

// Listar mis reseñas
export function listarMisResenas() {
  return api.get('resenas/')
}

// Listar todas las reseñas (solo admin)
export function listarTodasResenas(params = {}) {
  return api.get('resenas/todas/', { params })
}

// Crear nueva reseña
export function crearResena(data) {
  return api.post('resenas/crear/', data)
}

// Actualizar reseña
export function actualizarResena(id, data) {
  return api.put(`resenas/${id}/actualizar/`, data)
}

// Eliminar reseña
export function eliminarResena(id) {
  return api.delete(`resenas/${id}/eliminar/`)
}

// Cambiar visibilidad de reseña (solo admin)
export function cambiarVisibilidadResena(id, visible) {
  return api.patch(`resenas/${id}/visibilidad/`, { visible })
}