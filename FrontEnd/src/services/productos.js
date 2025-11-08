// frontend/src/services/productos.js
import api from './api'

// ========== PRODUCTOS ==========

/**
 * Listar todos los productos
 */
export function listarProductos(params = {}) {
  return api.get('productos/', { params })
}

/**
 * Obtener un producto específico por ID
 */
export function obtenerProducto(id) {
  return api.get(`productos/${id}/`)
}

/**
 * Crear nuevo producto (solo admin)
 * IMPORTANTE: Categorías válidas deben coincidir con el backend
 */
export function crearProducto(data) {
  // Si hay imagen, usar FormData
  if (data.imagen instanceof File) {
    const formData = new FormData()
    
    // Agregar campos uno por uno
    formData.append('nombre', data.nombre || '')
    formData.append('ingredientes', data.ingredientes || '')
    formData.append('precio', data.precio?.toString() || '0')
    
    // CRÍTICO: Enviar categoría en minúsculas
    formData.append('categoria', (data.categoria || '').toLowerCase())
    
    formData.append('disponible', data.disponible ? 'true' : 'false')
    formData.append('imagen', data.imagen)
    
    console.log('📤 Enviando FormData con imagen')
    
    return api.post('productos/crear/', formData, {
      headers: { 
        'Content-Type': 'multipart/form-data'
      }
    })
  }
  
  // Sin imagen, enviar JSON normal
  const jsonData = {
    nombre: data.nombre || '',
    ingredientes: data.ingredientes || '',
    precio: parseFloat(data.precio) || 0,
    // CRÍTICO: Categoría en minúsculas
    categoria: (data.categoria || '').toLowerCase(),
    disponible: Boolean(data.disponible)
  }
  
  console.log('📤 Enviando JSON (sin imagen):', jsonData)
  return api.post('productos/crear/', jsonData)
}

/**
 * Actualizar producto existente (solo admin)
 */
export function actualizarProducto(id, data) {
  if (data.imagen instanceof File) {
    const formData = new FormData()
    formData.append('nombre', data.nombre)
    formData.append('ingredientes', data.ingredientes)
    formData.append('precio', data.precio.toString())
    formData.append('categoria', (data.categoria || '').toLowerCase())
    formData.append('disponible', data.disponible ? 'true' : 'false')
    formData.append('imagen', data.imagen)
    
    return api.put(`productos/${id}/actualizar/`, formData, {
      headers: { 'Content-Type': 'multipart/form-data' }
    })
  }
  
  // Asegurar categoría en minúsculas también en JSON
  const jsonData = {
    ...data,
    categoria: (data.categoria || '').toLowerCase()
  }
  
  return api.put(`productos/${id}/actualizar/`, jsonData)
}

/**
 * Eliminar producto (solo admin)
 */
export function eliminarProducto(id) {
  return api.delete(`productos/${id}/eliminar/`)
}

// ========== PEDIDOS ==========

export function listarMisPedidos(params = {}) {
  return api.get('pedidos/', { params })
}

export function listarTodosPedidos(params = {}) {
  return api.get('pedidos/todos/', { params })
}

export function obtenerPedido(id) {
  return api.get(`pedidos/${id}/`)
}

export function crearPedido(data) {
  return api.post('pedidos/crear/', data)
}

export function actualizarPedido(id, data) {
  return api.put(`pedidos/${id}/actualizar/`, data)
}

export function cambiarEstadoPedido(id, estado) {
  return api.patch(`pedidos/${id}/estado/`, { estado })
}

export function cancelarPedido(id) {
  return api.delete(`pedidos/${id}/cancelar/`)
}

// ========== RESEÑAS ==========

export function listarResenasProducto(productoId) {
  return api.get(`productos/${productoId}/resenas/`)
}

export function listarMisResenas() {
  return api.get('resenas/')
}

export function listarTodasResenas(params = {}) {
  return api.get('resenas/todas/', { params })
}

export function crearResena(data) {
  return api.post('resenas/crear/', data)
}

export function actualizarResena(id, data) {
  return api.put(`resenas/${id}/actualizar/`, data)
}

export function eliminarResena(id) {
  return api.delete(`resenas/${id}/eliminar/`)
}

export function cambiarVisibilidadResena(id, visible) {
  return api.patch(`resenas/${id}/visibilidad/`, { visible })
}