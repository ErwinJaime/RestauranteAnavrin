<template>
  <div class="resenas-admin-container">
    <!-- Navegación -->
    <nav class="navbar">
      <h1 class="logo">ANAVRIN</h1>
      <div class="nav-links">
        <router-link to="/">Home</router-link>
        <router-link to="/about">About</router-link>
        <a href="#">Review</a>
      </div>
      <button class="btn-admin">Admin</button>
      <button class="btn-cerrar-sesion">Cerrar Sesión</button>
    </nav>

    <!-- Imagen Naranja superior izquierda -->
    <img src="@/assets/naranja.png" alt="Naranja" class="img-naranja">

    <!-- Imagen Aceite superior derecha -->
    <img src="@/assets/aceite.png" alt="Aceite" class="img-aceite">

    <!-- Contenido Principal -->
    <div class="main-content">
      <h1 class="title">Reseñas</h1>

      <!-- Tarjetas de reseñas -->
      <div class="resenas-container">
        <div 
          v-for="resena in resenasPaginaActual" 
          :key="resena.id" 
          class="resena-card"
        >
          <button class="btn-eliminar" @click="eliminarResena(resena.id)">✕</button>
          <div class="resena-header">
            <img :src="require(`@/assets/${resena.emoji}.png`)" :alt="resena.emoji" class="emoji">
            <h3 class="nombre-usuario">{{ resena.nombre }}</h3>
          </div>
          <p class="resena-texto">{{ resena.texto }}</p>
        </div>
      </div> 

      <!-- Flechas de navegación -->
      <div class="navegacion-flechas">
        <button class="flecha flecha-izq" @click="paginaAnterior" :disabled="paginaActual === 0">←</button>
        <button class="flecha flecha-der" @click="paginaSiguiente" :disabled="paginaActual >= totalPaginas - 1">→</button>
      </div>
    </div>

    <!-- Imagen Guacamole inferior izquierda -->
    <img src="@/assets/guacamole.png" alt="Guacamole" class="img-guacamole">

    <!-- Estrellas decorativas -->
    <img src="@/assets/estrellas.png" alt="Estrellas" class="img-estrellas">
  </div>
</template>

<script>
import { ref, computed } from 'vue'

export default {
  name: 'ResenasAdmin',
  setup() {
    const paginaActual = ref(0)
    const resenasPorPagina = 3

    const todasLasResenas = ref([
      { 
        id: 1,
        nombre: 'Tatiana Gualteros',
        texto: '"Buena presentación, sabores equilibrados y un ambiente agradable. Ideal para venir con amigos o desconectarse un rato."',
        emoji: 'feliz'
      },
      { 
        id: 2,
        nombre: 'Erwin Jaimes',
        texto: '"Excelente atención y productos de calidad. El menú es variado y todo llega fresco y bien presentado."',
        emoji: 'feliz'
      },
      { 
        id: 3,
        nombre: 'Pedro Suárez',
        texto: '"El plato estaba crudo, el servicio terrible, no lo recomiendo."',
        emoji: 'triste'
      },
      { 
        id: 4,
        nombre: 'Tatiana Nieto',
        texto: '"Excelente servicio, las bebidas son deliciosas."',
        emoji: 'feliz'
      }
    ])

    const resenasPaginaActual = computed(() => {
      const inicio = paginaActual.value * resenasPorPagina
      const fin = inicio + resenasPorPagina
      return todasLasResenas.value.slice(inicio, fin)
    })

    const totalPaginas = computed(() => {
      return Math.ceil(todasLasResenas.value.length / resenasPorPagina)
    })

    const eliminarResena = (id) => {
      const index = todasLasResenas.value.findIndex(r => r.id === id)
      if (index !== -1) {
        todasLasResenas.value.splice(index, 1)
        
        // Ajustar página si es necesario
        if (resenasPaginaActual.value.length === 0 && paginaActual.value > 0) {
          paginaActual.value--
        }
      }
    }

    const paginaSiguiente = () => {
      if (paginaActual.value < totalPaginas.value - 1) {
        paginaActual.value++
      }
    }

    const paginaAnterior = () => {
      if (paginaActual.value > 0) {
        paginaActual.value--
      }
    }

    return {
      paginaActual,
      resenasPaginaActual,
      totalPaginas,
      eliminarResena,
      paginaSiguiente,
      paginaAnterior
    }
  }
}
</script>

