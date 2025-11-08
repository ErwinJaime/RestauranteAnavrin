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
      <div class="buttons">
        <button class="btn-admin">Admin</button>
        <button class="btn-cerrar-sesion">Cerrar Sesión</button>
      </div>
    </nav>

    <!-- Imágenes decorativas -->
    <img src="@/assets/naranja.png" alt="Naranja" class="img-naranja" />
    <img src="@/assets/aceite.png" alt="Aceite" class="img-aceite" />

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
            <img
              :src="require(`@/assets/${resena.emoji}.png`)"
              :alt="resena.emoji"
              class="emoji"
            />
            <h3 class="nombre-usuario">{{ resena.nombre }}</h3>
          </div>
          <p class="resena-texto">{{ resena.texto }}</p>
        </div>
      </div>

      <!-- Flechas de navegación -->
      <div class="navegacion-flechas">
        <button
          class="flecha flecha-izq"
          @click="paginaAnterior"
          :disabled="paginaActual === 0"
        >
          ←
        </button>
        <button
          class="flecha flecha-der"
          @click="paginaSiguiente"
          :disabled="paginaActual >= totalPaginas - 1"
        >
          →
        </button>
      </div>
    </div>

    <!-- Imágenes inferiores -->
    <img src="@/assets/guacamole.png" alt="Guacamole" class="img-guacamole" />
    <img src="@/assets/estrellas.png" alt="Estrellas" class="img-estrellas" />
  </div>
</template>

<script setup>
import { ref, computed } from "vue";

const paginaActual = ref(0);
const resenasPorPagina = 3;

const todasLasResenas = ref([
  {
    id: 1,
    nombre: "Tatiana Gualteros",
    texto:
      '"Buena presentación, sabores equilibrados y un ambiente agradable. Ideal para venir con amigos o desconectarse un rato."',
    emoji: "feliz",
  },
  {
    id: 2,
    nombre: "Erwin Jaimes",
    texto:
      '"Excelente atención y productos de calidad. El menú es variado y todo llega fresco y bien presentado."',
    emoji: "feliz",
  },
  {
    id: 3,
    nombre: "Pedro Suárez",
    texto:
      '"El plato estaba crudo, el servicio terrible, no lo recomiendo."',
    emoji: "triste",
  },
  {
    id: 4,
    nombre: "Tatiana Nieto",
    texto: '"Excelente servicio, las bebidas son deliciosas."',
    emoji: "feliz",
  },
]);

const resenasPaginaActual = computed(() => {
  const inicio = paginaActual.value * resenasPorPagina;
  const fin = inicio + resenasPorPagina;
  return todasLasResenas.value.slice(inicio, fin);
});

const totalPaginas = computed(() =>
  Math.ceil(todasLasResenas.value.length / resenasPorPagina)
);

const eliminarResena = (id) => {
  const index = todasLasResenas.value.findIndex((r) => r.id === id);
  if (index !== -1) {
    todasLasResenas.value.splice(index, 1);
    if (resenasPaginaActual.value.length === 0 && paginaActual.value > 0) {
      paginaActual.value--;
    }
  }
};

const paginaSiguiente = () => {
  if (paginaActual.value < totalPaginas.value - 1) paginaActual.value++;
};
const paginaAnterior = () => {
  if (paginaActual.value > 0) paginaActual.value--;
};
</script>

<style scoped>
/* ------------------------
   BASE
------------------------- */
.resenas-admin-container {
  width: 100%;
  min-height: 100vh;
  background-color: #ffffff;
  position: relative;
  overflow-x: hidden;
  padding-bottom: 2rem;
}

/* ------------------------
   NAVBAR
------------------------- */
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  background-color: #ffffff;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 20px 60px;
  z-index: 50;
  flex-wrap: wrap;
  box-shadow: 0 1px 4px rgba(255, 255, 255, 0.05);
}

.logo {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1a1a1a;
}

.nav-links {
  display: flex;
  gap: 2rem;
  flex-wrap: wrap;
}

.nav-links a {
  font-size: 0.95rem;
  color: #444;
  text-decoration: none;
  transition: color 0.3s ease;
}

.nav-links a:hover {
  color: #ff6b35;
}

.buttons {
  display: flex;
  gap: 0.8rem;
  flex-wrap: wrap;
}

