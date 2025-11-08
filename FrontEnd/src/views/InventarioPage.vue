<template>
  <div class="inventario-container">
    <!-- Navegación -->
    <nav class="navbar">
      <h1 class="logo">ANAVRIN</h1>
      <div class="nav-links">
        <a href="#">Home</a>
        <router-link to="/about">About</router-link>
        <router-link to="/resenasadmin">Review</router-link>
      </div>
      <span class="btn-admin">Admin</span>
      <button class="btn-cerrar-sesion">Cerrar Sesión</button>
    </nav>

    <!-- Contenido Principal -->
    <div class="main-content">
      <h1 class="title">Inventario</h1>

      <!-- Barra de acciones -->
      <div class="actions-bar">
        <!-- Botón Agregar Nuevo Plato -->
        <button class="btn-agregar" @click="abrirModal">
          + Agregar Nuevo Plato
        </button>

        <!-- Buscador -->
        <div class="search-container">
          <svg class="search-icon" width="20" height="20" viewBox="0 0 24 24" fill="none">
            <path d="M21 21L15 15M17 10C17 13.866 13.866 17 10 17C6.13401 17 3 13.866 3 10C3 6.13401 6.13401 3 10 3C13.866 3 17 6.13401 17 10Z" stroke="#999" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
          <input 
            type="text" 
            placeholder="Buscar plato..." 
            class="search-input"
            v-model="searchQuery"
          >
        </div>
      </div>

      <!-- Tabla de productos -->
      <div class="table-container">
        <div v-if="cargando" class="loader"></div>
        <p v-else-if="productosFiltrados.length === 0" class="empty-message">
          {{ searchQuery ? 'No se encontraron productos' : 'Gestiona todos tus productos' }}
        </p>
        <div v-else class="table-wrapper">
          <table class="productos-table">
            <thead>
              <tr>
                <th>Imagen</th>
                <th>Nombre</th>
                <th>Descripción</th>
                <th>Precio</th>
                <th>Disponibilidad</th>
                <th>Opciones</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="producto in productosFiltrados" :key="producto.id">
                <td>
                  <div class="img-container">
                    <img 
                      :src="obtenerUrlImagen(producto.imagen)" 
                      :alt="producto.nombre"
                      class="producto-img"
                      @error="onImageError"
                    >
                  </div>
                </td>
                <td class="producto-nombre">{{ producto.nombre }}</td>
                <td class="producto-descripcion">{{ producto.ingredientes }}</td>
                <td class="producto-precio">${{ formatearPrecio(producto.precio) }}</td>
                <td>
                  <span :class="['badge-disponibilidad', producto.disponible ? 'disponible' : 'no-disponible']">
                    {{ producto.disponible ? 'Sí' : 'No' }}
                  </span>
                </td>
                <td class="td-opciones">
                  <button class="btn-editar" @click="editarProducto(producto.id)">
                    Editar
                  </button>
                  <button class="btn-eliminar" @click="eliminarProducto(producto.id)">
                    Eliminar
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Hojas decorativas -->
    <img src="@/assets/hoja3.png" alt="Hoja" class="hoja-below">
    <img src="@/assets/hoja2.png" alt="Hoja" class="hoja-bottom">
  
    <!-- Imagen Grapefruit superior izquierda -->
    <img src="@/assets/grapefruit.png" alt="Grapefruit" class="img-grapefruit">

    <!-- Imagen mortero derecha -->
    <img src="@/assets/mortero.png" alt="Mortero" class="img-mortero">

    <AgregarProducto
      :isOpen="mostrarModal"
      @cerrar="cerrarModal"
      @guardar="guardarProducto"
    />
  </div>
</template>

<script>
import { ref, onMounted, computed } from 'vue'
import { listarProductos, crearProducto, eliminarProducto as eliminarProductoAPI } from '@/services/productos'
import AgregarProducto from './AgregarProducto.vue' 

