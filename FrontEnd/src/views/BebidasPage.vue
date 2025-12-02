<template>
  <div class="bebidas-page">
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
      <!-- Lado Izquierdo - Imagen Principal -->
      <div class="content-left">
        <!-- Frutas Decorativas Dinámicas -->
        <transition name="fade" mode="out-in">
          <div :key="currentDrink.id" class="fruit-decorations">
            <img 
              v-for="(fruit, index) in currentDrink.decorativeFruits" 
              :key="index"
              :src="fruit" 
              :alt="`fruta-${index}`" 
              :class="`fruit fruit-${index + 1}`"
            >
          </div>
        </transition>

        <transition name="drink-rotate" mode="out-in">
          <div :key="currentDrink.id" class="drink-image-container">
            <img 
              :src="currentDrink.mainImage" 
              :alt="currentDrink.title" 
              class="drink-main-image"
            >
          </div>
        </transition>
      </div>

      <!-- Lado Derecho - Info de la Bebida -->
      <div class="content-right">
        <!-- Círculos pequeños de frutas -->
        <div class="small-fruits">
          <div 
            v-for="drink in drinks" 
            :key="drink.id"
            @click="changeDrink(drink.id)"
            class="small-fruit-container"
            :class="{ active: currentDrink.id === drink.id }"
          >
            <img 
              :src="drink.thumbnailImage" 
              :alt="drink.title" 
              class="small-fruit"
            >
          </div>
        </div>

        <transition name="fade-slide" mode="out-in">
          <div :key="currentDrink.id" class="drink-info">
            <h1 class="drink-title">{{ currentDrink.title }}</h1>
            <p class="drink-description">{{ currentDrink.description }}</p>
            <div class="price-tag">{{ currentDrink.price }}</div>
          </div>
        </transition>
      </div>
    </div>
  </div>
</template>


<script>
import { ref } from 'vue'

