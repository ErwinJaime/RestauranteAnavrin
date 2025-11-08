// frontend/src/services/productos.js
import axios from 'axios'

const productosAPI = axios.create({
  baseURL: 'http://127.0.0.1:8000/api/usuarios/',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json'
  }
})

// Interceptor para agregar el token automáticamente
productosAPI.interceptors.request.use(
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

// ========== FUNCIÓN AUXILIAR ==========
// Convierte valores a string si son arrays
function cleanValue(value) {
  if (Array.isArray(value)) {
    return value[0] || ''
  }
  return value
}

// ========== PRODUCTOS ==========

export function listarProductos(params = {}) {
  return productosAPI.get('productos/', { params })
}

export function obtenerProducto(id) {
  return productosAPI.get(`productos/${id}/`)
}

export function crearProducto(data) {
  console.log('🔍 Data recibida en crearProducto:', data)
  
  // Limpiar datos para evitar arrays
  const cleanData = {
    nombre: cleanValue(data.nombre) || '',
    ingredientes: cleanValue(data.ingredientes) || '',
    precio: cleanValue(data.precio) || '0',
    categoria: cleanValue(data.categoria) || '',
    disponible: data.disponible,
    imagen: data.imagen
  }
  
  console.log('✨ Data limpia:', cleanData)
  
  // Si hay imagen, usar FormData
  if (cleanData.imagen instanceof File) {
    const formData = new FormData()
    
    // Asegurar que cada campo se agrega solo UNA vez
    formData.append('nombre', String(cleanData.nombre))
    formData.append('ingredientes', String(cleanData.ingredientes))
    formData.append('precio', String(cleanData.precio))
    formData.append('categoria', String(cleanData.categoria).toLowerCase())
    formData.append('disponible', cleanData.disponible ? 'true' : 'false')
    formData.append('imagen', cleanData.imagen)
    
    console.log('📤 Enviando FormData con imagen')
    console.log('📋 Campos FormData:')
    for (let pair of formData.entries()) {
      console.log(`  ${pair[0]}:`, pair[1])
    }
    
    return productosAPI.post('productos/crear/', formData, {
      headers: { 
        'Content-Type': 'multipart/form-data'
      }
    })
  }
  
  // Sin imagen, enviar JSON normal
  const jsonData = {
    nombre: String(cleanData.nombre),
    ingredientes: String(cleanData.ingredientes),
    precio: parseFloat(cleanData.precio) || 0,
    categoria: String(cleanData.categoria).toLowerCase(),
    disponible: Boolean(cleanData.disponible)
  }
  
  console.log('📤 Enviando JSON (sin imagen):', jsonData)
  return productosAPI.post('productos/crear/', jsonData)
}

export function actualizarProducto(id, data) {
  // Limpiar datos
  const cleanData = {
    nombre: cleanValue(data.nombre) || '',
    ingredientes: cleanValue(data.ingredientes) || '',
    precio: cleanValue(data.precio) || '0',
    categoria: cleanValue(data.categoria) || '',
    disponible: data.disponible,
    imagen: data.imagen
  }
  
  if (cleanData.imagen instanceof File) {
    const formData = new FormData()
    formData.append('nombre', String(cleanData.nombre))
    formData.append('ingredientes', String(cleanData.ingredientes))
    formData.append('precio', String(cleanData.precio))
    formData.append('categoria', String(cleanData.categoria).toLowerCase())
    formData.append('disponible', cleanData.disponible ? 'true' : 'false')
    formData.append('imagen', cleanData.imagen)
    
    return productosAPI.put(`productos/${id}/actualizar/`, formData, {
      headers: { 'Content-Type': 'multipart/form-data' }
    })
  }
  
  const jsonData = {
    nombre: String(cleanData.nombre),
    ingredientes: String(cleanData.ingredientes),
    precio: parseFloat(cleanData.precio) || 0,
    categoria: String(cleanData.categoria).toLowerCase(),
    disponible: Boolean(cleanData.disponible)
  }
  
  return productosAPI.put(`productos/${id}/actualizar/`, jsonData)
}

export function eliminarProducto(id) {
  return productosAPI.delete(`productos/${id}/eliminar/`)
}

// ========== PEDIDOS ==========

export function listarMisPedidos(params = {}) {
  return productosAPI.get('pedidos/', { params })
}

export function listarTodosPedidos(params = {}) {
  return productosAPI.get('pedidos/todos/', { params })
}

export function obtenerPedido(id) {
  return productosAPI.get(`pedidos/${id}/`)
}

export function crearPedido(data) {
  return productosAPI.post('pedidos/crear/', data)
}

export function actualizarPedido(id, data) {
  return productosAPI.put(`pedidos/${id}/actualizar/`, data)
}

export function cambiarEstadoPedido(id, estado) {
  return productosAPI.patch(`pedidos/${id}/estado/`, { estado })
}

export function cancelarPedido(id) {
  return productosAPI.delete(`pedidos/${id}/cancelar/`)
}

// ========== RESEÑAS ==========

export function listarResenasProducto(productoId) {
  return productosAPI.get(`productos/${productoId}/resenas/`)
}

export function listarMisResenas() {
  return productosAPI.get('resenas/')
}

export function listarTodasResenas(params = {}) {
  return productosAPI.get('resenas/todas/', { params })
}

export function crearResena(data) {
  return productosAPI.post('resenas/crear/', data)
}

export function actualizarResena(id, data) {
  return productosAPI.put(`resenas/${id}/actualizar/`, data)
}

export function eliminarResena(id) {
  return productosAPI.delete(`resenas/${id}/eliminar/`)
}

export function cambiarVisibilidadResena(id, visible) {
  return productosAPI.patch(`resenas/${id}/visibilidad/`, { visible })
}