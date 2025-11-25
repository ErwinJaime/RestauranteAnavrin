<template>
  <div class="page-container">
    <!-- Sección 1 - Home: Sabores que Enamoran -->
    <section id="section1" class="section">
      <div class="container">
        <!-- Navegación -->
        <nav class="navbar">
          <h1 class="logo">ANAVRIN</h1>
          <div class="nav-links">
            <a href="/home">Home</a>
            <a href="/abouthome">About</a>
            <a href="/resenashome">Review</a>
          </div>
          <button class="btn-login">Iniciar Sesión</button>
        </nav>
        
        <!-- Contenido Sección 1 -->
        <section class="section-one">
          <div class="content-left">
            <h1 class="title">Sabores que<br>Enamoran</h1>
            <p class="description">
              Descubre postres, bebidas y platillos<br>
              creados para sorprender cada uno de<br>
              tus sentidos.
            </p>
            <img src="@/assets/hoja2.png" alt="Hoja" class="hoja-decoration">
          </div>

          <div class="content-right">
            <img src="@/assets/grapefruit.png" alt="Grapefruit" class="img-grapefruit">
            <img src="@/assets/plato-principal.png" alt="Plato Principal" class="img-plato">
          </div>
        </section>
      </div>
    </section>

    <!-- Sección 2 - Home2: Una Experiencia de Sabores -->
    <section id="section2" class="section section-two">
      <div class="container">
        <nav class="navbar">
          <h1 class="logo">ANAVRIN</h1>
          <div class="nav-links">
            <a href="/home">Home</a>
            <a href="/abouthome">About</a>
            <a href="/resenashome">Review</a>
          </div>
          <button class="btn-login">Iniciar Sesión</button>
        </nav>

        <div class="section-content">
          <h2 class="section-title-center">Una Experiencia de Sabores</h2>
          <p class="section-subtitle">Cada plato cuenta una historia: recetas únicas que combinan tradición e innovación.</p>
          
          <div class="cards-container">
            <div class="card">
              <div class="card-image">
                <img src="@/assets/bebida.png" alt="Bebidas" class="card-img">
              </div>
              <h3 class="card-title">Bebidas</h3>
              <p class="card-description">La frescura de la fruta natural en cada sorbo.</p>
            </div>

            <div class="card">
              <div class="card-image">
                <img src="@/assets/postre.png" alt="Postres" class="card-img">
              </div>
              <h3 class="card-title">Postres</h3>
              <p class="card-description">Un clásico reinventado, con sabores que despiertan emociones.</p>
            </div>

            <div class="card">
              <div class="card-image">
                <img src="@/assets/platillo.png" alt="Platillos" class="card-img">
              </div>
              <h3 class="card-title">Platillos</h3>
              <p class="card-description">Ingredientes frescos y un toque gourmet para tu paladar.</p>
            </div>
          </div>
        </div>

        <!-- Decoraciones -->
        <img src="@/assets/hoja-verde.png" alt="Hoja" class="deco-leaf deco-leaf-2">
        <img src="@/assets/arandanos.png" alt="Arándanos" class="deco-berries">
        <img src="@/assets/harina.png" alt="Harina" class="deco-flour">
      </div>
    </section>

    <!-- Sección 3 - Home3: Sabores del Mundo -->
    <section id="section3" class="section section-three">
      <div class="container">
        <nav class="navbar">
          <h1 class="logo">ANAVRIN</h1>
          <div class="nav-links">
            <a href="/home">Home</a>
            <a href="/abouthome">About</a>
            <a href="/resenashome">Review</a>
          </div>
          <button class="btn-login">Iniciar Sesión</button>
        </nav>

        <div class="section-content-three">
          <div class="content-left-three">
            <h2 class="section-title-three">Sabores del Mundo<br>en un Solo Lugar</h2>
            <p class="section-description-three">
              De Europa a América Latina, de Asia al<br>
              Mediterráneo. Nuestra cocina es un viaje por<br>
              distintas culturas.
            </p>
          </div>

          <div class="content-right-three">
            <img src="@/assets/plato-chocolate.png" alt="Plato de Chocolate" class="img-plato-three">
          </div>

          <div class="footer-banner">
            <p class="footer-text">El encuentro perfecto entre lo auténtico y lo inolvidable</p>
          </div>
        </div>

        <!-- Decoraciones Sección 3 -->
        <img src="@/assets/hoja-verde.png" alt="Hoja" class="deco-leaf-three deco-leaf-three-1">
        <img src="@/assets/hoja2.png" alt="Hoja" class="deco1-leaf-three deco1-leaf-three-1">
        <img src="@/assets/huevos.png" alt="Huevos" class="deco-eggs">
        <img src="@/assets/especias.png" alt="Especias" class="deco-spices">
        <img src="@/assets/cuchara.png" alt="Cuchara" class="deco-spoon"> 
      </div>
    </section>
  </div>
