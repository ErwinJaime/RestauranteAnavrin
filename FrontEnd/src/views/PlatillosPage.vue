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
      <button class="btn-login">Inicia Sesión</button>
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
        <transition name="dish-rotate" mode="out-in">
          <div :key="currentDish.id" class="dish-image-container">
            <img 
              :src="currentDish.mainImage" 
              :alt="currentDish.title" 
              class="dish-main-image"
            >
            <div 
              class="background-shape" 
              :style="{ backgroundColor: currentDish.bgColor }"
            ></div>
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
        thumbnailImage: require('@/assets/pasta-bowtie.png'),
        bgColor: '#FFF4E6',
        cardBgColor: '#FFF4E6'
      },
      {
        id: 2,
        title: 'Veggie Delight Noodles',
        description: 'Fideos salteados estilo asiático, brócoli, zanahoria en tiras, col morado, pimentón verde, cebolla blanca, salsa de soya ligera, jengibre fresco y semillas de sésamo.',
        price: '24.800 COP',
        mainImage: require('@/assets/noodles.png'),
        thumbnailImage: require('@/assets/noodles.png'),
        bgColor: '#FFE5D9',
        cardBgColor: '#FFE5D9'
      },
      {
        id: 3,
        title: 'Garden Glow Bow-Tie Pasta',
        description: 'Pasta farfalle con pesto de albahaca y nueces, tomates secos, arvejas tiernas, calabacín, hojas de rúgula y un toque de queso parmesano rallado.',
        price: '25.900 COP',
        mainImage: require('@/assets/pasta-glow.png'),
        thumbnailImage: require('@/assets/pasta-glow.png'),
        bgColor: '#E8F5E9',
        cardBgColor: '#E8F5E9'
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
}

.logo {
  font-size: 20px;
  font-weight: 600;
  color: #1a1a1a;
  letter-spacing: 1px;
  margin-left: 30px;
}

.nav-links {
  display: flex;
  gap: 60px;
}

.nav-links a {
  font-size: 14px;
  color: #666;
  text-decoration: none;
  transition: color 0.3s ease;
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
  font-size: 40px;
  font-weight: 700;
  margin-left: 10%;
  color: #1a1a1a;
  line-height: 1.1;
  margin-bottom: 20px;
  font-family: 'Open Sans', sans-serif;
}

.dish-description {
  font-size: 17px;
  margin-left: 10%;
  color: #666;
  line-height: 1.6;
  margin-bottom: 30px;
  font-family: 'Montserrat', sans-serif;
}

.price-tag {
  display: inline-block;
  padding: 10px 28px;
  font-size: 14px;
  margin-top: -40px; 
  margin-left: 20%;
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
  width: 380px; 
  height: 380px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.dish-main-image {
  width: 320px; 
  height: 320px;  
  object-fit: contain;
  position: relative;
  z-index: 2;
}

.background-shape {
  position: absolute;
  width: 290px; 
  height: 350px;
  border-radius: 50%;
  z-index: 1;
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
  transition: 0.3s ease;
}

.dish-card:hover {
  transform: translateY(-8px);
}

/* Imagen redonda flotante arriba */
.dish-thumb-container {
  position: absolute;
  top: 0px;
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
  text-align: center;
  z-index: 4;
}

.dish-card-title {
  font-size: 15px;
  font-weight: 600;
  margin-bottom: 4px;
  color: #000000;
  font-family: 'Open Sans', sans-serif;
}

.dish-card-price { /* precio plato*/ 
  font-size: 14px;
  font-weight: 700;
  color: #317A00;
  font-family: 'Montserrat', sans-serif;
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
</style>