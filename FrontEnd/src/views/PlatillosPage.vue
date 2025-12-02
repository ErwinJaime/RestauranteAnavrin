<template>
  <div class="platillos-page">
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

    <!-- Contenido Principal -->
    <div class="main-content">
      <!-- Lado Izquierdo - Info del Platillo -->
      <div class="content-left">
        <transition name="fade-slide" mode="out-in">
          <div :key="currentDish.id" class="dish-info">
            <h1 class="dish-title">{{ currentDish.title }}</h1>
            <p class="dish-description">{{ currentDish.description }}</p>
            <div class="price-tag">{{ currentDish.price }}</div>
          </div>
        </transition>
      </div>

      <!-- Lado Derecho - Imagen Principal -->
      <div class="content-right">
        <!-- Animación del CUADRO (independiente) -->
        <transition name="background-fade" mode="out-in">
          <div 
            :key="currentDish.id"
            class="background-shape" 
            :style="{ backgroundColor: currentDish.bgColor }"
          ></div>
        </transition>

        <!-- Animación del PLATO (independiente) -->*
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
    </div>


    <!-- Tarjetas de Platillos -->
    <div class="dishes-grid">
      <div 
        v-for="dish in dishes" 
        :key="dish.id"
        @click="changeDish(dish.id)"
        class="dish-card"
      >
        <!-- Imagen redonda flotando arriba -->
        <div class="dish-thumb-container">
          <img :src="dish.thumbnailImage" :alt="dish.title" class="dish-thumb-img">
        </div>

        <!-- Tarjeta de color debajo -->
        <div 
          class="dish-card-bg"
          :style="{ backgroundColor: dish.cardBgColor }"
        ></div>

        <!-- Info del platillo -->
        <div class="dish-card-info">
          <h3 class="dish-card-title">{{ dish.title }}</h3>
          <p class="dish-card-price">{{ dish.price }}</p>
        </div>
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
        title: 'Veggie Bow-Tie Pasta',
        description: 'Pasta tipo moñita farfalle, calabacín en julianas, pimientos rojos y amarillos, champiñones salteados, espinaca fresca, tomates cherry, aceite de oliva extra virgen y un toque de albahaca.',
        price: '23.500 COP',
        mainImage: require('@/assets/pasta-bowtie.png'),
        thumbnailImage: require('@/assets/pasta-bowtie1.png'),
        bgColor: '#FFE7BC',
        cardBgColor: '#FFE7BC'
      },
      {
        id: 2,
        title: 'Veggie Delight Noodles',
        description: 'Fideos salteados estilo asiático, brócoli, zanahoria en tiras, col morado, pimentón verde, cebolla blanca, salsa de soya ligera, jengibre fresco y semillas de sésamo.',
        price: '24.800 COP',
        mainImage: require('@/assets/noodles.png'),
        thumbnailImage: require('@/assets/noodles1.png'),
        bgColor: '#FFCCA6',
        cardBgColor: '#FFCCA6'
      },
      {
        id: 3,
        title: 'Garden Glow Bow-Tie Pasta',
        description: 'Pasta farfalle con pesto de albahaca y nueces, tomates secos, arvejas tiernas, calabacín, hojas de rúgula y un toque de queso parmesano rallado.',
        price: '25.900 COP',
        mainImage: require('@/assets/pasta-glow.png'),
        thumbnailImage: require('@/assets/pasta-glow1.png'),
        bgColor: '#B4FF9B',
        cardBgColor: '#B4FF9B'
      }
    ])

    const currentDish = ref(dishes.value[0])

    const changeDish = (dishId) => {
      const selected = dishes.value.find(d => d.id === dishId)
      if (selected) {
        currentDish.value = selected
      }
    }

    return {
      dishes,
      currentDish,
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
  justify-content: space-between;
  padding: 20px 100px 10px; 
  min-height: 0;
  gap: 60px;
}

/* Lado Izquierdo */
.content-left {
  width: 45%;
  position: relative;
}

.dish-info {
  animation: fadeInLeft 0.8s ease-out;
}

.dish-title {
  font-size: 28px;
  font-weight: 700;
  margin-left: 34%;
  color: #1a1a1a;
  line-height: 1.1;
  margin-bottom: 10px;
  font-family: 'Open Sans', sans-serif;
}

.dish-description {
  font-size: 11px;
  margin-left: 34%;
  color: #666;
  line-height: 1.6;
  margin-bottom: 30px;
  font-family: 'Montserrat', sans-serif;
}

.price-tag { /* etiqueta precio */
  display: inline-block;
  padding: 9px 28px;
  font-size: 14px;
  margin-top: -30px; 
  margin-left: 50%;
  font-weight: 600;
  color: #ffffff;
  background-color: #5B9918;
  border-bottom-right-radius: 20px;
  border-top-left-radius: 20px;
  font-family: 'Source Serif Pro', sans-serif;
}

/* Lado Derecho - Imagen */
.content-right {
  width: 55%;
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
}

.dish-image-container {
  position: relative;
  width: 650px;
  height: 650px;
}

.dish-main-image {
  position: absolute;
  width: 280px;
  height: 280px;
  object-fit: cover;
  border-radius: 50%;
  top: 240px;
  right: 60px;
  z-index: 2;
}

.background-shape {
  position: absolute;
  width: 210px;
  height: 245px;
  bottom: 0;
  right: 96px;
  top: 400px;
  z-index: 0;
  transition: background-color 1.2s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}

/* Tarjetas de Platillos */
.dishes-grid {
  display: flex;
  justify-content: flex-start; 
  left: 8px;
  gap: 40px;
  padding-bottom: 0px;  
  padding-left: 55px; 
  margin-top: 0; 
}

