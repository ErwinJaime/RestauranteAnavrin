<template>
  <div class="page-container">
    <!-- Navegación -->
    <nav class="navbar">
      <h1 class="logo">ANAVRIN</h1>
      <div class="nav-links">
        <a href="">Home</a>
        <router-link to="/aboutcliente">About</router-link>
        <router-link to="/resenascliente">Review</router-link>
      </div>
      <span class="btn-primary">Tatiana</span>
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
        <img src="@/assets/plato-principal.png" alt="Plato Principal" class="img-plato">
      </div>
    </div>

   <!-- Sección Inferior -->
<div class="bottom-section">
  <div class="review-section">
    <img src="@/assets/hoja-verde.png" alt="Hoja" class="icon-leaf">
    
    <div class="review-content">
      <div class="review-text">
        <img src="@/assets/corazon.png" alt="Corazón" class="icon-heart">
        <h2 class="review-title">
          Tu opinión nos ayuda<br>
          a crecer, comparte tu<br>
          experiencia aquí.
        </h2>
      </div>
      <router-link to="/crearresena" class="btn-review">Crear Reseña</router-link>
    </div>
    
    <img src="@/assets/hoja-verde.png" alt="Hoja" class="icon-leaf">
  </div>

  <!-- Footer -->
  <footer class="footer">
    <div class="footer-bottom">
      <p class="footer-slogan">El encuentro perfecto entre lo auténtico y lo inolvidable</p>
    </div>
  </footer>
</div>

    <!-- Decoraciones -->
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

