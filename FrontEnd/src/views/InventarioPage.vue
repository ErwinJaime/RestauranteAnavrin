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
        <p class="empty-message">Gestiona todos tus productos</p>
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
import { ref } from 'vue'
import AgregarProducto from './AgregarProducto.vue' 

export default {
  name: 'InventarioPage',
  components: {
    AgregarProducto
  },
  setup() {
    const searchQuery = ref('')
    const mostrarModal = ref(false)

    const abrirModal = () => {
      mostrarModal.value = true
    }

    const cerrarModal = () => {
      mostrarModal.value = false
    }

    const guardarProducto = (producto) => {
      console.log('Producto guardado:', producto)
      // Aquí agregarías la lógica para guardar en tu base de datos
      cerrarModal()
    }

    return {
      searchQuery,
      mostrarModal,
      abrirModal,
      cerrarModal,
      guardarProducto
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
</style>