.dish-card {
  position: relative;
  width: 170px; 
  height: 200px;
  cursor: pointer;
  transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}

.dish-card:hover {
  transform: translateY(-8px);
}

/* Imagen redonda flotante arriba */
.dish-thumb-container {
  position: absolute;
  top: -30px;
  left: 55%;
  transform: translateX(-50%);
  z-index: 3;
}

.dish-thumb-img {
  width: 120px; 
  height: 120px; 
  object-fit: cover;
  border-radius: 50%;
}

/* Fondo de color de la tarjeta */
.dish-card-bg {
  position: absolute;
  top: 40px; 
  bottom: 0px;
  width: 110%;
  height: 180px; 
  border-radius: 25px;
}

.dish-card.active {
  transform: translateY(-12px);
  box-shadow: 0 12px 32px rgba(0, 0, 0, 0.2);
}

.card-bg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1;
  transition: background-color 0.4s ease;
}

.dish-card-image {
  position: relative;
  z-index: 2;
  width: 100%;
  height: 140px;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 15px;
}

.dish-card-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 50%;
}

/* Texto dentro de la tarjeta */
.dish-card-info {
  position: absolute;
  bottom: 15px;
  width: 100%;
  text-align: left;
  z-index: 4;
}

.dish-card-title {
  font-size: 15px;
  font-weight: 600;
  margin-bottom: 4px;
  margin-left: 17%;
  color: #000000;
  font-family: 'Source Serif Pro', sans-serif;
}

.dish-card-price { /* precio plato*/ 
  font-size: 14px;
  font-weight: 700;
  color: #317A00;
  margin-left: 58%;
  font-family: 'Source Serif Pro', sans-serif;
}

/* Transiciones Vue */
.fade-slide-enter-active,
.fade-slide-leave-active {
  transition: all 1.2s cubic-bezier(0.25, 0.46, 0.45, 0.94);
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
  transition: all 1.2s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}

.dish-rotate-enter-from {
  opacity: 0;
  transform: translate(-200px, 200px) scale(0.2);
}

.dish-rotate-leave-to {
  opacity: 0;
  transform: translate(-200px, 200px) scale(0.2);
}

/* Animación del cuadro de fondo */
.background-fade-enter-active,
.background-fade-leave-active {
  transition: all 1s ease-in-out;
}

.background-fade-enter-from {
  opacity: 0;
  transform: translateY(100px);
}

.background-fade-leave-to {
  opacity: 0;
  transform: translateY(-100px);
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

  .background-shape {
    width: 320px;
    height: 320px;
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

  .dish-card-bg {
    height: 150px;
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
    gap: 105px;
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
    padding: 40px 110px 10px;
    gap: 40px;
  }

  .dish-title {
    font-size: 44px;
    margin-left: 20%;
  }

  .dish-description {
    font-size: 16px;
    margin-left: 20%;
  }

  .dish-image-container {
    width: 400px;
    height: 400px;
  }

  .dish-main-image {
    width: 410px;
    height: 410px;
    top: 120px;
    right: -45px;
  }

  .background-shape {
    width: 320px;
    height: 320px;
    right: 140px;
    top: 400px;
  }

  .dishes-grid {
    padding-left: 130px;
  }

  .dish-card {
    width: 179px; 
    height: 200px;
  }

   .dish-thumb-img {
    width: 145px;
    height: 145px;
  }

  .dish-card-title {
    font-size: 17px;
    font-weight: 550;
    margin-bottom: -14px;
    margin-left: 10%;
  }
  .dish-card-price { 
    font-size: 14px;
    font-weight: 700;
    margin-left: 59%;
  }

  .price-tag { 
    padding: 9px 30px;
    font-size: 20px;
    margin-top: -30px; 
    margin-left: 40%;
    font-weight: 560;
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

  .main-content {
    padding: 20px 80px 10px;
    gap: 50px;
  }

  .dish-title {
    font-size: 29px;
    
  }

  .dish-description {
    font-size: 13px;
  }

  .dish-image-container {
    width: 360px;
    height: 360px;
  }

  .dish-main-image {
    width: 300px;
    height: 300px;  
    right: -45px;  
    top: 100px;
  }

  .background-shape {
    width: 220px; 
    height: 300px; 
    right: -5px;  
    top: 310px;
  }

  .dishes-grid {
    gap: 30px;
    padding-left: 185px;
  }

  .dish-card {
    width: 160px;
    height: 190px;
  }

  .dish-thumb-img {
    width: 129px;
    height: 129px;
  }

  .dish-card-bg {
    height: 150px;
    top: 35px;
  }

  .dish-card-title {
    font-size: 14px;
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

  .background-shape {
    width: 250px;
    height: 250px;
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

  .dish-card-bg {
    height: 130px;
    top: 30px;
  }

  .dish-card-title {
    font-size: 13px;
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
  }

  .dish-image-container {
    width: 320px;
    height: 320px;
  }

  .dish-main-image {
    width: 260px;
    height: 260px;
  }

  .background-shape {
    width: 230px;
    height: 230px;
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

  .dish-card-bg {
    height: 140px;
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

  .background-shape {
    width: 200px;
    height: 200px;
  }

  .dish-card {
    width: 170px;
    height: 190px;
  }

  .dish-thumb-img {
    width: 110px;
    height: 110px;
  }

  .dish-card-bg {
    height: 135px;
  }

  .dish-card-title {
    font-size: 13px;
  }

  .dish-card-price {
    font-size: 12px;
  }
}
</style>
