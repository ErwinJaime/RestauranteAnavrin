<template>
  <div class="platillos-page">
    <!-- Navegación -->
    <nav class="navbar">
      <h1 class="logo">ANAVRIN</h1>
      <div class="nav-links"> 
        <router-link to="/">Home</router-link>
        <router-link to="/abouthome">About</router-link>
        <router-link to="/resenashome">Review</router-link>
      </div>
      <button class="btn-login">Iniciar Sesión</button>
    </nav>

    <!-- Contenido Principal -->
    <div class="main-content">
       <!-- Lado Derecho - Imagen Principal -->
      <div class="content-left">
        <transition name="dish-rotate" mode="out-in">
          <div :key="currentDish.id" class="dish-image-container">
            <img 
              :src="currentDish.mainImage" 
              :alt="currentDish.title" 
              class="dish-main-image"
            >
          </div>
        </transition>
      </div>

      <!-- Lado Derecho - Info del Platillo -->
      <div class="content-right">
        <!-- Tarjetas de Platillos -->
        <div class="dishes-grid">
          <div 
            v-for="dish in dishes" 
            :key="dish.id"
            @click="changeDish(dish.id)"
            class="dish-card"
            :class="{ 'swapping': isSwapping && clickedId === dish.id }"
          >
            <!-- Imagen redonda flotando arriba -->
            <div class="dish-thumb-container">
              <img :src="dish.thumbnailImage" :alt="dish.title" class="dish-thumb-img">
            </div>
          </div>
        </div>

        <transition name="fade-slide" mode="out-in">
          <div :key="currentDish.id" class="dish-info">
            <h1 class="dish-title">{{ currentDish.title }}</h1>
            <p class="dish-description">{{ currentDish.description }}</p>
            <div class="price-tag">{{ currentDish.price }}</div>
          </div>
        </transition>
      </div>
    </div>
  </div>
</template>


<script>
import { ref } from 'vue'

