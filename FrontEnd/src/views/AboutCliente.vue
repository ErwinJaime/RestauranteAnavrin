<template>
  <div class="about-container">
    <!-- Navegación -->
    <nav class="navbar">
      <h1 class="logo">ANAVRIN</h1>
      <div class="nav-links">
        <router-link to="/">Home</router-link>
        <a href="#">About</a>
        <router-link to="/resenascliente">Review</router-link>
      </div>
      <span class="btn-cliente">Tatiana</span>
      <button class="btn-cerrar-sesion" @click="cerrarSesion">Cerrar Sesión</button>
    </nav>

    <!-- Imagen superior -->
    <div class="hero-image">
      <img src="@/assets/planificacion.png" alt="Planificación" />
    </div>

    <!-- Contenido Principal -->
    <div class="main-content">
      <!-- Sección: ¿Quiénes somos? -->
      <section class="quienes-somos">
        <h1 class="title">¿Quiénes somos?</h1>
        <p class="subtitle">
          Anavrin S.A.S. nace con el propósito de transformar la experiencia gastronómica tradicional en un
          encuentro entre la tecnología, el arte culinario y el bienestar.
        </p>

        <!-- Tarjetas naranjas -->
        <div class="cards-container">
          <div class="card card-orange">
            <p>
              Anavrin S.A.S. nace con el propósito de transformar la experiencia gastronómica
              tradicional en un encuentro entre la tecnología, el arte culinario y el
              bienestar.
            </p>
          </div>
          <div class="card card-orange">
            <p>
              El sistema digital de Anavrin permite que cada visitante, mediante una interfaz instalada en las
              mesas del restaurante, pueda acceder al menú, hacer pedidos y compartir reseñas, generando una
              conexión directa entre el cliente y la experiencia gastronómica.
            </p>
          </div>
          <div class="card card-orange">
            <p>
              Anavrin representa la unión entre la pasión por la cocina y la eficiencia
              tecnológica, convirtiéndose en un símbolo de la evolución de la
              restauración moderna.
            </p>
          </div>
        </div>
      </section>

      <!-- Sección: Nuestra historia -->
      <section class="nuestra-historia">
        <h2 class="section-title">Nuestra historia</h2>
        <p class="section-subtitle">
          Aquí comienza una historia que nació lejos de casa, en un viaje por los sabores y tradiciones de Asia.
        </p>

        <!-- Contenido de dos columnas -->
        <div class="historia-content">
          <div class="historia-column">
            <p>
              En 2019, un grupo de emprendedores apasionados por la cocina emprendió un
              recorrido por Japón, Corea, Tailandia y Vietnam, descubriendo que cada plato
              contaba una historia, cada aroma transmitía una emoción y cada comida era una
              experiencia de equilibrio y bienestar.
            </p>
            <p>
              Inspirados por esa filosofía oriental, los fundadores decidieron crear un espacio
              donde la gastronomía se viviera con los cinco sentidos.
            </p>
          </div>
          <div class="historia-column">
            <p>
              Desde su fundación, Anavrin ha buscado ofrecer algo más que un menú: un lugar
              donde la tecnología, el diseño y la calidad se unen para crear una experiencia diferente.
            </p>
            <p>
              Hoy, seguimos innovando con el mismo propósito con el que comenzó este viaje:
              llevar al cliente a un estado de satisfacción plena, donde cada plato cuenta una historia.
            </p>
          </div>
        </div>
      </section>

      <!-- Imagen inferior -->
      <div class="bottom-image">
        <img src="@/assets/viajes.png" alt="Viajes" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const cerrarSesion = () => {
  localStorage.removeItem('usuario')
  localStorage.removeItem('correo')
  sessionStorage.clear()
  router.push('/')
}
</script>

<style scoped>
/* ------------------------
   BASE
------------------------- */
.about-container {
  width: 100%;
  min-height: 100vh;
  background-color: #ffffff;
  position: relative;
  overflow-x: hidden;
}

/* ------------------------
   NAVBAR
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
  color: #3597ff;
}

.btn-cliente {
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
   IMAGEN HERO
------------------------- */
.hero-image {
  width: 100%;
  margin-top: 80px;
  overflow: hidden;
}

.hero-image img {
  width: 100%;
  height: 400px;
  object-fit: cover;
  display: block;
}

