<!-- ================================= -->
<!-- NotFound.vue -->
<!-- ================================= -->

<template>
  <div class="not-found-container">
    <!-- Imágenes decorativas -->
    <img src="@/assets/grapefruit.png" alt="Grapefruit" class="deco-grapefruit">
    <img src="@/assets/bebida-verde.png" alt="Mortero" class="deco-mortero">
    <img src="@/assets/hoja2.png" alt="Hoja" class="deco-hoja">
    
    <div class="content">
      <div class="error-code">404</div>
      
      <div class="icon-wrapper">
        <svg width="100" height="100" viewBox="0 0 24 24" fill="none" class="search-icon">
          <circle cx="11" cy="11" r="7" stroke="#7cb342" stroke-width="2"/>
          <path d="M21 21L16.65 16.65" stroke="#7cb342" stroke-width="2" stroke-linecap="round"/>
          <path d="M9 11H13M11 9V13" stroke="#7cb342" stroke-width="2" stroke-linecap="round"/>
        </svg>
      </div>
      
      <h1 class="title">Contenido No Disponible</h1>
      
      <p class="message">
        Lo sentimos, la página que buscas no existe o no tienes permisos para acceder a ella.
      </p>
      
      <div class="actions">
        <button @click="volverInicio" class="btn-primary">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none">
            <path d="M3 12L2 12L2 8L6 8M21 12L22 12L22 16L18 16M9 3L15 3M12 3L12 9M6 8L6 3M18 16L18 21" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
            <path d="M8 12L8 17C8 18.1046 8.89543 19 10 19L14 19C15.1046 19 16 18.1046 16 17L16 12" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
          </svg>
          Volver al Inicio
        </button>
        <button @click="volverAtras" class="btn-secondary">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none">
            <path d="M15 18L9 12L15 6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
          Página Anterior
        </button>
      </div>
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

const volverAtras = () => {
  router.go(-1)
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;800&family=Montserrat:wght@400;500;600&display=swap');

.not-found-container {
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

.deco-mortero {
  position: fixed;
  bottom: -20px;
  right: -50px;
  width: 240px;
  height: 240px;
  object-fit: contain;
  z-index: 5;
  opacity: 0.7;
  animation: rotate 20s linear infinite;
}

@keyframes rotate {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

.deco-hoja {
  position: fixed;
  top: 120px;
  right: 80px;
  width: 100px;
  height: 100px;
  object-fit: contain;
  z-index: 5;
  opacity: 0.7;
  animation: sway 4s ease-in-out infinite;
}

@keyframes sway {
  0%, 100% { transform: rotate(-5deg) translateY(0); }
  50% { transform: rotate(5deg) translateY(-10px); }
}

.content {
  text-align: center;
  background: white;
  padding: 60px 50px;
  border-radius: 20px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  max-width: 600px;
  width: 100%;
  position: relative;
  z-index: 10;
}

.error-code {
  font-size: 80px;
  font-weight: 800;
  color: #7cb342;
  line-height: 1;
  margin-bottom: 10px;
  font-family: 'Open Sans', sans-serif;
  opacity: 0.2;
  letter-spacing: -2px;
}

.icon-wrapper {
  margin-bottom: 25px;
  animation: bounce 2s ease-in-out infinite;
}

@keyframes bounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-15px); }
}

.search-icon {
  filter: drop-shadow(0 2px 8px rgba(124, 179, 66, 0.2));
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

.actions {
  display: flex;
  gap: 15px;
  justify-content: center;
  flex-wrap: wrap;
}

.btn-primary, .btn-secondary {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 14px 30px;
  border: none;
  border-radius: 50px;
  font-size: 15px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  font-family: 'Montserrat', sans-serif;
}

.btn-primary {
  background-color: #7cb342;
  color: white;
  box-shadow: 0 4px 15px rgba(124, 179, 66, 0.3);
}

.btn-primary:hover {
  background-color: #6d9fef;
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(109, 159, 239, 0.4);
}

.btn-secondary {
  background-color: #e5e5e5;
  color: #666;
}

.btn-secondary:hover {
  background-color: #d0d0d0;
  color: #333;
  transform: translateY(-2px);
}

.btn-primary svg,
.btn-secondary svg {
  transition: transform 0.3s ease;
}

.btn-primary:hover svg {
  transform: scale(1.1);
}

.btn-secondary:hover svg {
  transform: translateX(-3px);
}

/* Responsive */
@media (max-width: 768px) {
  .deco-grapefruit,
  .deco-mortero,
  .deco-hoja {
    display: none;
  }

  .content {
    padding: 40px 30px;
  }

  .error-code {
    font-size: 60px;
  }

  .icon-wrapper svg {
    width: 80px;
    height: 80px;
  }

  .title {
    font-size: 28px;
  }

  .message {
    font-size: 14px;
  }

  .actions {
    flex-direction: column;
    gap: 12px;
  }

  .btn-primary, .btn-secondary {
    width: 100%;
    padding: 12px 24px;
    font-size: 14px;
  }
}
</style>