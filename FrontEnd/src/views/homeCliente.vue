<template>
  <div class="page-container">
    <!-- Navegación -->
    <nav class="navbar">
      <h1 class="logo">ANAVRIN</h1>
      <div class="nav-links">
        <a href="">Home</a>
        <a href="/aboutcliente">About</a>
        <a href="/resenascliente">Review</a>
      </div>
      <button class="btn-primary">Tatiana</button>
      <button class="btn-login">Cerrar Sesión</button>
    </nav>

    <!-- Contenido Principal -->
    <div class="main-content">
      <!-- Contenido Izquierdo -->
      <div class="content-left">
        <h1 class="title">Sabores que<br>Enamoran</h1>
        <p class="description">
          Descubre postres, bebidas y platillos<br>
          creados para sorprender cada uno de<br>
          tus sentidos.
        </p>
        <router-link to="/menu" class="btn-explore">Explorar Menú</router-link>
      </div>

      <!-- Contenido Derecho - Imágenes -->
      <div class="content-right">
        <img src="@/assets/grapefruit.png" alt="Grapefruit" class="img-grapefruit">
        <img src="@/assets/plato-principal.png" alt="Plato Principal" class="img-plato">
      </div>
    </div>

    <!-- Sección Inferior -->
    <div class="bottom-section">
      <div class="review-section">
        <img src="@/assets/corazon.png" alt="Corazón" class="icon-heart">
        <h2 class="review-title">
          Tu opinión nos ayuda<br>
          a crecer, comparte tu<br>
          experiencia aquí.
        </h2>
        <router-link to="/crearresena" class="btn-review">Crear Reseña</router-link>
        <img src="@/assets/hoja-verde.png" alt="Hoja" class="icon-leaf">
      </div>

      <div class="footer-banner">
        <p class="footer-text">El encuentro perfecto entre lo auténtico y lo inolvidable</p>
      </div>
    </div>

    <!-- Decoraciones -->
    <img src="@/assets/hoja-verde.png" alt="Hoja" class="deco-leaf deco-leaf-1">
    <img src="@/assets/hoja-verde.png" alt="Hoja" class="deco-leaf deco-leaf-2">
  </div>
</template>

<script>
export default {
  name: 'HomePage'
}
</script>

<style scoped>

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.page-container {
  width: 100%;
  min-height: 100vh;
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
  align-items: center;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
}

.logo {
  font-size: 20px;
  font-weight: 600;
  color: #1a1a1a;
  letter-spacing: 1px;
}

.nav-links {
  display: flex;
  gap: 50px;
  margin-left: auto;
  margin-right: auto;
}

.nav-links a {
  font-size: 14px;
  color: #666;
  text-decoration: none;
  font-family: 'Montserrat', sans-serif;
}

.nav-links a:hover {
  color: #000;
}

.btn-primary {
  padding: 10px 28px;
  font-size: 14px;
  color: #ffffff;
  background-color: #ff7b54;
  border: none;
  border-radius: 50px;
  cursor: pointer;
  font-family: 'Montserrat', sans-serif;
  margin-right: 12px;
}

.btn-primary:hover {
  background-color: #ff6b44;
}

.btn-login {
  padding: 10px 24px;
  font-size: 14px;
  color: #070707;
  border: 1px solid #ddd;
  background-color: transparent;
  border-radius: 50px;
  cursor: pointer;
  font-family: 'Montserrat', sans-serif;
}

.btn-login:hover {
  background-color: #f5f5f5;
}

/* Contenido Principal */
.main-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 140px 80px 60px;
  min-height: calc(100vh - 200px);
  gap: 60px;
}

.content-left {
  width: 45%;
  padding-left: 40px;
}

.title {
  font-size: 68px;
  font-weight: 700;
  color: #2d2a3e;
  line-height: 1.1;
  margin-bottom: 20px;
  font-family: 'Open Sans', sans-serif;
}

.description {
  font-size: 15px;
  color: #666;
  line-height: 1.6;
  margin-bottom: 35px;
  font-family: 'Montserrat', sans-serif;
}

.btn-explore {
  padding: 14px 32px;
  font-size: 14px;
  color: #ffffff;
  background-color: #ff7b54;
  border: none;
  border-radius: 50px;
  cursor: pointer;
  font-family: 'Montserrat', sans-serif;
  font-weight: 500;
}

.btn-explore:hover {
  background-color: #ff6b44;
}

/* Contenido Derecho - Imágenes */
.content-right {
  width: 55%;
  position: relative;
  height: 600px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.img-grapefruit {
  position: absolute;
  top: 0;
  left: -20px;
  width: 140px;
  height: 140px;
  object-fit: contain;
  z-index: 10;
}

.img-plato {
  position: relative;
  width: 500px;
  height: 500px;
  object-fit: contain;
  z-index: 5;
}

.img-bebida {
  position: absolute;
  bottom: 20px;
  left: 80px;
  width: 180px;
  height: 180px;
  object-fit: contain;
  z-index: 10;
}

/* Sección Inferior */
.bottom-section {
  position: relative;
  padding: 0 80px 0;
}

.review-section {
  position: relative;
  text-align: center;
  padding: 60px 0;
}

.icon-heart {
  width: 60px;
  height: 60px;
  margin-bottom: 20px;
  object-fit: contain;
}

.review-title {
  font-size: 36px;
  font-weight: 600;
  color: #2d2a3e;
  line-height: 1.3;
  margin-bottom: 30px;
  font-family: 'Open Sans', sans-serif;
}

.btn-review {
  padding: 14px 32px;
  font-size: 14px;
  color: #ffffff;
  background-color: #ff7b54;
  border: none;
  border-radius: 50px;
  cursor: pointer;
  font-family: 'Montserrat', sans-serif;
  font-weight: 500;
}

.btn-review:hover {
  background-color: #ff6b44;
}

.icon-leaf {
  position: absolute;
  right: 100px;
  top: 50%;
  transform: translateY(-50%);
  width: 80px;
  height: 80px;
  object-fit: contain;
  opacity: 0.6;
}

.footer-banner {
  background-color: #e8f4f8;
  padding: 20px;
  text-align: center;
}

.footer-text {
  font-size: 14px;
  color: #333;
  font-family: 'Montserrat', sans-serif;
}

/* Decoraciones */
.deco-leaf {
  position: absolute;
  width: 100px;
  height: 100px;
  object-fit: contain;
  opacity: 0.5;
}

.deco-leaf-1 {
  top: 180px;
  left: 40px;
}

.deco-leaf-2 {
  bottom: 280px;
  right: 60px;
}

/* Responsive */
@media (max-width: 1024px) {
  .main-content {
    flex-direction: column;
    padding: 120px 40px 40px;
    text-align: center;
  }

  .content-left,
  .content-right {
    width: 100%;
  }

  .content-left {
    padding-left: 0;
  }

  .title {
    font-size: 48px;
  }

  .content-right {
    height: 400px;
  }

  .img-plato {
    width: 350px;
    height: 350px;
  }

  .img-grapefruit {
    width: 100px;
    height: 100px;
  }

  .img-bebida {
    width: 130px;
    height: 130px;
  }

  .review-title {
    font-size: 28px;
  }
}
</style>
