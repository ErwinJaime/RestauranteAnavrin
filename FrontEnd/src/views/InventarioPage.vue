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
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 50;
  background-color: #ffffff;
  padding: 20px 80px;
  display: flex;
  justify-content: space-between;
  gap: 20px;
  margin-right: -500px;
}

.logo {
  font-size: 20px;
  font-weight: 600;
  color: #1a1a1a;
  letter-spacing: 1px;
  margin-left: 70px;
}

.nav-links {
  display: flex;
  gap: 60px;
  margin-left: 30px;
}

.nav-links a,
.nav-links router-link {
  font-size: 14px;
  color: #666;
  text-decoration: none;
  transition: color 0.3s ease;
}

.nav-links a:hover,
.nav-links router-link:hover {
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
  margin-right: -230px;
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
  margin-right: 440px;
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
  margin-top: -80px;
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

/* Tablets (768px - 1024px) */
@media (max-width: 1024px) {
  .navbar {
    padding: 20px 40px;
    margin-right: 0;
    justify-content: space-between;
  }

  .logo {
    margin-left: 0;
    font-size: 18px;
  }

  .nav-links {
    gap: 30px;
    margin-left: 20px;
  }

  .nav-links a,
  .nav-links router-link {
    font-size: 13px;
  }

  .btn-admin {
    margin-right: 0;
    padding: 8px 20px;
    font-size: 13px;
  }

  .btn-cerrar-sesion {
    margin-right: 0;
    padding: 8px 18px;
    font-size: 13px;
  }

  /* Imágenes decorativas más pequeñas */
  .img-grapefruit {
    width: 140px;
    height: 140px;
    top: -45px;
    left: -50px;
  }

  .hoja-below {
    width: 70px;
    height: 70px;
    top: 400px;
    right: 20px;
  }

  .hoja-bottom {
    width: 60px;
    height: 60px;
    bottom: 120px;
    left: 40px;
  }

  .img-mortero {
    width: 180px;
    height: 180px;
    right: -50px;
    top: 160px;
  }

  .main-content {
    max-width: 700px;
    padding: 120px 30px 60px;
  }

  .title {
    font-size: 38px;
    margin-top: -60px;
  }

  .actions-bar {
    max-width: 100%;
    margin-left: 0;
    gap: 15px;
  }

  .btn-agregar {
    margin-left: 0;
    padding: 10px 24px;
    font-size: 11px;
  }

  .search-container {
    max-width: 350px;
  }

  .table-container {
    padding: 40px 30px;
    min-height: 280px;
  }
}

/* Pantallas medianas de computador (769px - 1200px) */
@media (min-width: 769px) and (max-width: 1200px) {
  .navbar {
    padding: 20px 50px;
  }

  .logo {
    margin-left: 20px;
  }

  .nav-links {
    gap: 40px;
    margin-left: 25px;
  }

  .btn-admin {
    margin-right: -100px;
  }

  .btn-cerrar-sesion {
    margin-right: 200px;
  }

  .main-content {
    max-width: 800px;
  }

  .title {
    font-size: 40px;
  }

  .btn-agregar {
    margin-left: 80px;
  }

  .img-mortero {
    right: -55px;
  }
}

/* Tablets pequeñas (600px - 768px) */
@media (max-width: 768px) {
  .navbar {
    padding: 15px 20px;
    flex-wrap: wrap;
    gap: 10px;
  }

  .logo {
    font-size: 16px;
    margin-left: 0;
  }

  .nav-links {
    gap: 20px;
    margin-left: 0;
    order: 3;
    width: 100%;
    justify-content: center;
    padding-top: 10px;
  }

  .nav-links a,
  .nav-links router-link {
    font-size: 12px;
  }

  .btn-admin {
    padding: 6px 16px;
    font-size: 12px;
    margin-right: 0;
  }

  .btn-cerrar-sesion {
    padding: 6px 14px;
    font-size: 12px;
    margin-right: 0;
  }

  /* Ocultar imágenes decorativas en tablets pequeñas */
  .img-grapefruit,
  .hoja-below,
  .hoja-bottom,
  .img-mortero {
    display: none;
  }

  .main-content {
    padding: 140px 20px 40px;
    max-width: 100%;
  }

  .title {
    font-size: 32px;
    margin-top: -40px;
    margin-bottom: 25px;
  }

  .actions-bar {
    flex-direction: column;
    align-items: stretch;
    gap: 15px;
    margin-bottom: 30px;
  }

  .btn-agregar {
    margin-left: 0;
    margin-top: 0;
    width: 100%;
    padding: 12px 24px;
    font-size: 13px;
  }

  .search-container {
    max-width: 100%;
    margin-top: 0;
  }

  .search-input {
    padding: 10px 20px 10px 50px;
    font-size: 14px;
  }

  .table-container {
    padding: 30px 20px;
    min-height: 240px;
    margin-top: 0;
  }

  .empty-message {
    font-size: 14px;
  }
}

/* Pantallas pequeñas de computador (1025px - 1366px) */
@media (min-width: 1025px) and (max-width: 1366px) {
  .navbar {
    padding: 20px 60px;
    margin-right: -300px;
  }

  .logo {
    margin-left: 40px;
  }

  .btn-admin {
    margin-right: -150px;
  }

  .btn-cerrar-sesion {
    margin-right: 300px;
  }

  .main-content {
    max-width: 850px;
  }

  .btn-agregar {
    margin-left: 120px;
  }
}

/* Pantallas de 15.6 pulgadas - 1366x768 (HD) */
@media (min-width: 1280px) and (max-width: 1440px) {
  .navbar {
    padding: 18px 60px;
    margin-right: -250px;
  }

  .logo {
    margin-left: 50px;
    font-size: 19px;
  }

  .nav-links {
    gap: 50px;
    margin-left: 25px;
  }

  .nav-links a,
  .nav-links router-link {
    font-size: 13.5px;
  }

  .btn-admin {
    margin-right: -180px;
    padding: 8px 26px;
    font-size: 13.5px;
  }

  .btn-cerrar-sesion {
    margin-right: 350px;
    padding: 8px 20px;
    font-size: 13.5px;
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
    right: 30px;
  }

  .hoja-bottom {
    width: 70px;
    height: 70px;
    bottom: 130px;
    left: 60px;
  }

  .img-mortero {
    width: 200px;
    height: 200px;
    right: -60px;
    top: 150px;
  }

  .main-content {
    max-width: 850px;
    padding-top: 130px;
  }

  .title {
    font-size: 42px;
    margin-top: -70px;
  }

  .actions-bar {
    margin-bottom: 35px;
  }

  .btn-agregar {
    margin-left: 140px;
    padding: 10px 30px;
    font-size: 12px;
  }

  .search-container {
    max-width: 380px;
  }

  .table-container {
    padding: 55px 35px;
    min-height: 300px;
  }
}

/* Pantallas de 15.6 pulgadas - 1920x1080 (Full HD) */
@media (min-width: 1680px) and (max-width: 1920px) {
  .navbar {
    padding: 20px 100px;
    margin-right: -400px;
  }

  .logo {
    margin-left: 80px;
  }

  .nav-links {
    gap: 70px;
    margin-left: 40px;
  }

  .btn-admin {
    margin-right: -200px;
  }

  .btn-cerrar-sesion {
    margin-right: 380px;
  }

  .img-grapefruit {
    width: 200px;
    height: 200px;
    top: -60px;
    left: -70px;
  }

  .hoja-below {
    width: 100px;
    height: 100px;
    top: 480px;
    right: 50px;
  }

  .hoja-bottom {
    width: 90px;
    height: 90px;
    bottom: 150px;
    left: 80px;
  }

  .img-mortero {
    width: 250px;
    height: 250px;
    right: -70px;
    top: 130px;
  }

  .main-content {
    max-width: 1000px;
  }

  .title {
    font-size: 48px;
  }

  .btn-agregar {
    margin-left: 180px;
  }
}
</style>