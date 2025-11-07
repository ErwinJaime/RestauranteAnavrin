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

    <!-- Imagen Grapefruit superior izquierda -->
    <img src="@/assets/grapefruit.png" alt="Grapefruit" class="img-grapefruit">

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
        <p v-else class="empty-message">Gestiona todos tus productos</p>
      </div>
    </div>

    <!-- Hojas decorativas -->
    <img src="@/assets/hoja3.png" alt="Hoja" class="hoja-below">
    <img src="@/assets/hoja2.png" alt="Hoja" class="hoja-bottom">
  
    
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
import { ref, onMounted } from 'vue'
import { listarProductos, crearProducto, eliminarProducto } from '@/services/productos'
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

    onMounted(() => {
      cargarProductos()
    })

    const cargarProductos = async () => {
      try {
        cargando.value = true
        // Usamos el servicio de productos importado
        const response = await listarProductos()
        productos.value = response.data
      } catch (error) {
        console.log('No se pudieron cargar los productos')
        
        // Manejar error de autenticación
        if (error.response?.status === 401) {
          console.log('Error de autenticación al cargar productos')
        }
        
        productos.value = []
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

    const guardarProducto = async (productoData) => {
      try {
        cargando.value = true
        
        // Verificar autenticación
        const token = localStorage.getItem('access_token')
        if (!token) {
          alert('No estás autenticado. Por favor, inicia sesión.')
          mostrarModal.value = false
          return
        }

        console.log('📥 Datos recibidos del modal:', productoData)
        
        // Preparar los datos para el backend
        const datosParaEnviar = {
          nombre: productoData.nombreProducto,
          categoria: productoData.categoria, // Ya viene en minúsculas del modal
          ingredientes: productoData.ingredientes,
          precio: parseFloat(productoData.precio),
          disponible: Boolean(productoData.disponible),
        }

        // Agregar imagen solo si existe
        if (productoData.imagen && productoData.imagen instanceof File) {
          datosParaEnviar.imagen = productoData.imagen
        }

        console.log('📤 Datos a enviar al backend:', datosParaEnviar)

        // Crear producto usando el servicio
        const response = await crearProducto(datosParaEnviar)

        console.log('✅ Producto creado exitosamente:', response.data)

        // Agregar el nuevo producto a la lista
        productos.value.push(response.data)
        
        // Cerrar modal y limpiar
        cerrarModal()
        alert('¡Producto agregado exitosamente!')
        
        // Recargar la lista completa
        await cargarProductos()
        
      } catch (error) {
        console.error('❌ Error al guardar producto:', error)
        
        // Manejo detallado de errores
        if (error.response) {
          const status = error.response.status
          const errorData = error.response.data
          
          console.error('Detalles del error:', errorData)
          
          if (status === 400) {
            // Error de validación
            let mensajeError = 'Error en los datos del producto:\n'
            
            if (typeof errorData === 'object') {
              Object.keys(errorData).forEach(key => {
                const errores = Array.isArray(errorData[key]) ? errorData[key] : [errorData[key]]
                mensajeError += `\n• ${key}: ${errores.join(', ')}`
              })
            } else {
              mensajeError = errorData.toString()
            }
            
            alert(mensajeError)
          } else if (status === 401) {
            alert('Tu sesión ha expirado. Por favor, inicia sesión nuevamente.')
            localStorage.removeItem('access_token')
            localStorage.removeItem('refresh_token')
            localStorage.removeItem('user')
            // router.push('/login') // Descomenta si tienes router
          } else if (status === 403) {
            alert('No tienes permisos para agregar productos.')
          } else {
            alert(`Error del servidor (${status}). Por favor, intenta nuevamente.`)
          }
        } else if (error.request) {
          alert('No se pudo conectar con el servidor. Verifica tu conexión.')
        } else {
          alert('Error inesperado: ' + error.message)
        }
      } finally {
        cargando.value = false
      }
    }

    const editarProducto = async (id) => {
      console.log('Editar producto:', id)
      alert('Función de editar en desarrollo')
    }

    const eliminarProductoHandler = async (id) => {
      if (!confirm('¿Estás seguro de eliminar este producto?')) {
        return
      }

      try {
        cargando.value = true
        
        // Verificar autenticación antes de eliminar
        const token = localStorage.getItem('access_token')
        if (!token) {
          alert('No estás autenticado. Por favor, inicia sesión.')
          return
        }
        
        // Usar el servicio importado eliminarProducto
        await eliminarProducto(id)
        
        // Eliminar de la lista local
        productos.value = productos.value.filter(p => p.id !== id)
        
        alert('Producto eliminado exitosamente')
      } catch (error) {
        console.error('Error al eliminar producto:', error)
        
        // Manejar diferentes tipos de errores
        if (error.response?.status === 401) {
          alert('Error de autenticación. Tu sesión ha expirado.')
          localStorage.removeItem('access_token')
          localStorage.removeItem('refresh_token')
          localStorage.removeItem('user')
        } else if (error.response?.status === 403) {
          alert('No tienes permisos para eliminar productos.')
        } else if (error.response?.status === 404) {
          alert('El producto no existe o ya fue eliminado.')
        } else {
          alert('Error al eliminar el producto.')
        }
      } finally {
        cargando.value = false
      }
    }

    return {
      searchQuery,
      mostrarModal,
      productos,
      cargando,
      abrirModal,
      cerrarModal,
      guardarProducto,
      editarProducto,
      eliminarProducto: eliminarProductoHandler
    }
  }
}
</script>

<style scoped>
/* General */
.inventario-container {
  width: 100%;
  height: 100vh;
  background-color: #ffffff;
  position: relative;
  overflow: hidden;
}