export default {
  name: 'InventarioPage',
  components: {
    AgregarProducto
  },
  setup() {
    const searchQuery = ref('')
    const mostrarModal = ref(false)
    const productos = ref([])
    const cargando = ref(false)

    // Productos filtrados según búsqueda
    const productosFiltrados = computed(() => {
      if (!searchQuery.value) {
        return productos.value
      }
      const query = searchQuery.value.toLowerCase()
      return productos.value.filter(p => 
        p.nombre.toLowerCase().includes(query) ||
        p.ingredientes.toLowerCase().includes(query)
      )
    })

    // Cargar productos al montar el componente
    onMounted(() => {
      cargarProductos()
    })

    const cargarProductos = async () => {
      try {
        cargando.value = true
        const response = await listarProductos()
        productos.value = response.data
        console.log('✅ Productos cargados:', productos.value)
      } catch (error) {
        console.error('❌ Error al cargar productos:', error)
        if (error.response) {
          console.error('Respuesta del servidor:', error.response.data)
        }
        alert('Error al cargar los productos. Verifica que el backend esté corriendo.')
      } finally {
        cargando.value = false
      }
    }

    const abrirModal = () => {
      mostrarModal.value = true
    }

    const cerrarModal = () => {
      mostrarModal.value = false
    }

    const guardarProducto = async (producto) => {
      try {
        cargando.value = true
        console.log('📦 Guardando producto:', producto)
        
        const response = await crearProducto(producto)
        
        console.log('✅ Producto guardado:', response.data)
        
        cerrarModal()
        alert('¡Producto agregado exitosamente!')
        
        // Recargar la lista completa
        await cargarProductos()
      } catch (error) {
        console.error('❌ Error al guardar producto:', error)
        
        // Mensaje de error más detallado
        if (error.response) {
          console.error('Respuesta del servidor:', error.response.data)
          const errorMsg = error.response.data.error || error.response.data.message || JSON.stringify(error.response.data)
          alert(`Error: ${errorMsg}`)
        } else if (error.request) {
          alert('Error de conexión. Verifica que el backend esté corriendo en http://127.0.0.1:8000')
        } else {
          alert('Error al guardar el producto')
        }
      } finally {
        cargando.value = false
      }
    }

    const editarProducto = async (id) => {
      console.log('✏️ Editar producto:', id)
      alert('Función de editar en desarrollo')
    }

    const eliminarProducto = async (id) => {
      if (!confirm('¿Estás seguro de eliminar este producto?')) {
        return
      }

      try {
        cargando.value = true
        await eliminarProductoAPI(id)
        
        // Eliminar de la lista local
        productos.value = productos.value.filter(p => p.id !== id)
        
        alert('✅ Producto eliminado exitosamente')
      } catch (error) {
        console.error('❌ Error al eliminar producto:', error)
        alert('Error al eliminar el producto')
      } finally {
        cargando.value = false
      }
    }

    // Formatear precio en pesos colombianos
    const formatearPrecio = (precio) => {
      return new Intl.NumberFormat('es-CO').format(precio)
    }

    // Obtener URL de imagen
    const obtenerUrlImagen = (imagenUrl) => {
      if (!imagenUrl) {
        return 'https://via.placeholder.com/100x100?text=Sin+Imagen'
      }
      
      // Si ya es una URL completa, devolverla
      if (imagenUrl.startsWith('http://') || imagenUrl.startsWith('https://')) {
        return imagenUrl
      }
      
      // Si es una ruta relativa, agregar la base del backend
      return `http://127.0.0.1:8000${imagenUrl}`
    }

    // Manejo de error de imagen
    const onImageError = (event) => {
      event.target.src = 'https://via.placeholder.com/100x100?text=Error'
    }

    return {
      searchQuery,
      mostrarModal,
      productos,
      productosFiltrados,
      cargando,
      abrirModal,
      cerrarModal,
      guardarProducto,
      editarProducto,
      eliminarProducto,
      formatearPrecio,
      obtenerUrlImagen,
      onImageError
    }
  }
}
</script>

<style scoped>
/* General */
.inventario-container {
  width: 100%;
  min-height: 100vh;
  background-color: #ffffff;
  position: relative;
  overflow-x: hidden;
}

/* Navegación */
.navbar {
  position: fixed !important;
  top: 0;
  left: 0;
  right: 0;
  z-index: 50;
  background-color: #ffffff;
  padding: 20px 3% !important;
  display: flex !important;
  flex-direction: row !important;
  align-items: center !important;
  justify-content: space-between !important;
  gap: 15px !important;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}

.logo {
  font-size: 20px;
  font-weight: 600;
  color: #1a1a1a;
  letter-spacing: 1px;
  margin-left: 30px;
  flex-shrink: 0;
}