.btn-primary {
  padding: 8px 28px;
  font-size: 18px;
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

.btn-login {
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

.btn-login:hover {
  background-color: #6d9fef;
  color: rgb(21, 3, 3);
}

/* Contenido Principal */
.main-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0px 80px 60px;
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
  text-decoration: none;
  display: inline-block; 

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
  left: 2px;
  width: 160px;
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
  padding: 0 0px 0;
}

.review-section {
  position: relative;
  padding: 20px 80px 5px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 60px;
}

.review-content {
  display: flex;
  align-items: center;
  gap: 60px;
}

.review-text {
  display: flex;
  align-items: center;
  gap: 130px;
}

.icon-heart {
  width: 90px;
  height: 90px;
  object-fit: contain;
  flex-shrink: 0;
}

.review-title {
  font-size: 36px;
  font-weight: 600;
  color: #2d2a3e;
  line-height: 1.3;
  text-align: left;
  font-family: 'Open Sans', sans-serif;
  margin: 0;
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
  flex-shrink: 0;
  text-decoration: none;
  display: inline-block;
  white-space: nowrap;
}

.btn-review:hover {
  background-color: #ff6b44;
}

.icon-leaf {
  position: absolute;
  width: 80px;
  height: 100px;
  object-fit: contain;
  opacity: 0.6;
}

.icon-leaf:first-of-type {
  left: 80px;
  top: 50%;
  transform: translateY(-50%);
}

.icon-leaf:last-of-type {
  right: 10px;
  top: 50%;
  transform: translateY(10%);
}

/* Media Queries para la sección de reseñas */
@media (min-width: 1440px) {
  .review-section {
    padding: 80px 120px;
  }

  .review-content {
    gap: 80px;
  }

  .review-text {
    gap: 25px;
  }

  .icon-heart {
    width: 70px;
    height: 70px;
  }

  .review-title {
    font-size: 40px;
    line-height: 1.4;
  }

  .btn-review {
    padding: 16px 36px;
    font-size: 15px;
  }

  .icon-leaf {
    width: 90px;
    height: 90px;
  }

  .icon-leaf:first-of-type {
    left: 120px;
  }

  .icon-leaf:last-of-type {
    right: 120px;
  }
}

@media (max-width: 1023px) {
  .review-section {
    padding: 60px 40px;
  }

  .review-content {
    flex-direction: column;
    gap: 30px;
    text-align: center;
  }

  .review-text {
    flex-direction: column;
    align-items: center;
  }

  .review-title {
    text-align: center;
    font-size: 28px;
  }

  .icon-leaf {
    display: none;
  }
}

@media (max-width: 767px) {
  .review-section {
    padding: 40px 20px;
  }

  .review-title {
    font-size: 24px;
  }

  .icon-heart {
    width: 50px;
    height: 50px;
  }

  .btn-review {
    padding: 12px 28px;
    font-size: 13px;
  }
}

/* ==================== FOOTER ==================== */
.footer {
  background: #ffffff;
  padding: 80px 20px 0;
  margin-top: 20px;
  position: relative;
}

.footer-bottom {
  background: #d4e7f7f1;
  padding: 25px 0px;
  text-align: center;
}

.footer-slogan {
  color: #7a7a7a;
  font-size: 0.95rem;
  letter-spacing: 0.3px;
  margin: 0;
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

/* ------------------------
   MEDIA QUERIES
------------------------- */

/* Pantallas grandes (1600px+) */
@media (min-width: 1440px) {
  .page-container {
    max-width: none;
    margin: 0 auto;
  }

  /* Navegación mejorada para 1440px */
  .navbar {
    padding: 25px 5% !important;
    gap: 25px !important;
  }

  .logo {
    font-size: 22px;
    margin-left: 50px;
  }

  .nav-links {
    gap: 70px;
    margin-left: 120px;
  }

  .nav-links a {
    font-size: 15px;
  }

  .btn-primary {
    padding: 10px 32px;
    font-size: 15px;
    margin-right: 15px !important;
  }

  .btn-login {
    padding: 10px 26px;
    font-size: 15px;
  }

  /* Contenido Principal optimizado */
  .main-content {
    padding: 40px 100px 80px;
    gap: 80px;
  }

  .content-left {
    width: 48%;
    padding-left: 50px;
  }

  .title {
    font-size: 74px;
    margin-bottom: 25px;
  }

  .description {
    font-size: 16px;
    margin-bottom: 40px;
    line-height: 1.7;
  }

  .btn-explore {
    padding: 16px 36px;
    font-size: 15px;
  }

  /* Contenido Derecho mejorado */
  .content-right {
    width: 52%;
    height: 650px;
  }

  .img-plato {
    width: 550px;
    height: 550px;
  }

  .img-grapefruit {
    width: 170px;
    height: 150px;
    left: 10px;
  }

  .img-bebida {
    width: 190px;
    height: 190px;
    left: 90px;
    bottom: 30px;
  }

  /* Sección de Reseñas mejorada */
  .bottom-section {
    padding: 0 0px 0;
  }

  .review-section {
    padding: 80px 0;
  }

  .icon-heart {
    width: 70px;
    height: 70px;
    margin-bottom: 25px;
  }

  .review-title {
    font-size: 40px;
    margin-bottom: 35px;
    line-height: 1.4;
  }

  .btn-review {
    padding: 16px 36px;
    font-size: 15px;
  }

  .icon-leaf {
    width: 90px;
    height: 90px;
    right: 120px;
  }

  /* Footer optimizado */
  .footer {
    padding: 0 0 0;
    margin-top:40px;
  }

  .footer-bottom {
    padding: 30px 20px;
  }

  .footer-slogan {
    font-size: 1.05rem;
  }

  /* Decoraciones ajustadas */
  .deco-leaf-1 {
    top: 200px;
    left: 60px;
    width: 110px;
    height: 110px;
  }

  .deco-leaf-2 {
    bottom: 320px;
    right: 80px;
    width: 110px;
    height: 110px;
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

  .btn-primary {
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

  .btn-primary {
    padding: 8px 26px;
    font-size: 12px;
    margin-right: 4px !important;
  }

  .btn-login {
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

  .btn-primary {
    padding: 8px 24px;
    font-size: 13px;
    margin-right: 8px !important;
  }

  .btn-login {
    padding: 8px 18px;
    font-size: 13px;
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

  .btn-primary {
    padding: 7px 20px;
    font-size: 12px;
    margin-right: 8px !important;
  }

  .btn-login {
    padding: 7px 16px;
    font-size: 12px;
  }

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

  .footer {
    padding: 60px 20px 0;
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

  .btn-primary {
    padding: 7px 20px;
    font-size: 12px;
    margin-left: 0 !important;
    margin-right: 5px !important;
  }

  .btn-login {
    padding: 7px 16px;
    font-size: 12px;
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

  .btn-primary,
  .btn-login {
    padding: 6px 16px;
    font-size: 11px;
  }
}
</style>