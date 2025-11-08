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
        <p v-else class="empty-message">Gestiona todos tus productos</p>
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
import { ref, onMounted } from 'vue'
import axios from 'axios'
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

    const API_URL = 'http://localhost:3000/api' // Ejemplo

    // Cargar productos al montar el componente
    onMounted(() => {
      cargarProductos()
    })

    const cargarProductos = async () => {
      try {
        cargando.value = true
        const response = await axios.get(`${API_URL}/productos`)
        productos.value = response.data
      } catch (error) {
        console.error('Error al cargar productos:', error)
        alert('Error al cargar los productos')
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
        const response = await axios.post(`${API_URL}/productos`, {
          nombre: producto.nombreProducto,
          categoria: producto.categoria,
          ingredientes: producto.ingredientes,
          precio: producto.precio,
          disponible: producto.disponible,
          imagen: producto.imagen
        })

        // Agregar el nuevo producto a la lista
        productos.value.push(response.data)
        
        cerrarModal()
        alert('¡Producto agregado exitosamente!')
        
        // Recargar la lista
        await cargarProductos()
      } catch (error) {
        console.error('Error al guardar producto:', error)
        alert('Error al guardar el producto')
      } finally {
        cargando.value = false
      }
    }

    const editarProducto = async (id) => {
      // Aquí implementarás la lógica de editar
      console.log('Editar producto:', id)
      alert('Función de editar en desarrollo')
    }

    const eliminarProducto = async (id) => {
      if (!confirm('¿Estás seguro de eliminar este producto?')) {
        return
      }

      try {
        cargando.value = true
        await axios.delete(`${API_URL}/productos/${id}`)
        
        // Eliminar de la lista local
        productos.value = productos.value.filter(p => p.id !== id)
        
        alert('Producto eliminado exitosamente')
      } catch (error) {
        console.error('Error al eliminar producto:', error)
        alert('Error al eliminar el producto')
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
      eliminarProducto
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
  color: white;
}

/* Imágenes decorativas */
.img-grapefruit {
  position: fixed;
  top: -80px;
  left: 70px;
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
  margin-top: -40px;
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
    font-size: 15px;
    margin-right: 5px !important;
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

  .img-grapefruit {
    width: 160px;
    height: 160px;
    top:40px;
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

/* Pantallas medianas (1280px - 1366px) - 15.6" HD */
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
    font-size: 14px;
    margin-right: 4px !important;
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
    top: 80px;
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

/* Pantallas pequeñas de laptop (1024px - 1279px) - 14" */
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
    padding: 12px 15px !important;
  }

  .logo {
    font-size: 16px;
  }

  .nav-links {
    gap: 20px;
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
    margin-top: -10px;
  }

    .table-container {
    padding: 25px 15px;
    min-height: 200px;
  }
}
</style>