/* ------------------------
   CONTENIDO PRINCIPAL
------------------------- */
.main-content {
  max-width: 100%;
  margin: 0 auto;
  padding: 60px 0;
}

/* ------------------------
   QUIÉNES SOMOS
------------------------- */
.quienes-somos {
  text-align: center;
  margin-bottom: 80px;
  padding: 0;
}

.title {
  font-size: 2.8rem;
  font-weight: 800;
  color: #28233b;
  margin-bottom: 20px;
  font-family: "Open Sans", sans-serif;
}

.subtitle {
  font-size: 1.05rem;
  color: #333;
  line-height: 1.6;
  max-width: 900px;
  margin: 0 auto 50px;
}

.cards-container {
  display: flex;
  justify-content: space-between;
  align-items: stretch;
  flex-wrap: nowrap;
  gap: 8px; /* medio cm aprox */
  margin: 0 auto;
  padding: 0;
  width: 100%; /* usa el ancho del contenedor, sin desbordar */
  max-width: 1920px; /* evita que se corte en pantallas grandes */
  box-sizing: border-box;
}


.card {
  flex: 1;
  display: flex; /* permite centrar contenido */
  align-items: center; /* centra verticalmente */
  justify-content: center; /* centra horizontalmente */
  border-radius: 0;
  padding: 40px;
  background-color: #ff6b35;
  color: white;
  text-align: center;
  box-shadow: none;
  margin: 0;
}

.card p {
  margin: 0;
  font-size: 0.95rem;
  line-height: 1.6;
  text-align: center;
}


.card-orange {
  background-color: #ff6b35;
  color: white;
}


/* ------------------------
   NUESTRA HISTORIA
------------------------- */
.nuestra-historia {
  margin-bottom: 60px;
  padding: 0 40px;
}

.section-title {
  font-size: 2.5rem;
  font-weight: 800;
  color: #28233b;
  text-align: center;
  margin-bottom: 20px;
  font-family: "Open Sans", sans-serif;
}

.section-subtitle {
  font-size: 1rem;
  color: #333;
  text-align: center;
  margin-bottom: 50px;
  line-height: 1.6;
}

.historia-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 60px;
  max-width: 800px;
  margin: 0 auto;
}

.historia-column p {
  font-size: 0.95rem;
  color: #333;
  line-height: 1.8;
  text-align: justify;
  margin-bottom: 20px;
}

/* ------------------------
   IMAGEN INFERIOR
------------------------- */
.bottom-image {
  width: 100%;
  margin-top: 20px;
  border-radius: 0;
  overflow: hidden;
}

.bottom-image img {
  width: 100%;
  height: 450px;
  object-fit: cover;
  display: block;
  border-radius: 0;
}

/* ------------------------
   MEDIA QUERIES
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

  .hero-image img {
    height: 450px;
  }

  .card {
    width: 100%;
    height: 220px;
    padding: 0;
  }

  .card p {
    padding: 35px;
  }

  .bottom-image img {
  height: 520px;
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

  .card {
    width: 100%;
    height: 200px;
  }

  .card p {
    padding: 30px;
    font-size: 0.9rem;
  }

  .bottom-image img {
    height: 350px;
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

  .historia-content {
    grid-template-columns: 1fr;
    gap: 30px;
  }

  .cards-container {
    grid-template-columns: 1fr;
    gap: 0;
  }

  .card {
    width: 100%;
    height: 220px;
  }

  .card p {
    padding: 30px;
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

  .main-content {
    padding: 40px 0;
  }

  .quienes-somos {
    padding: 0 20px;
  }

  .nuestra-historia {
    padding: 0 20px;
  }

  .title {
    font-size: 2rem;
  }

  .section-title {
    font-size: 1.8rem;
  }

  .hero-image img {
    height: 200px;
  }

  .bottom-image img {
    height: 280px;
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

  .title {
    font-size: 1.8rem;
  }

  .section-title {
    font-size: 1.6rem;
  }

  .subtitle,
  .section-subtitle {
    font-size: 0.9rem;
  }

  .hero-image img {
    height: 180px;
  }

  .bottom-image img {
    height: 250px;
  }

  .card p,
  .historia-column p {
    font-size: 0.85rem;
  }
}
</style>