export default {
  name: 'BebidasPage',
  setup() {
    const drinks = ref([
      {
        id: 1,
        title: 'Aperol Spritz',
        description: 'Un cóctel ligero y refrescante, ideal para el aperitivo. Su mezcla de Aperol, Prosecco y agua con gas, decorado con una rodaja de naranja, lo convierte en eventos sociales.',
        price: '30.000 COP',
        mainImage: require('@/assets/aperol-spritz.png'),
        thumbnailImage: require('@/assets/naranja-circulo.png'),
        bgColor: '#FFE7BC',
        cardBgColor: '#FFE7BC',
        decorativeFruits: [
          require('@/assets/naranja-rodaja.png'),
        ]
      },
      {
        id: 2,
        title: 'Cosmopolitan',
        description: 'Un cóctel femenino y elegante que ha ganado fama por su sabor equilibrado entre ácido y dulce. Su base de vodka y licor de naranja lo hace perfecto para cualquier celebración.',
        price: '38.000 COP',
        mainImage: require('@/assets/Cosmopolitan.png'),
        thumbnailImage: require('@/assets/toronja-circulo.png'),
        bgColor: '#CAFFBF',
        cardBgColor: '#CAFFBF',
        decorativeFruits: [
          require('@/assets/toronja-rodaja.png'),
        ]
      },
      {
        id: 3,
        title: 'Daiquiri Clásico',
        description: 'Un cóctel cubano por excelencia, el Daiquiri es refrescante, simple y delicioso. Es una opción perfecta para quienes buscan un sabor cítrico y suave.',
        price: '29.000 COP',
        mainImage: require('@/assets/Daiquiri-Clásico.png'),
        thumbnailImage: require('@/assets/lima-circulo.png'),
        bgColor: '#FFADAD',
        cardBgColor: '#FFADAD',
        decorativeFruits: [
          require('@/assets/lima-rodaja.png'),
        ]
      }
    ])

    const currentDrink = ref(drinks.value[0])

    const changeDrink = (drinkId) => {
      const selected = drinks.value.find(d => d.id === drinkId)
      if (selected) {
        currentDrink.value = selected
      }
    }

    return {
      drinks,
      currentDrink,
      changeDrink
    }
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Source+Serif+Pro:wght@400;600;700&display=swap'); 

/* Page Container */
.bebidas-page {
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
  padding: 120px 100px 40px; 
  min-height: 0;
  gap: 80px;
}

/* Lado Izquierdo */
.content-left {
  width: 50%;
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 600px;
}

.drink-image-container {
  position: relative;
  width: 450px;
  height: 450px;
  z-index: 10;
}

.drink-main-image {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

/* Frutas Decorativas Flotantes */
.fruit-decorations {
  position: absolute;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 5;
}

.fruit {
  position: absolute;
  width: 150px;
  height: 150px;
  object-fit: contain;
}

.fruit-1 {
  top: 10%;
  left: 5%;
  animation-delay: 0s;
}

.fruit-2 {
  top: 60%;
  left: -5%;
  animation-delay: 1s;
}

.fruit-3 {
  bottom: 15%;
  left: 10%;
  animation-delay: 2s;
}

.fruit-4 {
  top: 5%;
  right: 10%;
  animation-delay: 1.5s;
}

/* Lado Derecho */
.content-right {
  width: 50%;
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
}

.drink-info {
  width: 100%;
  margin-top: 40px; 
  animation: fadeInLeft 0.8s ease-out;
}

.drink-title {
  font-size: 36px;
  font-weight: 700;
  color: #1a1a1a;
  line-height: 1.2;
  margin-bottom: 15px;
  font-family: 'Open Sans', sans-serif;
}

.drink-description {
  font-size: 14px;
  color: #666;
  line-height: 1.6;
  margin-bottom: 25px;
  font-family: 'Montserrat', sans-serif;
  max-width: 500px;
}

.price-tag {
  display: inline-block;
  padding: 12px 40px;
  font-size: 16px;
  font-weight: 600;
  color: #ffffff;
  background-color: #7C0000;
  border-bottom-right-radius: 20px;
  border-top-left-radius: 20px;
  font-family: 'Source Serif Pro', sans-serif;
}

/* Círculos pequeños de frutas */
.small-fruits {
  position: absolute;
  top: -130px;
  right: 0;
  display: flex;
  gap: 20px;
  z-index: 10;
}

.small-fruit-container {
  cursor: pointer;
  transition: all 0.3s ease;
}

.small-fruit {
  width: 110px;
  height: 110px;
  object-fit: cover;
  border-radius: 50%;
  transition: all 0.3s ease;
}

.small-fruit-container:hover .small-fruit {
  transform: translateY(-5px) scale(1.1);
}

.small-fruit-container.active .small-fruit {
  transform: translateY(-8px) scale(1.15);
}

/* Transiciones Vue */
.fade-slide-enter-active,
.fade-slide-leave-active {
  transition: all 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}

.fade-slide-enter-from {
  opacity: 0;
  transform: translateX(-50px);
}

.fade-slide-leave-to {
  opacity: 0;
  transform: translateX(50px);
}

.drink-rotate-enter-active,
.drink-rotate-leave-active {
  transition: all 0.8s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.drink-rotate-enter-from {
  opacity: 0;
  transform: scale(0.3) rotate(-10deg);
}

.drink-rotate-leave-to {
  opacity: 0;
  transform: scale(0.3) rotate(10deg);
}

.fade-enter-active {
  transition: all 1s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.fade-leave-active {
  transition: all 0.5s ease;
}

.fade-enter-from {
  opacity: 0;
  transform: translate(-150px, -150px) rotate(-15deg) scale(0.3);
}

.fade-leave-to {
  opacity: 0;
  transform: translate(100px, 100px) scale(0.5);
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
    padding: 20px 100px !important;
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
    padding: 140px 120px 60px;
    gap: 100px;
  }

  .drink-title {
    font-size: 42px;
  }

  .drink-description {
    font-size: 16px;
  }

  .drink-image-container {
    width: 500px;
    height: 500px;
  }

  .small-fruit {
    width: 80px;
    height: 80px;
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
    padding: 130px 110px 50px;
    gap: 90px;
  }

  .drink-title {
    font-size: 38px;
  }

  .drink-description {
    font-size: 16px;
  }

  .price-tag {
    padding: 15px 65px;
    font-size: 18px;
  }

  .drink-image-container {
    width: 550px;
    height: 550px;
    top: -50px;
    left: -37px;
  }

  .small-fruits {
    top: -100px;
    right: 33%;
  }

  .small-fruit {
    width: 120px;
    height: 120px;
  }

  .fruit{
    width: 600px;
    height: 600px;
    left: -76px;
    top: -50px
  }
}

/* Pantallas medianas (1280px - 1366px) */
@media (min-width: 1280px) and (max-width: 1366px) {
  .navbar {
    padding: 20px 70px !important;
  }

  .logo {
    font-size: 19px;
    margin-left: -5px;
  }

  .nav-links {
    gap: 40px;
  }

  .nav-links a {
    font-size: 14px;
  }

  .btn-login {
    padding: 8px 20px;
    font-size: 14px;
    margin-right: -19px !important;
  }

  .main-content {
    padding: 120px 80px 40px;
    gap: 60px;
  }

  .drink-title {
    font-size: 32px;
  }

  .drink-description {
    font-size: 13px;
  }

  .drink-image-container {
    width: 400px;
    height: -290%;
    top: -30px;
    left: -30px;
  }

  .small-fruits {
    top: -100px;
    right: 30%;
  }

  .small-fruit {
    width: 100px;
    height: 100px;
  }

  .fruit {
    width: 480px;
    height: 480px;
    left: -25px;
    top: 30px;
  }
}

/* Pantallas pequeñas de laptop (1024px - 1279px) */
@media (min-width: 1024px) and (max-width: 1279px) {
  .navbar {
    padding: 18px 50px !important;
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
    padding: 110px 60px 30px;
    gap: 50px;
  }

  .drink-title {
    font-size: 28px;
  }

  .drink-description {
    font-size: 12px;
  }

  .drink-image-container {
    width: 350px;
    height: 350px;
  }

  .small-fruit {
    width: 90px;
    height: 90px;
  }

  .fruit {
    width: 110px;
    height: 110px;
  }
}

/* Tablets (768px - 1023px) */
@media (max-width: 1023px) {
  .navbar {
    padding: 16px 35px !important;
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

  .bebidas-page {
    height: auto;
    overflow-y: auto;
  }

  .main-content {
    flex-direction: column;
    padding: 100px 40px 20px;
    gap: 40px;
  }

  .content-left,
  .content-right {
    width: 100%;
  }

  .content-left {
    height: 400px;
  }

  .drink-title {
    font-size: 28px;
    text-align: center;
  }

  .drink-description {
    font-size: 13px;
    text-align: center;
  }

  .drink-info {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .drink-image-container {
    width: 320px;
    height: 320px;
  }

  .small-fruits {
    position: static;
    justify-content: center;
    margin-bottom: 30px;
  }

  .fruit {
    width: 50px;
    height: 50px;
  }
}

/* Tablets pequeñas (600px - 767px) */
@media (max-width: 767px) {
  .navbar {
    padding: 15px 20px !important;
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
    margin-left: 0;
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

  .drink-title {
    font-size: 24px;
  }

  .drink-description {
    font-size: 12px;
  }

  .drink-image-container {
    width: 280px;
    height: 280px;
  }

  .small-fruit {
    width: 55px;
    height: 55px;
  }

  .fruit {
    width: 45px;
    height: 45px;
  }
}
</style>