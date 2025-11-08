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
      <button class="btn-cerrar-sesion" @click="cerrarSesion">Cerrar Sesión</button>
    </nav>

    <!-- Contenido Principal -->
    <div class="main-content">
      <h1 class="title">Inventario</h1>

      <!-- Barra de acciones -->
      <div class="actions-bar">
        <!-- Botón Agregar Nuevo Plato -->
        <button class="btn-agregar" @click="abrirModalAgregar">
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
          {{ searchQuery ? 'No se encontraron productos' : 'No hay productos en el inventario' }}
        </p>
        <div v-else class="table-wrapper">
          <table class="productos-table">
            <thead>
              <tr class="table-header">
                <th class="text-center">Imagen</th>
                <th class="text-center">Nombre</th>
                <th class="text-center">Descripción</th>
                <th class="text-center">Precio</th>
                <th class="text-center">Disponibilidad</th>
                <th class="text-center">Opciones</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="producto in productosPaginados" :key="producto.id">
                <td class="text-center">
                  <div class="img-container">
                    <img 
                      :src="producto.imagen || 'https://via.placeholder.com/100x100?text=Sin+Imagen'" 
                      :alt="producto.nombre"
                      class="producto-img"
                      @error="onImageError"
                    >
                  </div>
                </td>
                <td class="producto-nombre text-center">{{ producto.nombre || 'Sin nombre' }}</td>
                <td class="producto-descripcion text-center">{{ producto.ingredientes || 'Sin descripción' }}</td>
                <td class="producto-precio text-center">${{ formatearPrecio(producto.precio) }}</td>
                <td class="text-center">
                  <span :class="['badge-disponibilidad', producto.disponible ? 'disponible' : 'no-disponible']">
                    {{ producto.disponible ? 'Sí' : 'No' }}
                  </span>
                </td>
                <td class="td-opciones text-center">
                  <div class="opciones-container">
                    <button class="btn-editar" @click="editarProducto(producto.id)">
                      Editar
                    </button>
                    <button class="btn-eliminar" @click="confirmarEliminarProducto(producto.id)">
                      Eliminar
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
          
          <!-- PAGINACIÓN SIMPLE Y LIMPIA -->
          <div v-if="totalPaginas > 1" class="paginacion">
            <button 
              class="btn-paginacion anterior"
              @click="cambiarPagina(paginaActual - 1)" 
              :disabled="paginaActual === 1"
            >
              <span class="flecha">‹</span> Anterior
            </button>

            

            <button 
              class="btn-paginacion siguiente"
              @click="cambiarPagina(paginaActual + 1)" 
              :disabled="paginaActual === totalPaginas"
            >
              Siguiente <span class="flecha">›</span>
            </button>
          </div>
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
      :isOpen="mostrarModalAgregar"
      @cerrar="cerrarModalAgregar"
      @guardar="guardarProducto"
    />

    <!-- Modal Editar Producto -->
    <EditarProducto
      :isOpen="mostrarModalEditar"
      :producto="productoSeleccionado"
      @cerrar="cerrarModalEditar"
      @guardar="actualizarProducto"
    />

    <!-- Modal de confirmación para eliminar producto -->
    <ModalConfirmacion
      :isOpen="mostrarConfirmacionEliminar"
      titulo="¿Eliminar producto?"
      mensaje="Esta acción eliminará el producto permanentemente y no se puede deshacer."
      textoConfirmar="Eliminar"
      :cargando="cargando"
      @cerrar="cerrarConfirmacionEliminar"
      @confirmar="eliminarProducto"
    />
  </div>
</template>

<script>
import { ref, onMounted, computed, watch } from 'vue'
import { 
  listarProductos, 
  crearProducto, 
  obtenerProducto, 
  actualizarProducto as actualizarProductoAPI,
  eliminarProducto as eliminarProductoAPI 
} from '@/services/productos'
import AgregarProducto from './AgregarProducto.vue' 
import EditarProducto from './EditarProducto.vue'
import ModalConfirmacion from './ModalConfirmacion.vue'
import { useRouter } from 'vue-router'