export default {
  name: 'PlatillosPage',
  setup() {
    const dishes = ref([
      {
        id: 1,
        title: 'Pastel de Fresas con Crema',
        description: 'Bizcocho de vainilla esponjoso, relleno de crema batida fresca, fresas en láminas, cobertura ligera de azúcar glas y decoración con cerezas.',
        price: '14.500 COP',
        mainImage: require('@/assets/Pastel-de-Fresas.png'),
        thumbnailImage: require('@/assets/Pastel-de-Fresas1.png'),
        bgColor: '#FFE7BC',
        cardBgColor: '#FFE7BC'
      },
      {
        id: 2,
        title: 'Cheesecake de Arándanos',
        description: 'Base de galleta triturada, relleno cremoso de queso crema, coulis de arándanos naturales y uvas negras como decoración.',
        price: '16.000 COP',
        mainImage: require('@/assets/Cheesecake.png'),
        thumbnailImage: require('@/assets/Cheesecake1.png'),
        bgColor: '#FFCCA6',
        cardBgColor: '#FFCCA6'
      },
      {
        id: 3,
        title: 'Torta de Naranja con Chocolate',
        description: 'Bizcocho de naranja húmedo, capas de chocolate semiamargo, cobertura de virutas de chocolate y decoración con ralladura de cítricos.',
        price: '13.800 COP',
        mainImage: require('@/assets/Torta-de-Naranja.png'),
        thumbnailImage: require('@/assets/Torta-de-Naranja1.png'),
        bgColor: '#B4FF9B',
        cardBgColor: '#B4FF9B'
      }
    ])

    const currentDish = ref(dishes.value[0])
    const isSwapping = ref(false)
    const clickedId = ref(null)

    const changeDish = (dishId) => {
      if (isSwapping.value || currentDish.value.id === dishId) return
      
      isSwapping.value = true
      clickedId.value = dishId
      
      const selected = dishes.value.find(d => d.id === dishId)
      
      setTimeout(() => {
        currentDish.value = selected
        setTimeout(() => {
          isSwapping.value = false
          clickedId.value = null
        }, 2000)
      }, 100)
    }

    return {
      dishes,
      currentDish,
      isSwapping,
      clickedId,
      changeDish
    }
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Source+Serif+Pro:wght@400;600;700&display=swap'); 

/* Page Container */
.platillos-page {
  width: 100%;
  height: 100vh;  
  background-color: #ffffff;
  overflow: hidden;  
  display: flex;
  flex-direction: column;
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

/* Contenido Principal */
.main-content {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px 100px 10px; 
  min-height: 0;
  gap: 80px;
}

/* Lado Izquierdo */
.content-left {
  width: 55%;
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
}

.dish-info {
  width: 100%;
  animation: fadeInLeft 0.8s ease-out;
}

.dish-title {
  font-size: 32px;
  font-weight: 700;
  color: #1a1a1a;
  line-height: 1.2;
  margin-bottom: 15px;
  font-family: 'Open Sans', sans-serif;
}

.dish-description {
  font-size: 14px;
  color: #666;
  line-height: 1.6;
  margin-bottom: 25px;
  font-family: 'Montserrat', sans-serif;
  max-width: 450px;
}

.price-tag { /* etiqueta precio */
  display: inline-block;
  padding: 12px 50px;
  font-size: 16px;
  font-weight: 600;
  color: #ffffff;
  background-color: #7C0000;
  border-bottom-right-radius: 20px;
  border-top-left-radius: 20px;
  font-family: 'Source Serif Pro', sans-serif;
  align-self: flex-start;
}

/* Lado Derecho - Imagen */
.content-right {
  width: 45%;
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  padding-top: 80px;
}

.dish-image-container {
  position: relative;
  width: 500px;
  height: 500px;
}

.dish-main-image {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

/* Tarjetas de Platillos */
.dishes-grid {
  position: absolute; 
  top: -30px;  
  left: 0;
  display: flex;
  justify-content: flex-start;
  gap: 10px;  
  margin-bottom: 50px;
  padding-bottom: 0;
  padding-left: 0;
}

.dish-card {
  position: relative;
  width: 130px; 
  height: 130px;
  cursor: pointer;
  transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
  box-shadow: none ;
}

.dish-card:hover {
  transform: none;
}

/* Imagen redonda flotante arriba */
.dish-thumb-container {
  position: relative;
  width: 100px;
  height: 100px;
}

.dish-thumb-img {
  width: 130%;
  height: 130%;
  object-fit: cover;
  border-radius: 50%;
  cursor: pointer;
  transition: all 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.dish-thumb-img:hover {
  transform: translateY(-15px) scale(1.1);
}

.dish-card.swapping .dish-thumb-img {
  animation: cardToMain 2s cubic-bezier(0.34, 1.56, 0.64, 1);
  z-index: 1000;
}

@keyframes cardToMain {
  0% {
    transform: scale(1) translate(0, 0);
    opacity: 1;
  }
  50% {
    transform: scale(3) translate(-200px, -100px);
    opacity: 0.3;
  }
  100% {
    transform: scale(1) translate(0, 0);
    opacity: 1;
  }
}

.dish-card.active {
  transform: translateY(-12px);
  box-shadow: none;
}

/* Transiciones Vue */
.fade-slide-enter-active,
.fade-slide-leave-active {
  transition: all 2s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}

.fade-slide-enter-from {
  opacity: 0;
  transform: translateX(-100px);
}

.fade-slide-leave-to {
  opacity: 0;
  transform: translateX(100px);
}

.dish-rotate-enter-active,
.dish-rotate-leave-active {
  transition: all 1.2s cubic-bezier(0.34, 1.56, 0.64, 1);
  transition: all 1.2s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.dish-rotate-enter-from {
  opacity: 0;
  transform: translate(200px, 100px) scale(0.2);
}

.dish-rotate-leave-to {
  opacity: 0;
  transform: translate(-200px, -100px00px) scale(0.2);
}

@keyframes fadeInLeft {
  from {
    opacity: 0;
    transform: translateX(-50px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
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

  .main-content {
    padding: 20px 120px 10px;
    gap: 80px;
  }

  .dish-title {
    font-size: 45px;
  }

  .dish-description {
    font-size: 15px;
  }

  .dish-image-container {
    width: 420px;
    height: 420px;
  }

  .dish-main-image {
    width: 350px;
    height: 350px;
  }

  .dishes-grid {
    padding-left: 140px;
  }

  .dish-card {
    width: 180px;
    height: 210px;
  }

  .dish-thumb-img {
    width: 130px;
    height: 130px;
  }

}

/* Pantallas medianas-grandes (1367px - 1599px) */
@media (min-width: 1367px) and (max-width: 1599px) {
  .navbar {
    padding: 20px 90px;
  }

  .logo {
    font-size: 20px;
    margin-left: 46px;
  }

  .nav-links {
    gap: 64px;
    margin-left: 439px;
  }

  .nav-links a {
    font-size: 15px;
  }

  .btn-login {
    padding: 7px 22px;
    font-size: 14px;
    margin-right: 30px;
  }

  .main-content {
    padding: 20px 110px 10px;
    gap: 70px;
  }

   .content-right {
    padding-top: 145px;  
  }

  .dish-info {
    margin-top: 0;
  }

  .dish-title {
    font-size: 43px;
  }

  .dish-description {
    font-size: 16px;
    max-width: 400px;
  }

  .dish-image-container {
    width: 500px;
    height: 400px;
  }

  .dish-main-image {
    width: 650px;
    height: 650px;
    margin-left: -125px;
    margin-top: -87px;
  }

  .dishes-grid {
    gap: 18px;
    padding-left: 0;
    position: absolute;
    top: -40px; 
    left: 0;
    margin-bottom: 0; 
  }

  .dish-card {
    width: 145px;
    height: 145px;
  }

  .price-tag {
    padding: 13px 60px;
    font-size: 18px;
    margin-left: 0;
  }

  .dish-thumb-img {
    width: 150%;
    height: 150%;
  }
  
  .dish-card-price {
    font-size: 13px;
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
    padding: 8px 20px;
    font-size: 12px;
    margin-right: 15px !important;
  }

  .main-content {
    padding: 20px 80px 10px;
    gap: 50px;
  }

  .content-right {
    padding-top: 140px;  
  }

  .dish-info {
    margin-top: 0;  
  }

  .dish-title {
    font-size: 30px;
  }

  .dish-description {
    font-size: 13px;
    max-width: 400px;
  }

  .dish-image-container {
    width: 360px;
    height: 360px;
  }

  .dish-main-image {
    width: 495px;
    height: 495px;
    margin-left: -110px;
    margin-top: -47px;
  }

  .dishes-grid {
    gap: 10px;
    padding-left: 0;
    position: absolute;
    top: -30px;  
    left: 0;
    margin-bottom: 0; 
  }

  .dish-card {
    width: 130px;
    height: 130px;
  }

  .price-tag {
    padding: 10px 40px;
    font-size: 15px;
    margin-left: 0;
  }

  .dish-thumb-img {
    width: 130%;
    height: 130%;
  }
  .dish-card-price {
    font-size: 13px;
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

  .main-content {
    padding: 20px 60px 10px;
    gap: 40px;
  }

  .dish-title {
    font-size: 34px;
  }

  .dish-description {
    font-size: 12px;
  }

  .dish-image-container {
    width: 340px;
    height: 340px;
  }

  .dish-main-image {
    width: 280px;
    height: 280px;
  }

  .dishes-grid {
    gap: 25px;
    padding-left: 80px;
  }

  .dish-card {
    width: 150px;
    height: 180px;
  }

  .dish-thumb-img {
    width: 100px;
    height: 100px;
  }

  .dish-card-price {
    font-size: 12px;
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

  .platillos-page {
    height: auto;
    overflow-y: auto;
  }

  .main-content {
    flex-direction: column;
    padding: 100px 40px 20px;
    gap: 30px;
  }

  .content-left,
  .content-right {
    width: 100%;
  }

  .dish-title {
    font-size: 32px;
    text-align: center;
  }

  .dish-description {
    font-size: 13px;
    text-align: center;
  }

  .dish-info {
    display: flex;
    flex-direction: column;
    align-items: center;
    animation: fadeInLeft 0.8s ease-out;
  }

  .dish-image-container {
    width: 320px;
    height: 320px;
  }

  .dish-main-image {
    width: 260px;
    height: 260px;
  }

  .dishes-grid {
    flex-direction: column;
    align-items: center;
    padding-left: 0;
    gap: 20px;
  }

  .dish-card {
    width: 180px;
    height: 200px;
  }

  .dish-thumb-img {
    width: 120px;
    height: 120px;
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

  .main-content {
    padding: 100px 20px 20px;
  }

  .dish-title {
    font-size: 28px;
  }

  .dish-description {
    font-size: 12px;
  }

  .dish-image-container {
    width: 280px;
    height: 280px;
  }

  .dish-main-image {
    width: 230px;
    height: 230px;
  }

  .dish-card {
    width: 170px;
    height: 190px;
  }

  .dish-thumb-img {
    width: 110px;
    height: 110px;
  }

  .dish-card-price {
    font-size: 12px;
  }
}
</style>