.nav-links {
  display: flex !important;
  gap: 60px;
  align-items: center;
  flex: 1;
  justify-content: center;
  margin-left: 100px;
}

.nav-links a {
  font-size: 14px;
  color: #666;
  text-decoration: none;
  transition: color 0.3s ease;
  white-space: nowrap;
}

.nav-links a:hover {
  color: #6d9fef;
}

.btn-admin {
  padding: 8px 28px;
  font-size: 14px;
  color: #000;
  background-color: #ff6b35;
  border: none;
  border-radius: 50px;
  cursor: default;
  font-weight: 580;
  white-space: nowrap;
  flex-shrink: 0;
  margin-left: auto !important;
  margin-right: 10px !important;
}

.btn-cerrar-sesion {
  padding: 8px 22px;
  font-size: 14px;
  color: #070707;
  border: 2px solid #ddd;
  background-color: transparent;
  border-radius: 50px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 600;
  white-space: nowrap;
  flex-shrink: 0;
}

.btn-cerrar-sesion:hover {
  background-color: #6d9fef;
  color: rgb(21, 3, 3);
}

/* Imágenes decorativas */
.img-grapefruit {
  position: fixed;
  top: 70px;
  left: -70px;
  width: 180px;
  height: 180px;
  object-fit: contain;
  z-index: 5;
  pointer-events: none;
}

.hoja-below {
  position: fixed;
  top: 450px;
  right: 40px;
  width: 90px;
  height: 90px;
  object-fit: contain;
  z-index: 5;
}

.hoja-bottom {
  position: fixed;
  bottom: 140px;
  left: 70px;
  width: 80px;
  height: 80px;
  object-fit: contain;
  z-index: 5;
}

.img-mortero {
  position: fixed;
  bottom: 40px;
  top: 140px;
  right: -65px;
  width: 230px;
  height: 230px;
  object-fit: contain;
  z-index: 5;
}

/* Contenido Principal */
.main-content {
  max-width: 900px;
  margin: 0 auto;
  padding-top: 140px;
  padding-bottom: 60px;
  text-align: center;
}

.title {
  font-size: 45px;
  font-weight: 800;
  color: #28233b;
  margin-bottom: 30px;
  margin-top: -35px;
  font-family: 'Open Sans', sans-serif;
}

/* Barra de acciones */
.actions-bar {
  display: flex;
  align-items: center;
  justify-content: center; 
  gap: 20px;
  margin-bottom: 40px;
  max-width: 900px;
  margin-left: auto;
  margin-right: auto;
  margin-top: -20px;
  padding: 0 20px;
}

.btn-agregar {
  padding: 10px 32px;
  font-size: 12px;
  color: white;
  background-color: #7cb342;
  border: none;
  border-radius: 50px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 600;
  white-space: nowrap;
}

.btn-agregar:hover {
  background-color: #6a9f38;
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(124, 179, 66, 0.3);
}

/* Buscador */
.search-container {
  position: relative;
  flex: 1;
  max-width: 400px;
}

.search-icon {
  position: absolute;
  left: 20px;
  top: 50%;
  transform: translateY(-50%);
  z-index: 1;
}

.search-input {
  width: 100%;
  padding: 8px 20px 10px 50px;
  border: 2px solid #e5e5e5;
  border-radius: 50px;
  font-size: 13px;
  font-family: 'Montserrat', sans-serif;
  transition: border-color 0.3s ease;
  background-color: white;
}

.search-input:focus {
  outline: none;
  border-color: #7cb342;
}

.search-input::placeholder {
  color: #999;
}

/* Tabla de productos */
.table-container {
  background-color: rgb(253, 252, 252);
  border-radius: 16px;
  padding: 30px 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  min-height: 290px;
  margin-top: -30px;
  margin: 0 20px;
}

.table-wrapper {
  width: 100%;
  overflow-x: auto;
}

.productos-table {
  width: 100%;
  border-collapse: collapse;
  font-family: 'Montserrat', sans-serif;
}

.productos-table thead {
  background-color: #e8d7a8;
}

.productos-table th {
  padding: 14px 12px;
  text-align: left;
  font-weight: 600;
  font-size: 13px;
  color: #333;
  border-bottom: 2px solid #ddd;
}