</template>

<script>

export default {
  name: 'HomePage',
  setup() {
    const scrollToSection = (sectionId) => {
      const element = document.getElementById(sectionId)
      if (element) {
        element.scrollIntoView({ 
          behavior: 'smooth',
          block: 'start'
        })
      }
    }

    return {
      scrollToSection
    }
  },
  mounted() {
    // Agregar clase visible a la primera sección al cargar
    const firstSection = document.querySelector('.section:first-child')
    if (firstSection) {
      firstSection.classList.add('visible')
    }

    // Observer para animar elementos al hacer scroll
    const observerOptions = {
      threshold: 0.3,
      rootMargin: '0px'
    }

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          // Agregar clase cuando entra en la vista
          entry.target.classList.add('visible')
        } else {
          // Quitar clase cuando sale de la vista
          entry.target.classList.remove('visible')
        }
      })
    }, observerOptions)

    // Observar todas las secciones
    const sections = document.querySelectorAll('.section')
    sections.forEach(section => {
      observer.observe(section)
    })
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400&display=swap');

/* Page Container con Scroll Suave */
.page-container {
  width: 100%;
  height: 100vh;
  overflow-y: scroll;
  overflow-x: hidden;
  scroll-behavior: smooth;
  scroll-snap-type: y mandatory;
}

/* Cada Sección */
.section {
  min-height: 100vh;
  scroll-snap-align: start;
  scroll-snap-stop: always;
  position: relative;
}

/* General */
.container {
  width: 100%;
  height: 100vh;
  background-color: #ffffff;
  overflow: hidden;
  overflow-x: hidden;
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
  justify-content: flex-start;
  margin-left: 350px;
}

.nav-links a {
  font-size: 14px;
  color: #666;
  text-decoration: none;
  transition: color 0.3s ease;
  white-space: nowrap;
}

.nav-links a:hover {
  color: #6d9fef;
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
  margin-right: -170px;
  font-weight: 600;
  white-space: nowrap;
  flex-shrink: 0;
}

.btn-login:hover {
  background-color: #6d9fef;
  color: rgb(7, 7, 7);
}

/* Sección 1 HOME  */
.section-one {
  min-height: 100vh;
  max-height: 100vh;
  display: flex;
  align-items: center;
  padding-top: 200px;
  padding-left: 10px;
  padding-right: 80px;
  gap: 80px;
  overflow: hidden;
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
  color: #1a181f;
  line-height: 1.0;
  margin-bottom: 9px;
  margin-bottom: 10px;
  font-family: 'Open Sans', sans-serif;
  opacity: 0;
  transform: translateX(-100px);
  transition: all 1.2s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}

.section:first-child.visible .title {
  opacity: 1;
  transform: translateX(0);
}

.description {
  font-size: 15px;
  color: #666;
  line-height: 1.3;
  margin-bottom: 30px;
  font-weight: 400;
  font-family: 'Montserrat', sans-serif;
  opacity: 0;
  transform: translateX(-50px);
  transition: all 0.8s ease-out 0.2s;
}

.section:first-child.visible .description {
  opacity: 1;
  transform: translateX(0);
}

.hoja-decoration {
  width: 150px;
  height: 150px;
  object-fit: contain;
  margin-bottom: 45px;
  margin-left: 100px;
  display: block;
  opacity: 0;
  transform: scale(0.5) rotate(180deg);
  transition: all 1s ease-out 0.4s;
} 

.section:first-child.visible .hoja-decoration {
  opacity: 1;
  transform: scale(1) rotate(0deg);
}

