<!-- ContenidoNoDisponible.vue -->
<template>
  <div class="no-access-container">
    <!-- Imágenes decorativas -->
    <img src="@/assets/grapefruit.png" alt="Grapefruit" class="deco-grapefruit">
    <img src="@/assets/hoja3.png" alt="Hoja" class="deco-hoja-top">
    <img src="@/assets/hoja2.png" alt="Hoja" class="deco-hoja-bottom">
    
    <div class="content">
      <div class="icon-wrapper">
        <svg width="120" height="120" viewBox="0 0 24 24" fill="none" class="lock-icon">
          <rect x="5" y="11" width="14" height="10" rx="2" stroke="#ff6b35" stroke-width="2"/>
          <path d="M8 11V7a4 4 0 1 1 8 0v4" stroke="#ff6b35" stroke-width="2" stroke-linecap="round"/>
          <circle cx="12" cy="16" r="1.5" fill="#ff6b35"/>
        </svg>
      </div>
      
      <h1 class="title">Acceso Denegado</h1>
      
      <p class="message">
        No tienes permisos para acceder a este contenido.
        <br>Si crees que esto es un error, contacta al administrador.
      </p>
      
      <button @click="volverInicio" class="btn-back">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
          <path d="M19 12H5M5 12L12 19M5 12L12 5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        Volver al Inicio
      </button>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const volverInicio = () => {
  const user = JSON.parse(localStorage.getItem('user') || '{}')
  const esAdmin = user.es_admin === true || user.role === 'admin'
  const token = localStorage.getItem('access_token')
  
  if (token && esAdmin) {
    router.push('/administracion')
  } else if (token) {
    router.push('/homeCliente')
  } else {
    router.push('/')
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;800&family=Montserrat:wght@400;500;600&display=swap');

.no-access-container {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #f5f5f5;
  padding: 20px;
  position: relative;
  overflow: hidden;
}

/* Imágenes decorativas */
.deco-grapefruit {
  position: fixed;
  top: -55px;
  left: -65px;
  width: 180px;
  height: 180px;
  object-fit: contain;
  z-index: 5;
  opacity: 0.8;
}

.deco-hoja-top {
  position: fixed;
  top: 100px;
  right: 50px;
  width: 100px;
  height: 100px;
  object-fit: contain;
  z-index: 5;
  opacity: 0.7;
  animation: float 3s ease-in-out infinite;
}

.deco-hoja-bottom {
  position: fixed;
  bottom: 80px;
  left: 60px;
  width: 90px;
  height: 90px;
  object-fit: contain;
  z-index: 5;
  opacity: 0.7;
  animation: float 4s ease-in-out infinite;
}

@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-15px); }
}

.content {
  text-align: center;
  background: white;
  padding: 60px 50px;
  border-radius: 20px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  max-width: 550px;
  width: 100%;
  position: relative;
  z-index: 10;
}

.icon-wrapper {
  margin-bottom: 25px;
  animation: pulse 2s ease-in-out infinite;
}

@keyframes pulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.05); }
}

.lock-icon {
  filter: drop-shadow(0 2px 8px rgba(255, 107, 53, 0.2));
}

.title {
  font-size: 36px;
  font-weight: 800;
  color: #28233b;
  margin-bottom: 20px;
  font-family: 'Open Sans', sans-serif;
  letter-spacing: -0.5px;
}

.message {
  font-size: 16px;
  color: #666;
  margin-bottom: 35px;
  line-height: 1.8;
  font-family: 'Montserrat', sans-serif;
}

.btn-back {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 14px 35px;
  background-color: #ff6b35;
  color: white;
  border: none;
  border-radius: 50px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  font-family: 'Montserrat', sans-serif;
  box-shadow: 0 4px 15px rgba(255, 107, 53, 0.3);
}

.btn-back:hover {
  background-color: #3b82f6;
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(59, 130, 246, 0.4);
}

.btn-back svg {
  transition: transform 0.3s ease;
}

.btn-back:hover svg {
  transform: translateX(-3px);
}

/* Responsive */
@media (max-width: 768px) {
  .deco-grapefruit,
  .deco-hoja-top,
  .deco-hoja-bottom {
    display: none;
  }

  .content {
    padding: 40px 30px;
  }

  .title {
    font-size: 28px;
  }

  .message {
    font-size: 14px;
  }

  .btn-back {
    padding: 12px 28px;
    font-size: 14px;
  }
}
</style>