.productos-table tbody tr {
  border-bottom: 1px solid #eee;
  transition: background-color 0.2s ease;
}

.productos-table tbody tr:hover {
  background-color: #f9f9f9;
}

.productos-table td {
  padding: 16px 12px;
  font-size: 13px;
  color: #555;
  vertical-align: middle;
}

/* Columna de imagen */
.img-container {
  width: 80px;
  height: 80px;
  border-radius: 8px;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #f5f5f5;
}

.producto-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* Columna de nombre */
.producto-nombre {
  font-weight: 600;
  color: #333;
  font-size: 14px;
}

/* Columna de descripción */
.producto-descripcion {
  max-width: 200px;
  font-size: 12px;
  color: #666;
  line-height: 1.4;
}

/* Columna de precio */
.producto-precio {
  font-weight: 600;
  color: #7cb342;
  font-size: 14px;
}

/* Badge de disponibilidad */
.badge-disponibilidad {
  padding: 5px 14px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
  display: inline-block;
}

.badge-disponibilidad.disponible {
  background-color: #d4edda;
  color: #155724;
}

.badge-disponibilidad.no-disponible {
  background-color: #f8d7da;
  color: #721c24;
}

/* Botones de opciones */
.td-opciones {
  display: flex;
  gap: 8px;
  align-items: center;
}

.btn-editar,
.btn-eliminar {
  padding: 7px 16px;
  border: none;
  border-radius: 6px;
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.btn-editar {
  background-color: #ff9f43;
  color: white;
}

.btn-editar:hover {
  background-color: #ff8800;
  transform: translateY(-1px);
  box-shadow: 0 2px 6px rgba(255, 159, 67, 0.3);
}

.btn-eliminar {
  background-color: #ee5a6f;
  color: white;
}

.btn-eliminar:hover {
  background-color: #d63447;
  transform: translateY(-1px);
  box-shadow: 0 2px 6px rgba(238, 90, 111, 0.3);
}

/* Loader */
.loader {
  border: 4px solid #f3f3f3;
  border-top: 4px solid #7cb342;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  animation: spin 1s linear infinite;
  margin: 60px auto;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.empty-message {
  color: #8b8585b0;
  font-size: 16px;
  font-weight: 500;
  font-family: 'Montserrat', sans-serif;
  padding: 60px 20px;
}

/* RESPONSIVE DESIGN */
@media (max-width: 1023px) {
  .main-content {
    max-width: 100%;
    padding: 130px 20px 50px;
  }

  .table-container {
    margin: 0 10px;
  }

  .productos-table th,
  .productos-table td {
    padding: 10px 8px;
    font-size: 12px;
  }

  .img-container {
    width: 60px;
    height: 60px;
  }
}

@media (max-width: 767px) {
  .navbar {
    padding: 15px 20px !important;
    flex-wrap: wrap !important;
    gap: 15px !important;
    justify-content: center !important;
  }

  .logo {
    font-size: 18px;
    width: 100%;
    text-align: center;
    margin: 0 0 10px 0;
  }

  .nav-links {
    gap: 30px;
    width: 100%;
    justify-content: center;
    margin-left: 0;
  }

  .btn-admin {
    margin-left: 0 !important;
    margin-right: 5px !important;
  }

  .img-grapefruit,
  .hoja-below,
  .hoja-bottom,
  .img-mortero {
    display: none;
  }

  .main-content {
    padding: 160px 15px 40px;
  }

  .title {
    font-size: 32px;
  }

  .actions-bar {
    flex-direction: column;
    gap: 15px;
    padding: 0 10px;
  }

  .btn-agregar {
    width: 100%;
  }

  .search-container {
    max-width: 100%;
  }

  .table-container {
    padding: 20px 10px;
    margin: 0 10px;
  }

  .productos-table {
    font-size: 11px;
  }

  .productos-table th,
  .productos-table td {
    padding: 8px 6px;
  }

  .img-container {
    width: 50px;
    height: 50px;
  }

  .producto-descripcion {
    max-width: 120px;
    font-size: 11px;
  }

  .td-opciones {
    flex-direction: column;
    gap: 5px;
  }

  .btn-editar,
  .btn-eliminar {
    padding: 6px 12px;
    font-size: 11px;
    width: 100%;
  }
}
</style>