/* Contenido Derecho - Imágenes */
.content-right {
  width: 50%;
  position: relative;
  height: 500px;
}

.img-grapefruit {
  position: absolute;
  top: 80px;
  left: 30px;
  width: 160px;
  height: 160px;
  object-fit: contain;
  z-index: 10;
  opacity: 0;
  transform: translate(-80px, -80px);  
  transition: all 1.2s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}

.section:first-child.visible .img-grapefruit {
  opacity: 1;
  transform: translate(0, 0);
}

.img-plato {
  position: absolute;
  top: 40%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 500px;
  height: 450px;
  object-fit: contain;
  opacity: 0;
  transform: translate(-50%, calc(-50% + 100px)); 
  transition: all 1.5s cubic-bezier(0.25, 0.46, 0.45, 0.94) 0.3s;
}

.section:first-child.visible .img-plato {
  opacity: 1;
  transform: translate(-50%, -50%);
}

/* ========== SECCIÓN 2 - HOME2 ========== */
.section-two {
  background-color: #f8f9fa;
}

.section-content {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 100px 80px 60px; 
}

.section-title-center {
  font-size: 48px;
  font-weight: 700;
  top: 25%;
  color: #1a181f;
  text-align: center;
  margin-bottom: 15px;
  font-family: 'Open Sans', sans-serif;
  opacity: 0;
  transform: translateY(-50px);
  transition: all 1.2s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}

.section-two.visible .section-title-center {
  opacity: 1;
  transform: translateY(0);
}

.section-subtitle {
  font-size: 15px;
  color: #666;
  text-align: center;
  margin-bottom: 30px;
  font-family: 'Montserrat', sans-serif;
  opacity: 0;
  transform: translateY(-40px);
  transition: all 1.2s cubic-bezier(0.25, 0.46, 0.45, 0.94) 0.2s;
}

.section-two.visible .section-subtitle {
  opacity: 1;
  transform: translateY(0);
}

.cards-container {
  display: flex;
  justify-content: center;
  gap: 50px;
  margin-bottom: 50px;
  max-width: 1200px;
}

.card {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  opacity: 0;
  transform: scale(0.5) rotate(60deg);
  transition: all 1.2s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}

.card:nth-child(1) {
  transition-delay: 0.2s;
}

.card:nth-child(2) {
  transition-delay: 0.4s;
}

.card:nth-child(3) {
  transition-delay: 0.6s;
}

.section-two.visible .card {
  opacity: 1;
  transform: translateY(0) rotate(0deg);
}

.card-image {
  width: 200px;
  height: 200px;
  border-radius: 50%;
  overflow: hidden;
  margin-bottom: 20px;
  background-color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
}

.card-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.card-title {
  font-size: 22px;
  font-weight: 600;
  color: #1a181f;
  margin-bottom: 10px;
  font-family: 'Open Sans', sans-serif;
}

.card-description {
  font-size: 14px;
  color: #666;
  max-width: 250px;
  font-family: 'Montserrat', sans-serif;
  line-height: 1.4;
}

/* Decoraciones Sección 2 */
.deco-leaf {
  position: absolute;
  width: 80px;
  height: 80px;
  object-fit: contain;
  opacity: 0;
  transition: all 1.2s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}

.section-two.visible .deco-leaf {
  opacity: 1;
}

.deco-leaf-2 {
  top: 400px;
  bottom: 150px;
  right: 70px;
  transform: translate(60px, 60px);
}

.section-two.visible .deco-leaf-2 {
  transform: translate(0, 0);
}

.deco-berries {
  position: absolute;
  width: 300px;
  height: 300px;
  object-fit: contain;
  top: 110px;
  left: -92px;
  opacity: 0;
  transform: translate(-50px, -50px);
  transition: all 1.2s cubic-bezier(0.25, 0.46, 0.45, 0.94) 0.3s;
}

.section-two.visible .deco-berries {
  opacity: 1;
  transform: translate(0, 0);
}

.deco-flour {
  position: absolute;
  width: 120px;
  height: 120px;
  object-fit: contain;
  top: 80px;
  right: 10px;
  opacity: 0;
  transform: translate(50px, -50px);
  transition: all 1.2s cubic-bezier(0.25, 0.46, 0.45, 0.94) 0.4s;
}