<style scoped>
/* General */
.resenas-admin-container {
  width: 100%;
  min-height: 100vh;
  background-color: #ffffff;
  position: relative;
  overflow-x: hidden;
  padding-bottom: 0;
  margin-bottom: 0;
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
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 580;
  margin-right: -230px;
}

.btn-admin:hover {
  background-color: #3b82f6;
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
.img-naranja {
  position: fixed;
  top: 60px;
  left: 15px;
  width: 160px;
  height: 160px;
  object-fit: contain;
  z-index: 60;
}

.img-aceite {
  position: fixed;
  top: 50px;
  right: 2px;
  width: 150px;
  height: 150px;
  object-fit: contain;
  z-index: 5;
}

.img-guacamole {
  position: fixed;
  bottom: -60px;
  left: 70px;
  width: 200px;
  height: 200px;
  object-fit: contain;
  z-index: 5;
}

.img-estrellas {
  position: fixed;
  bottom: 0;
  right: 5px;
  width: 140px;
  height: 140px;
  object-fit: contain;
  z-index: 5;
}

/* Contenido Principal */
.main-content {
  max-width: 1100px;
  margin: 0 auto;
  padding-top: 140px;
  padding-bottom: 20px;
  text-align: center;
}

.title {
  font-size: 45px;
  font-weight: 800;
  color: #28233b;
  margin-bottom: 50px;
  margin-top: -20px;
  font-family: 'Open Sans', sans-serif;
}

/* Contenedor de reseñas */
.resenas-container {
  display: grid;
  grid-template-columns: repeat(3, 350px);
  gap: 25px;
  margin-bottom: 40px;
  padding: 0 20px;
  min-height: 150px;
  justify-content: center;
}

/* Tarjetas de reseña */
.resena-card {
  background-color: #e8e5b8;
  border-radius: 20px;
  padding: 25px 20px;
  position: relative;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  max-width: 350px;
  min-height: 200px;
}

.btn-eliminar {
  position: absolute;
  top: 15px;
  right: 15px;
  width: 30px;
  height: 30px;
  background-color: #dc3545;
  color: white;
  border: none;
  border-radius: 50%;
  font-size: 18px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
}

.btn-eliminar:hover {
  background-color: #c82333;
  transform: scale(1.1);
}

.resena-header {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  margin-bottom: 15px;
  width: 100%;
}

.emoji {
  width: 45px;
  height: 45px;
  object-fit: contain;
  flex-shrink: 0;
}

.nombre-usuario {
  font-size: 17px;
  font-weight: 700;
  color: #1a1a1a;
  margin: 0;
  font-family: 'Open Sans', sans-serif;
  text-align: left;
  line-height: 45px;
}

.resena-texto {
  font-size: 14px;
  line-height: 1.6;
  color: #333;
  margin: 0;
  font-family: 'Montserrat', sans-serif;
  text-align: center;
}

/* Navegación flechas */
.navegacion-flechas {
  display: flex;
  gap: 0px;
  justify-content: center;
  margin-top: 30px;
}

.flecha {
  width: 60px;
  height: 60px;
  background-color: transparent;
  border: none;
  font-size: 40px;
  color: #ff6b35;
  cursor: pointer;
  transition: all 0.3s ease;
}

.flecha:hover:not(:disabled) {
  color: #3b82f6;
  transform: scale(1.2);
}

.flecha:disabled {
  color: #ccc;
  cursor: not-allowed;
  opacity: 0.5;
}
</style>