/* Navegación */
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 50;
  background-color: #ffffff;
  padding: 20px 40px;
  display: grid;
  grid-template-columns: 200px 1fr auto auto;
  align-items: center;
  gap: 30px;
}

.logo {
  font-size: 20px;
  font-weight: 600;
  color: #1a1a1a;
  letter-spacing: 1px;
  justify-self: start;
  padding-left: 20px;
}

.nav-links {
  display: flex;
  gap: 60px;
  flex: 1;
  justify-content: center;
  align-items: center;
}

.nav-links a,
.nav-links router-link {
  font-size: 14px;
  color: #666;
  text-decoration: none;
  transition: color 0.3s ease;
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
}

.btn-cerrar-sesion:hover {
  background-color: #6d9fef;
  color: white;
}

/* Imágenes decorativas */
.img-grapefruit {
  position: fixed;
  top: -55px;
  left: -65px;
  width: 180px;
  height: 180px;
  object-fit: contain;
  z-index: 60;
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
  margin-top: -40px;
  font-family: 'Open Sans', sans-serif;
}

/* Barra de acciones */
.actions-bar {
  display: flex;
  align-items: center;
  gap: 20px;
  margin-bottom: 40px;
  max-width: 900px;
  margin-left: 0;
  margin-right: auto;
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
  margin-left: 165px;
  margin-top: -20px;
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
  margin-top: -20px;
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
  padding: 60px 40px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.336);
  min-height: 320px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: -30px;
}

.empty-message {
  color: #8b8585b0;
  font-size: 16px;
  font-weight:500;
  font-family: 'Montserrat', sans-serif;
}

/* ===== RESPONSIVE DESIGN ===== */

/* Pantallas grandes (1600px+) */
@media (min-width: 1600px) {
  .navbar {
    padding: 20px 80px;
    grid-template-columns: 250px 1fr auto auto;
    gap: 40px;
  }

  .logo {
    font-size: 22px;
    padding-left: 40px;
  }

  .nav-links {
    gap: 80px;
  }

  .nav-links a {
    font-size: 15px;
  }

  .btn-admin {
    padding: 10px 32px;
    font-size: 15px;
  }

  .btn-cerrar-sesion {
    padding: 10px 26px;
    font-size: 15px;
  }

  .main-content {
    max-width: 1200px;
    padding: 140px 60px 60px;
  }

  .title {
    font-size: 50px;
  }
}

/* Pantallas medianas-grandes (1367px - 1599px) */
@media (min-width: 1367px) and (max-width: 1599px) {
  .navbar {
    padding: 20px 60px;
    grid-template-columns: 220px 1fr auto auto;
    gap: 35px;
  }

  .logo {
    font-size: 20px;
    padding-left: 30px;
  }

  .nav-links {
    gap: 70px;
  }

  .nav-links a {
    font-size: 14px;
  }

  .main-content {
    max-width: 1100px;
  }

  .title {
    font-size: 46px;
  }
}

/* Pantallas medianas (1280px - 1366px) - 15.6" HD */
@media (min-width: 1280px) and (max-width: 1366px) {
  .navbar {
    padding: 20px 50px;
    grid-template-columns: 200px 1fr auto auto;
    gap: 30px;
  }

  .logo {
    font-size: 19px;
    padding-left: 25px;
  }

  .nav-links {
    gap: 60px;
  }

  .nav-links a {
    font-size: 14px;
  }

  .btn-admin {
    padding: 8px 26px;
    font-size: 14px;
  }

  .btn-cerrar-sesion {
    padding: 8px 20px;
    font-size: 14px;
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
    top: -50px;
    left: -60px;
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

/* Pantallas pequeñas de laptop (1024px - 1279px) - 14" */
@media (min-width: 1024px) and (max-width: 1279px) {
  .navbar {
    padding: 20px 40px;
    grid-template-columns: 180px 1fr auto auto;
    gap: 25px;
  }

  .logo {
    font-size: 18px;
    padding-left: 20px;
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
    padding: 20px 30px;
    grid-template-columns: 160px 1fr auto auto;
    gap: 20px;
  }

  .logo {
    font-size: 17px;
    padding-left: 15px;
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
}

/* Tablets pequeñas (600px - 767px) */
@media (max-width: 767px) {
  .navbar {
    padding: 15px 20px;
    grid-template-columns: 1fr;
    grid-template-rows: auto auto;
    gap: 15px;
    justify-items: center;
  }

  .logo {
    font-size: 18px;
    padding-left: 0;
    grid-column: 1 / -1;
  }

  .nav-links {
    gap: 30px;
    grid-column: 1 / -1;
    order: 1;
  }

  .nav-links a {
    font-size: 13px;
  }

  .btn-admin {
    padding: 7px 20px;
    font-size: 12px;
    order: 2;
  }

  .btn-cerrar-sesion {
    padding: 7px 16px;
    font-size: 12px;
    order: 3;
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
    padding: 30px 20px;
    min-height: 240px;
  }

  .empty-message {
    font-size: 14px;
  }
}

/* Móviles (hasta 599px) */
@media (max-width: 599px) {
  .navbar {
    padding: 12px 15px;
  }

  .logo {
    font-size: 16px;
  }

  .nav-links {
    gap: 20px;
    flex-wrap: wrap;
  }

  .nav-links a {
    font-size: 12px;
  }

  .btn-admin,
  .btn-cerrar-sesion {
    padding: 6px 16px;
    font-size: 11px;
  }

  .main-content {
    padding: 170px 15px 30px;
  }

  .title {
    font-size: 28px;
    margin-bottom: 20px;
  }

  .table-container {
    padding: 25px 15px;
    min-height: 200px;
  }
}
</style>