<template>
  <div class="resenas-admin-container">
    <!-- Navegación (actualizada desde inventario) -->
    <nav class="navbar">
      <h1 class="logo">ANAVRIN</h1>
      <div class="nav-links">
        <router-link to="/">Home</router-link>
        <router-link to="/about">About</router-link>
        <a href="#">Review</a>
      </div>
      <span class="btn-admin">Admin</span>
      <button class="btn-cerrar-sesion">Cerrar Sesión</button>
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
   NAVBAR (actualizada desde inventario)
------------------------- */
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
  box-shadow: 0 1px 4px rgba(255, 255, 255, 0.05);
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
  color: #35a4ff;
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
  top: 70px;
  left: 40px;
  width: 145px;
}

.img-aceite {
  top: 50px;
  right: 0px;
  width: 140px;
}

.img-guacamole {
  bottom: 0px;
  left: 50px;
  width: 200px;
}

.img-estrellas {
  bottom: 0;
  right: 5px;
  width: 120px;
}

/* ------------------------
   CONTENIDO PRINCIPAL
------------------------- */
.main-content {
  width: min(90%, 1400px);
  margin: 0 auto;
  padding-top: 140px;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  min-height: calc(100vh - 140px);
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
  display: flex;
  flex-wrap: nowrap;
  gap: 30px;
  justify-content: center;
  padding: 0 1rem;
  max-width: 1400px;
  margin: 0 auto;
}

.resena-card {
  background-color: #e8e5b8;
  border-radius: 20px;
  padding: 35px 25px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  text-align: center;
  position: relative;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  width: 350px;
  min-height: 200px;
  flex-shrink: 0;
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
   MEDIA QUERIES (desde inventario)
------------------------- */

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

  .resena-card {
    width: 380px;
    min-height: 220px;
    padding: 40px 30px;
  }

  .resenas-container {
    gap: 40px;
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
    font-size: 12px;
    margin-right: 4px !important;
  }

  .btn-cerrar-sesion {
    padding: 8px 20px;
    font-size: 12px;
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
    padding-top: 140px;
  }

  .resena-card {
    width: 280px;
  }

  .img-naranja,
  .img-aceite,
  .img-guacamole,
  .img-estrellas {
    width: 120px;
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
    padding-top: 130px;
  }

  .resena-card {
    width: 280px;
  }

  .img-naranja,
  .img-aceite,
  .img-guacamole,
  .img-estrellas {
    width: 110px;
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
    margin-left: 0;
  }

  .nav-links {
    gap: 30px;
    width: 100%;
    justify-content: center;
    margin-left: 0;
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

  .img-naranja,
  .img-aceite,
  .img-guacamole,
  .img-estrellas {
    display: none;
  }

  .main-content {
    padding-top: 160px;
  }

  .title {
    font-size: 32px;
  }

  .resenas-container {
    flex-direction: column;
    align-items: center;
    flex-wrap: wrap;
  }

  .resena-card {
    width: 320px;
    max-width: 90%;
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
    padding-top: 170px;
  }

  .title {
    font-size: 28px;
  }

  .resenas-container {
    flex-wrap: wrap;
  }

  .resena-card {
    padding: 20px 15px;
  }
}
</style>