.section-two.visible .deco-flour {
  opacity: 1;
  transform: translate(0, 0);
}

/* ========== SECCIÓN 3 - HOME3 ========== */
.section-three {
  background-color: #ffffff;
}

.section-content-three {
  min-height: 100vh;
  display: flex;
  align-items: center;
  padding: 140px 90px 90px;
  position: relative;
}

.content-left-three {
  width: 45%;
  padding-left: 100px;
  margin-top: -40px; 
}

.section-title-three {
  font-size: 52px;
  font-weight: 700;
  color: #1a181f;
  line-height: 1.1;
  margin-bottom: 20px;
  margin-top: -20px;
  font-family: 'Open Sans', sans-serif;
  opacity: 0;
  transform: translateX(-100px);
  transition: all 1.2s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}

.section-three.visible .section-title-three {
  opacity: 1;
  transform: translateX(0);
}

.section-description-three {
  font-size: 15px;
  color: #666;
  line-height: 1.5;
  font-family: 'Montserrat', sans-serif;
  opacity: 0;
  transform: translateX(-100px);
  transition: all 1.2s cubic-bezier(0.25, 0.46, 0.45, 0.94) 0.2s;
}

.section-three.visible .section-description-three {
  opacity: 1;
  transform: translateX(0);
}

.content-right-three {
  width: 55%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.img-plato-three {
  width: 500px;
  height: 500px;
  top: 40%;
  object-fit: contain;
  opacity: 0;
  transform: translateX(100px) rotate(-70deg);
  transition: all 1.5s cubic-bezier(0.25, 0.46, 0.45, 0.94) 0.3s;
}

.section-three.visible .img-plato-three {
  opacity: 1;
  transform: translateX(0) translateY(-70px) ; 
}

.footer-banner {
  position: absolute;
  bottom: 100px;
  left: 0;
  right: 0;
  background-color: #daeef5;
  padding: 20px;
  text-align: center;
}

.footer-text {
  font-size: 14px;
   font-weight: 600;
  color: #696363;
  font-family: 'Montserrat', sans-serif;
}

/* Decoraciones Sección 3 */
.deco-leaf-three {
  position: absolute;
  width: 67px;
  height: 67px;
  object-fit: contain;
  opacity: 0;
  transform: translate(-40px, -40px);
  transition: all 1.2s cubic-bezier(0.25, 0.46, 0.45, 0.94) 0.3s;
}

.section-three.visible .deco-leaf-three {
  opacity: 1;
  transform: translate(0, 0);
}

.deco-leaf-three-1 {
  top: 80px;
  left: 350px;
}

.deco1-leaf-three {
  position: absolute;
  width: 67px;
  height: 67px;
  object-fit: contain;
  opacity: 0;
  transform: translate(-40px, -40px);
  transition: all 1.2s cubic-bezier(0.25, 0.46, 0.45, 0.94) 0.3s;
}

.section-three.visible .deco1-leaf-three {
  opacity: 1;
  transform: translate(0, 0);
}

.deco1-leaf-three-1 {
  top: 400px;
  left: 300px;
}

.deco-eggs {
  position: absolute;
  width: 270px;
  height: 270px;
  object-fit: contain;
  bottom: 250px;
  left: -84px;
  opacity: 0;
  transform: translate(-50px, 50px);
  transition: all 1.2s cubic-bezier(0.25, 0.46, 0.45, 0.94) 0.5s;
}

.section-three.visible .deco-eggs {
  opacity: 1;
  transform: translate(0, 0);
}

.deco-spices {
  position: absolute;
  width: 140px;
  height: 140px;
  object-fit: contain;
  bottom: 60px;
  left: 2px;
  opacity: 0;
  transform: translate(-40px, 50px);
  transition: all 1.2s cubic-bezier(0.25, 0.46, 0.45, 0.94) 0.6s;
}

.section-three.visible .deco-spices {
  opacity: 1;
  transform: translate(0, 0);
}

.deco-spoon {
  position: absolute;
  width: 280px;  
  height: 280px;
  object-fit: contain;
  bottom: 60px;  
  left: 560px;   
  opacity: 0;
  transform: translate(-50px, 50px) rotate(-30deg);  
  transition: all 1.2s cubic-bezier(0.25, 0.46, 0.45, 0.94) 0.7s;
}

.section-three.visible .deco-spoon {
  opacity: 1;
  transform: translate(0, 0) rotate(0deg);  /* Vuelve a su rotación normal */
}

/* ===== RESPONSIVE DESIGN ===== */

/* Pantallas grandes (1600px+) */
@media (min-width: 1600px) {
  .navbar {
    padding: 20px 100px;
  }

  .logo {
    font-size: 24px;
    margin-left: 80px;
  }

  .nav-links {
    gap: 80px;
  }

  .nav-links a {
    font-size: 16px;
  }

  .btn-login {
    padding: 12px 28px;
    font-size: 15px;
    margin-right: -180px;
  }

  .section-one {
    padding-top: 220px;
    padding-left: 20px;
    padding-right: 100px;
    gap: 100px;
  }

  .content-left {
    padding-left: 180px;
  }

  .title {
    font-size: 75px;
  }

  .description {
    font-size: 17px;
    margin-bottom: 35px;
  }

  .hoja-decoration {
    width: 170px;
    height: 170px;
    margin-left: 120px;
  }

  .img-grapefruit {
    width: 180px;
    height: 180px;
    top: 90px;
    left: 40px;
  }

  .img-plato {
    width: 550px;
    height: 500px;
  }
  
  .section-title-center {
    font-size: 32px;
  }

  .section-title-three {
    font-size: 34px;
  }

  .img-plato-three {
    width: 280px;
    height: 280px;
  }

}

/* Pantallas medianas-grandes (1367px - 1599px) */
@media (min-width: 1367px) and (max-width: 1599px) {
  .navbar {
    padding: 20px 90px;
  }

  .logo {
    font-size: 23px;
    margin-left: 78px;
  }

  .nav-links {
    gap: 70px;
  }

  .nav-links a {
    font-size: 15px;
  }

  .btn-login {
    padding: 11px 26px;
    font-size: 14px;
    margin-right: -170px;
  }

  .section-one {
    padding-top: 210px;
    padding-left: 15px;
    padding-right: 90px;
    gap: 90px;
  }

  .content-left {
    padding-left: 170px;
  }

  .title {
    font-size: 70px;
  }

  .description {
    font-size: 16px;
  }

  .hoja-decoration {
    width: 160px;
    height: 160px;
    margin-left: 110px;
  }

  .img-grapefruit {
    width: 170px;
    height: 170px;
    top: 85px;
    left: 35px;
  }

  .img-plato {
    width: 520px;
    height: 470px;
  }

  .section-title-center {
    font-size: 52px;
  }

  .section-title-three {
    font-size: 56px;
  }
}

/* Pantallas medianas (1280px - 1366px) */
@media (min-width: 1280px) and (max-width: 1366px) {
  .navbar {
    padding: 20px 70px;
  }

  .logo {
    font-size: 19px;
    margin-left: 30px;
  }

  .nav-links {
    gap: 60px;
  }

  .nav-links a {
    font-size: 14px;
  }

  .btn-login {
    padding: 7px 20px;
    font-size: 12px;
    margin-right: 15px !important;
  }

  .section-one {
    padding-top: 280px;
    padding-left: 10px;
    padding-right: 70px;
    gap: 60px;
    max-height: 100vh; 
  }

  .content-left {
    padding-left: 220px;
  }

  .title {
    font-size: 60px;
    color: #2e293c;
  }

  .description {
    font-size: 15px;
  }

  .hoja-decoration {
    width: 90px;
    height: 140px;
    margin-left: 200px;
  }

  .img-grapefruit {
    width: 155px;
    height: 155px;
    top: -80px;
    left: -600px;
  }

  .img-plato {
    top: 25%;
    width: 480px;
    height: 430px;
  }

  .section-title-center {
    font-size: 45px;
  }

  .cards-container {
    gap: 35px;
  }

  .card-image {
    width: 180px;
    height: 180px;
  }

  .section-title-three {
    font-size: 40px;
    margin-top: -100px;
  }

  .img-plato-three {
    width: 420px;
    height: 420px;
  }
}

/* Pantallas pequeñas de laptop (1024px - 1279px) */
@media (min-width: 1024px) and (max-width: 1279px) {
  .navbar {
    padding: 18px 50px;
  }

  .logo {
    font-size: 20px;
    margin-left: 40px;
  }

  .nav-links {
    gap: 50px;
  }

  .nav-links a {
    font-size: 13px;
  }

  .btn-login {
    padding: 9px 22px;
    font-size: 13px;
    margin-right: -120px;
  }

  .section-one {
    padding-top: 150px;
    padding-left: 5px;
    padding-right: 50px;
    gap: 40px;
  }

  .content-left {
    padding-left: 100px;
  }

  .title {
    color: #1a181f;
    font-size: 55px;
  }

  .description {
    font-size: 14px;
    margin-bottom: 25px;
  }

  .hoja-decoration {
    width: 130px;
    height: 130px;
    margin-left: 70px;
    margin-bottom: 18px;
  }

  .img-grapefruit {
    width: 140px;
    height: 140px;
    top: 75px;
    left: 22px;
  }

  .img-plato {
    width: 420px;
    height: 380px;
  }

  .section-title-center {
    font-size: 40px;
  }

  .cards-container {
    gap: 30px;
  }

  .card-image {
    width: 160px;
    height: 160px;
  }

  .section-title-three {
    font-size: 42px;
  }

  .content-left-three {
    padding-left: 60px;
  }

  .img-plato-three {
    width: 400px;
    height: 400px;
  }
}

/* Tablets (768px - 1023px) */
@media (max-width: 1023px) {
  .navbar {
    padding: 16px 35px;
  }

  .logo {
    font-size: 19px;
    margin-left: 20px;
  }

  .nav-links {
    gap: 40px;
  }

  .nav-links a {
    font-size: 13px;
  }

  .btn-login {
    padding: 8px 20px;
    font-size: 12px;
    margin-right: -100px;
  }

  .section-one {
    flex-direction: column;
    padding-top: 140px;
    padding-left: 20px;
    padding-right: 20px;
    gap: 40px;
    text-align: center;
  }

  .content-left {
    width: 100%;
    padding-left: 0;
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .title {
    font-size: 48px;
  }

  .description {
    font-size: 14px;
    margin-bottom: 20px;
  }

  .hoja-decoration {
    width: 110px;
    height: 110px;
    margin-left: 0;
    margin-bottom: 15px;
  }

  .content-right {
    width: 100%;
    height: 400px;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .img-grapefruit {
    position: absolute;
    top: 120px;
    left: 20px;
    width: 110px;
    height: 110px;
  }

  .img-plato {
    position: relative;
    width: 350px;
    height: 320px;
    top: auto;
    left: auto;
    transform: none;
  }
  .section-title-center {
    font-size: 36px;
  }

  .cards-container {
    flex-direction: column;
    gap: 40px;
  }

  .section-content-three {
    flex-direction: column;
    padding: 140px 40px 100px;
  }

  .content-left-three {
    width: 100%;
    padding-left: 0;
    text-align: center;
    margin-bottom: 40px;
  }

  .content-right-three {
    width: 100%;
  }

  .section-title-three {
    font-size: 38px;
  }

  .img-plato-three {
    width: 350px;
    height: 350px;
  }
}

/* Tablets pequeñas (600px - 767px) */
@media (max-width: 767px) {
  .navbar {
    padding: 15px 20px;
    flex-wrap: wrap;
    justify-content: center;
    gap: 15px;
  }

  .logo {
    font-size: 18px;
    width: 100%;
    text-align: center;
    margin-left: 0;
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

  .btn-login {
    padding: 7px 18px;
    font-size: 12px;
    margin-right: 0;
  }
  
  .section-one {
    padding-top: 160px;
    padding-left: 15px;
    padding-right: 15px;
    gap: 30px;
  }

  .title {
    font-size: 40px;
  }

  .description {
    font-size: 13px;
  }

  .hoja-decoration {
    width: 100px;
    height: 100px;
  }

  .img-grapefruit {
    width: 90px;
    height: 90px;
    top: 130px;
    left: 15px;
  }

  .img-plato {
    width: 300px;
    height: 270px;
  }

  .content-right {
    height: 320px;
  }
}
</style>