.btn-admin,
.btn-cerrar-sesion {
  padding: 8px 20px;
  border-radius: 50px;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-admin {
  background-color: #ff6b35;
  border: none;
  color: white;
}


.btn-cerrar-sesion {
  background: transparent;
  border: 2px solid #ddd;
  color: #333;
}

.btn-cerrar-sesion:hover {
  background-color: #6d9fef;
  color: #fff;
}

/* ------------------------
   DECORATIVOS
------------------------- */
.img-naranja,
.img-aceite,
.img-guacamole,
.img-estrellas {
  position: fixed;
  object-fit: contain;
  z-index: 10;
  opacity: 0.9;
}

.img-naranja {
  top: 80px;
  left: 40px;
  width: 130px;
}

.img-aceite {
  top: 50px;
  right: 0px;
  width: 150px;
}

.img-guacamole {
  bottom: 0px;
  left: 50px;
  width: 160px;
}

.img-estrellas {
  bottom: 0;
  right: 5px;
  width: 155px;
}

/* ------------------------
   CONTENIDO PRINCIPAL
------------------------- */
.main-content {
  width: min(90%, 1400px); /* ✅ flexible y centrado */
  margin: 0 auto;
  padding-top: 180px;
  text-align: center;
}

.title {
  font-size: clamp(2rem, 2.5vw, 2.8rem);
  font-weight: 800;
  color: #28233b;
  margin-bottom: 40px;
  font-family: "Open Sans", sans-serif;
}

/* ------------------------
   TARJETAS
------------------------- */
.resenas-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 30px;
  justify-content: center;
  padding: 0 1rem;
}

.resena-card {
  background-color: #e8e5b8;
  border-radius: 20px;
  padding: 25px 20px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  text-align: center;
  position: relative;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.resena-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 6px 10px rgba(0, 0, 0, 0.15);
}

.btn-eliminar {
  position: absolute;
  top: 10px;
  right: 10px;
  width: 28px;
  height: 28px;
  border: none;
  border-radius: 50%;
  background: #dc3545;
  color: #fff;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-eliminar:hover {
  background: #c82333;
  transform: scale(1.1);
}

.resena-header {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  margin-bottom: 10px;
}

.emoji {
  width: 40px;
  height: 40px;
}

.nombre-usuario {
  font-size: 1rem;
  font-weight: 700;
  color: #1a1a1a;
}

.resena-texto {
  font-size: 0.9rem;
  color: #333;
  line-height: 1.5;
}

/* ------------------------
   FLECHAS
------------------------- */
.navegacion-flechas {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin-top: 20px;
}

.flecha {
  font-size: 2rem;
  background: none;
  border: none;
  color: #ff6b35;
  cursor: pointer;
  transition: transform 0.3s ease, color 0.3s ease;
}

.flecha:hover:not(:disabled) {
  transform: scale(1.2);
  color: #3b82f6;
}

.flecha:disabled {
  color: #ccc;
  cursor: not-allowed;
}

/* ------------------------
   MEDIA QUERIES
------------------------- */

/* Tablets medianas */
@media (max-width: 992px) {
  .navbar {
    padding: 15px 30px;
  }

  .img-naranja,
  .img-aceite,
  .img-guacamole,
  .img-estrellas {
    width: 90px;
  }
}

/* Tablets y móviles */
@media (max-width: 768px) {
  .navbar {
    flex-direction: column;
    gap: 10px;
  }

  .nav-links {
    justify-content: center;
    gap: 1rem;
  }

  .buttons {
    justify-content: center;
  }

  .main-content {
    padding-top: 180px;
  }

  .title {
    font-size: 1.8rem;
  }

  .resena-card {
    padding: 20px 15px;
  }

  .img-naranja,
  .img-aceite,
  .img-guacamole,
  .img-estrellas {
    display: none;
  }
}

/* Celulares pequeños */
@media (max-width: 480px) {
  .navbar {
    padding: 10px 20px;
  }

  .logo {
    font-size: 1.3rem;
  }

  .resenas-container {
    grid-template-columns: 1fr;
  }

  .btn-admin,
  .btn-cerrar-sesion {
    font-size: 0.8rem;
    padding: 6px 14px;
  }
}
</style>