export default {
  name: 'InventarioPage',
  components: {
    AgregarProducto,
    EditarProducto,
    ModalConfirmacion
  },
  setup() {
    const searchQuery = ref('')
    const mostrarModalAgregar = ref(false)
    const mostrarModalEditar = ref(false)
    const productoSeleccionado = ref(null)
    const productos = ref([])
    const cargando = ref(false)
    const mostrarConfirmacionEliminar = ref(false)
    const productoAEliminar = ref(null)

    const paginaActual = ref(1)
    const elementosPorPagina = ref(2)

    const router = useRouter()

    const cerrarSesion = () => {
      localStorage.removeItem('usuario')
      localStorage.removeItem('correo')
      sessionStorage.clear()
      router.push('/')
    }

    // Productos filtrados según búsqueda
    const productosFiltrados = computed(() => {
      if (!searchQuery.value) {
        return productos.value
      }
      const query = searchQuery.value.toLowerCase()
      return productos.value.filter(p => 
        (p.nombre || '').toLowerCase().includes(query) ||
        (p.ingredientes || '').toLowerCase().includes(query)
      )
    })

    // Productos paginados
    const productosPaginados = computed(() => {
      const inicio = (paginaActual.value - 1) * elementosPorPagina.value
      const fin = inicio + elementosPorPagina.value
      return productosFiltrados.value.slice(inicio, fin)
    })

    // Total de páginas
    const totalPaginas = computed(() => {
      return Math.ceil(productosFiltrados.value.length / elementosPorPagina.value)
    })

    // Cambiar de página
    const cambiarPagina = (pagina) => {
      if (pagina >= 1 && pagina <= totalPaginas.value) {
        paginaActual.value = pagina
      }
    }

    // Resetear a página 1 cuando cambia la búsqueda
    watch(searchQuery, () => {
      paginaActual.value = 1
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
        
        if (productos.value.length > 0) {
          console.log('🔍 Estructura completa del primer producto:', JSON.stringify(productos.value[0], null, 2))
        }
      } catch (error) {
        console.error('❌ Error al cargar productos:', error)
        alert('Error al cargar los productos. Verifica que el backend esté corriendo.')
      } finally {
        cargando.value = false
      }
    }

    const abrirModalAgregar = () => {
      mostrarModalAgregar.value = true
    }

    const cerrarModalAgregar = () => {
      mostrarModalAgregar.value = false
    }

    const guardarProducto = async (producto) => {
      try {
        cargando.value = true
        console.log('📦 Guardando producto:', producto)
        
        const response = await crearProducto(producto)
        console.log('✅ Producto guardado:', response.data)
        
        cerrarModalAgregar()
        await cargarProductos()
      } catch (error) {
        console.error('❌ Error al guardar producto:', error)
      } finally {
        cargando.value = false
      }
    }

    const editarProducto = async (id) => {
      try {
        cargando.value = true
        console.log('✏️ Editando producto:', id)
        
        const response = await obtenerProducto(id)
        productoSeleccionado.value = response.data
        
        console.log('📋 Producto obtenido:', productoSeleccionado.value)
        
        mostrarModalEditar.value = true
      } catch (error) {
        console.error('❌ Error al obtener producto:', error)
      } finally {
        cargando.value = false
      }
    }

    const cerrarModalEditar = () => {
      mostrarModalEditar.value = false
      productoSeleccionado.value = null
    }

    const actualizarProducto = async (productoActualizado) => {
      try {
        cargando.value = true
        console.log('🔄 Actualizando producto:', productoActualizado)
        
        const dataToSend = {
          nombre: productoActualizado.nombreProducto,
          ingredientes: productoActualizado.ingredientes,
          precio: productoActualizado.precio,
          categoria: productoActualizado.categoria,
          disponible: productoActualizado.disponible,
          imagen: productoActualizado.imagen
        }
        
        const response = await actualizarProductoAPI(productoActualizado.id, dataToSend)
        console.log('✅ Producto actualizado:', response.data)
        
        cerrarModalEditar()
        await cargarProductos()
      } catch (error) {
        console.error('❌ Error al actualizar producto:', error)
        alert('Error al actualizar el producto: ' + (error.response?.data?.message || error.message))
      } finally {
        cargando.value = false
      }
    }

    const confirmarEliminarProducto = (id) => {
      productoAEliminar.value = id
      mostrarConfirmacionEliminar.value = true
    }

    const cerrarConfirmacionEliminar = () => {
      mostrarConfirmacionEliminar.value = false
      productoAEliminar.value = null
    }

    const eliminarProducto = async () => {
      if (!productoAEliminar.value) return

      try {
        cargando.value = true
        await eliminarProductoAPI(productoAEliminar.value)
        
        productos.value = productos.value.filter(p => p.id !== productoAEliminar.value)
        
        cerrarConfirmacionEliminar()
      } catch (error) {
        console.error('❌ Error al eliminar producto:', error)
        alert('Error al eliminar el producto')
      } finally {
        cargando.value = false
      }
    }

    // Formatear precio
    const formatearPrecio = (precio) => {
      return new Intl.NumberFormat('es-CO').format(precio || 0)
    }

    // Manejo de error de imagen
    const onImageError = (event) => {
      console.error('❌ Error cargando imagen:', event.target.src)
      event.target.src = 'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAwIiBoZWlnaHQ9IjEwMCIgdmlld0JveD0iMCAwIDEwMCAxMDAiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjxyZWN0IHdpZHRoPSIxMDAiIGhlaWdodD0iMTAwIiBmaWxsPSIjRjVGNUY1Ii8+Cjx0ZXh0IHg9IjUwIiB5PSI1MCIgZm9udC1mYW1pbHk9IkFyaWFsLCBzYW5zLXNlcmlmIiBmb250LXNpemU9IjEwIiBmaWxsPSIjOTk5IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBkeT0iMC4zNWVtIj5FcnJvciBJbWFnZW48L3RleHQ+Cjwvc3ZnPg=='
    }

    return {
      searchQuery,
      mostrarModalAgregar,
      mostrarModalEditar,
      mostrarConfirmacionEliminar,
      productos,
      productoSeleccionado,
      productoAEliminar,
      productosFiltrados,
      productosPaginados,
      cargando,
      paginaActual,
      totalPaginas,
      abrirModalAgregar,
      cerrarModalAgregar,
      cerrarModalEditar,
      actualizarProducto,
      guardarProducto,
      editarProducto,
      confirmarEliminarProducto,
      cerrarConfirmacionEliminar,
      eliminarProducto,
      cambiarPagina,
      formatearPrecio,
      onImageError,
      cerrarSesion
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
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
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

.nav-links a,
.nav-links router-link {
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
  margin-right: 35px;
  margin-top: -20px;
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
  background-color: #6d9fef;
  transform: translateY(-2px);
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

/* Tabla de productos - DISEÑO UNIFICADO CON BORDES REDONDEADOS */
.table-container {
  background-color: rgb(253, 252, 252);
  border-radius: 16px;
  padding: 0;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.336);
  min-height: 290px;
  margin-top: -30px;
  overflow: hidden;
  border: 1px solid #e8d7a8;
  height: auto;
}

.table-wrapper {
  width: 100%;
  overflow-x: auto;
}

/* ALINEACIÓN CENTRADA PARA TODAS LAS CELDAS */
.text-center {
  text-align: center !important;
}

.productos-table {
  width: 100%;
  border-collapse: collapse;
  font-family: 'Montserrat', sans-serif;
  border-radius: 16px;
  overflow: hidden;
}

/* Encabezado de la tabla */
.productos-table thead {
  background-color: #e8d7a8;
}

.table-header {
  border-radius: 16px 16px 0 0;
  overflow: hidden;
}

.productos-table th {
  padding: 16px 8px;
  text-align: center !important;
  font-weight: 600;
  font-size: 14px;
  color: #000000;
  border-bottom: 2px solid #d4c18b;
}

/* Filas del cuerpo */
.table-row {
  border-bottom: 1px solid #f0f0f0;
  transition: background-color 0.2s ease;
  background-color: white;
}

.table-row:last-child {
  border-bottom: none;
}

.productos-table tbody tr:hover {
  background-color: #f9f9f9;
}

.productos-table td {
  padding: 16px 8px;
  font-size: 13px;
  color: #000000;
  vertical-align: middle;
  background-color: transparent;
  text-align: center !important;
}

/* Asegurar que la primera fila del cuerpo tenga borde superior sutil */
.productos-table tbody tr:first-child td {
  border-top: 1px solid #f0f0f0;
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
  margin: 0 auto;
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
  margin: 0 auto;
}

/* Columna de precio */
.producto-precio {
  font-weight: 600;
  color: #191b17;
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

/* Botones de opciones - UNO ENCIMA DEL OTRO */
.td-opciones {
  min-width: 120px;
}

.opciones-container {
  display: flex;
  flex-direction: column;
  gap: 8px;
  align-items: center;
  justify-content: center;
  margin: 0 auto;
}

.btn-editar,
.btn-eliminar {
  padding: 8px 16px;
  border: none;
  border-radius: 6px;
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  width: 85px;
  text-align: center;
}

.btn-editar {
  background-color: #ff9f43;
  color: white;
}

.btn-editar:hover {
  background-color: #ff8800;
  transform: translateY(-1px);
}

.btn-eliminar {
  background-color: #ee5a6f;
  color: white;
}

.btn-eliminar:hover {
  background-color: #d63447;
  transform: translateY(-1px);
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

/* PAGINACIÓN SIMPLE Y LIMPIA */
.paginacion {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 20px;
  margin-top: 30px;
  padding: 20px;
  background-color: #f9f9f9;
  border-top: 1px solid #e8d7a8;
}

.btn-paginacion {
  background: #fff;
  border: 1px solid #ddd;
  padding: 8px 16px;
  border-radius: 20px;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.2s ease;
  color: #333;
  display: flex;
  align-items: center;
  gap: 5px;
}

.btn-paginacion:hover:not(:disabled) {
  background: #f5f5f5;
  border-color: #ccc;
}

.btn-paginacion:disabled {
  color: #999;
  cursor: not-allowed;
  background: #f9f9f9;
}

.flecha {
  font-size: 16px;
  font-weight: bold;
}

.paginacion-info {
  font-weight: 500;
  color: #555;
  font-size: 14px;
}

/* ===== RESPONSIVE DESIGN ===== */

/* Pantallas grandes (1600px+) */
@media (min-width: 1600px) {
  .navbar {
    padding: 20px 5% !important;
    gap: 20px !important;
  }

  .logo {
    font-size: 22px;
    margin-right: 40px;
  }

  .nav-links {
    gap: 80px;
  }

  .nav-links a {
    font-size: 15px;
  }

  .btn-admin {
    padding: 10px 32px;
    font-size: 12px;
    margin-right: 4px !important;
  }

  .btn-cerrar-sesion {
    padding: 10px 26px;
    font-size: 12px;
  }

  .main-content {
    max-width: 1200px;
    padding: 180px 60px 60px;
  }

  .title {
    font-size: 50px;
    margin-top: 10px;
  }

  .actions-bar {
    margin-bottom: 60px;
  }

  .table-container {
    min-height: 380px;
  }

  .img-grapefruit {
    width: 160px;
    height: 160px;
    top: 100px;
    left: -70px;
  }
}

/* Pantallas medianas-grandes (1367px - 1599px) */
@media (min-width: 1367px) and (max-width: 1599px) {
  .navbar {
    padding: 20px 4% !important;
    gap: 18px !important;
  }

  .logo {
    font-size: 20px;
    margin-right: 35px;
  }

  .nav-links {
    gap: 70px;
  }

  .nav-links a {
    font-size: 14px;
  }

  .btn-admin {
    margin-right: 12px !important;
  }

  .main-content {
    max-width: 1100px;
  }

  .title {
    font-size: 46px;
  }

  .img-grapefruit {
    width: 160px;
    height: 160px;
    top: 40px;
    left: -70px;
  }
}

/* Pantallas medianas (1280px - 1366px) */
@media (min-width: 1280px) and (max-width: 1366px) {
  .navbar {
    padding: 20px 3% !important;
    gap: 12px !important;
  }

  .logo {
    font-size: 19px;
    margin-right: 30px;
  }

  .nav-links {
    gap: 60px;
  }

  .nav-links a {
    font-size: 14px;
  }

  .btn-admin {
    padding: 8px 26px;
    font-size: 12px;
    margin-right: 4px !important;
  }

  .btn-cerrar-sesion {
    padding: 8px 20px;
    font-size: 12px;
  }

  .main-content {
    max-width: 1000px;
  }

  .title {
    font-size: 44px;
  }

  .img-grapefruit {
    width: 160px;
    height: 160px;
    top: 70px;
    left: -70px;
  }

  .hoja-below {
    width: 80px;
    height: 80px;
    top: 420px;
  }

  .hoja-bottom {
    width: 70px;
    height: 70px;
  }

  .img-mortero {
    width: 200px;
    height: 200px;
    right: -60px;
  }
}

/* Pantallas pequeñas de laptop (1024px - 1279px) */
@media (min-width: 1024px) and (max-width: 1279px) {
  .navbar {
    padding: 20px 2% !important;
    gap: 10px !important;
  }

  .logo {
    font-size: 18px;
    margin-right: 25px;
  }

  .nav-links {
    gap: 50px;
  }

  .nav-links a {
    font-size: 13px;
  }

  .btn-admin {
    padding: 8px 24px;
    font-size: 13px;
    margin-right: 8px !important;
  }

  .btn-cerrar-sesion {
    padding: 8px 18px;
    font-size: 13px;
  }

  .main-content {
    max-width: 900px;
    padding: 140px 30px 60px;
  }

  .title {
    font-size: 42px;
    margin-top: -40px;
  }

  .img-grapefruit {
    width: 140px;
    height: 140px;
    top: -45px;
    left: -55px;
  }

  .hoja-below {
    width: 70px;
    height: 70px;
    top: 400px;
    right: 30px;
  }

  .hoja-bottom {
    width: 60px;
    height: 60px;
    bottom: 120px;
    left: 50px;
  }

  .img-mortero {
    width: 180px;
    height: 180px;
    right: -55px;
    top: 160px;
  }
}

/* Tablets (768px - 1023px) */
@media (max-width: 1023px) {
  .navbar {
    padding: 20px 2% !important;
    gap: 10px !important;
  }

  .logo {
    font-size: 17px;
    margin-right: 20px;
  }

  .nav-links {
    gap: 40px;
  }

  .nav-links a {
    font-size: 13px;
  }

  .btn-admin {
    padding: 7px 20px;
    font-size: 12px;
    margin-right: 8px !important;
  }

  .btn-cerrar-sesion {
    padding: 7px 16px;
    font-size: 12px;
  }

  .main-content {
    max-width: 750px;
    padding: 130px 25px 50px;
  }

  .title {
    font-size: 38px;
  }

  .img-grapefruit {
    width: 130px;
    height: 130px;
    top: -40px;
    left: -50px;
  }

  .hoja-below {
    width: 60px;
    height: 60px;
    top: 380px;
    right: 20px;
  }

  .hoja-bottom {
    width: 55px;
    height: 55px;
    bottom: 100px;
    left: 40px;
  }

  .img-mortero {
    width: 160px;
    height: 160px;
    right: -50px;
    top: 170px;
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

/* Tablets pequeñas (600px - 767px) */
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
    margin-right: 0;
    margin-bottom: 10px;
  }

  .nav-links {
    gap: 30px;
    width: 100%;
    justify-content: center;
  }

  .nav-links a {
    font-size: 13px;
  }

  .btn-admin {
    padding: 7px 20px;
    font-size: 12px;
    margin-left: 0 !important;
    margin-right: 5px !important;
  }

  .btn-cerrar-sesion {
    padding: 7px 16px;
    font-size: 12px;
  }

  .img-grapefruit,
  .hoja-below,
  .hoja-bottom,
  .img-mortero {
    display: none;
  }

  .main-content {
    padding: 160px 20px 40px;
    max-width: 100%;
  }

  .title {
    font-size: 32px;
    margin-bottom: 25px;
    margin-top: -20px;
  }

  .actions-bar {
    flex-direction: column;
    gap: 15px;
  }

  .btn-agregar {
    width: 100%;
    padding: 12px 24px;
    font-size: 13px;
  }

  .search-container {
    max-width: 100%;
  }

  .search-input {
    padding: 10px 20px 10px 50px;
    font-size: 14px;
  }

  .table-container {
    padding: 20px 10px;
    min-height: 240px;
    border-radius: 12px;
  }

  .empty-message {
    font-size: 14px;
  }

  .productos-table {
    font-size: 11px;
    border-radius: 12px;
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
    max-width: 150px;
    font-size: 11px;
  }

  .td-opciones {
    min-width: auto;
  }

  .opciones-container {
    gap: 5px;
  }

  .btn-editar,
  .btn-eliminar {
    padding: 6px 12px;
    font-size: 11px;
    width: 75px;
  }

  .paginacion {
    flex-direction: column;
    gap: 12px;
    padding: 15px;
  }
}

/* Móviles pequeños (menos de 600px) */
@media (max-width: 600px) {
  .navbar {
    padding: 12px 15px !important;
  }

  .logo {
    font-size: 16px;
    margin-left: 0;
  }

  .nav-links {
    gap: 20px;
    margin-left: 0;
  }

  .nav-links a {
    font-size: 12px;
  }

  .btn-admin {
    padding: 6px 16px;
    font-size: 11px;
  }

  .btn-cerrar-sesion {
    padding: 6px 14px;
    font-size: 11px;
  }

  .main-content {
    padding: 140px 15px 30px;
  }

  .title {
    font-size: 28px;
    margin-bottom: 20px;
  }

  .table-container {
    padding: 15px 5px;
  }

  .productos-table th,
  .productos-table td {
    padding: 6px 4px;
    font-size: 10px;
  }

  .img-container {
    width: 40px;
    height: 40px;
  }

  .btn-editar,
  .btn-eliminar {
    width: 65px;
    padding: 5px 8px;
    font-size: 10px;
  }

  .paginacion {
    padding: 12px;
  }

  .btn-paginacion {
    padding: 6px 12px;
    font-size: 13px;
  }

  .paginacion-info {
    font-size: 13px;
  }
}
</style>