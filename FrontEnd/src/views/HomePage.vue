<template>
  <div class="container">
    <!-- Navegación -->
    <nav class="navbar">
      <h1 class="logo">ANAVRIN</h1>
      <div class="nav-links">
        <a href="#">Home</a>
        <a href="#">About</a>
        <a href="#">Review</a>
      </div>
      <button class="btn-login">Inicia Sesión</button>
      <img src="@/assets/aceite.png" alt="Aceite" class="img-aceite">
    </nav>
    <!-- SECCIÓN 1: Sabores que Enamoran -->
    <section class="section-one">
      <!-- Contenido Izquierdo -->
      <div class="content-left">
        <h1 class="title">Sabores que<br>Enamoran</h1>
        <p class="description">
          Descubre postres, bebidas y platillos<br>
          creados para sorprender cada uno de<br>
          tus sentidos.
        </p>
        <img src="@/assets/hoja.png" alt="Hoja" class="hoja-decoration"> 
        <button 
          @click="goToNext"
          @mouseover="hoveredButton = true"
          @mouseout="hoveredButton = false"
          :class="['btn-siguiente', { hovered: hoveredButton }]"
        >
          Siguiente →
        </button>
      </div>

      <!-- Imágenes Derecha -->
      <div class="content-right">
        <!-- Grapefruit arriba -->
        <img src="@/assets/grapefruit.png" alt="Grapefruit" class="img-grapefruit">
        
        <!-- Plato principal -->
        <img src="@/assets/plato-principal.png" alt="Plato Principal" class="img-plato">
      </div>
    </section>
  </div>
</template>

<script>
import { ref } from 'vue'

export default {
  name: 'HomePage',
  setup() {
    const hoveredButton = ref(false)

    const goToNext = () => {
      console.log('Ir a siguiente sección')
    }

    return {
      hoveredButton,
      goToNext
    }
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400&display=swap');
/* General */
.container {
  width: 100%;
  height: 100vh;
  background-color: #ffffff;
  overflow: visible;
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
  align-items: center;
}

.logo {
  font-size: 22px;
  font-weight: 600;
  color: #1a1a1a;
  letter-spacing: 1px;
  margin-left: 75px;
}

.nav-links {
  display: flex;
  gap: 60px;
}

.nav-links a {
  font-size: 14px;
  color: #666;
  text-decoration: none;
  transition: color 0.3s ease;
}

.nav-links a:hover {
  color: #6d9fef;
}

.btn-login {
  padding: 10px 24px;
  font-size: 14px;
  color: #070707;
  border: 2px solid #ddd2d288;
  background-color: transparent;
  border-radius: 50px;
  cursor: pointer;
  transition: all 0.3s ease;
  margin-right: -160px;
}

.btn-login:hover {
  background-color: #6d9fef;
  color: white;
}

/* Sección 1 */
.section-one {
  min-height: 100vh;
  display: flex;
  align-items: center;
  padding-top: 200px;
  padding-left: 10px;
  padding-right: 80px;
  gap: 80px;
  overflow: visible;
}

/* Contenido Izquierdo */
.content-left {
  width: 55%;
  position: relative;
  padding-left: 160px;
  text-align: left;
}

.title {
  font-size: 65px;
  font-weight: 700;
  color: #1a1a1a;
  line-height: 1.0;
  margin-bottom: 9px;
  margin-bottom: 10px;
  font-family: 'Open Sans', sans-serif;
}

.description {
  font-size: 15px;
  color: #666;
  line-height: 1.3;
  margin-bottom: 30px;
  font-weight: 400;
  font-family: 'Montserrat', sans-serif;
}

.hoja-decoration {
  width: 150px;
  height: 150px;
  object-fit: contain;
  margin-bottom: 20px;
  margin-left: 100px;
  display: block;
} 

.img-aceite {
  width: 120px;
  object-fit: contain;
  margin-right: -80px;
  margin-top: -30px
}

.btn-siguiente {
  padding: 10px 36px;
  font-size: 15px;
  border: solid #ddd2d288 ;
  font-weight: 600;
  background-color: #fff;
  border-radius: 50px ;
  cursor: pointer;
  transition: all 0.3s ease;
  margin-left: -130px;  
}

.btn-siguiente:hover,
.btn-siguiente.hovered {
  background-color: #3b82f6;
  color: white;
  border-color: #3b82f6;
}

/* Contenido Derecho - Imágenes */
.content-right {
  width: 50%;
  position: relative;
  height: 500px;
}

.img-grapefruit {
  position: fixed;
  top: 80px;
  left: 30px;
  width: 160px;
  height: 160px;
  object-fit: contain;
  z-index: 10;
}

.img-plato {
  position: absolute;
  top: 40%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 500px;
  height: 450px;
  object-fit: contain;
}
</style>