<template>
  <div class="resena-container">
    <!-- Navegación -->
    <nav class="navbar">
      <h1 class="logo">ANAVRIN</h1>
      <div class="nav-links">
        <router-link to="/">Home</router-link>
        <router-link to="/about">About</router-link>
        <router-link to="/review">Review</router-link>
      </div>
      <span v-if="usuarioNombre !== 'Invitado'" class="btn-admin">{{ usuarioNombre }}</span>
      <span v-else class="btn-invitado">Invitado</span>
      <button class="btn-cerrar-sesion" @click="cerrarSesion">
        {{ usuarioNombre !== 'Invitado' ? 'Cerrar Sesión' : 'Iniciar Sesión' }}
      </button>
    </nav>

    <!-- Decoraciones -->
    <img src="@/assets/naranja.png" alt="naranja" class="decoration-naranja" />
    <img src="@/assets/aceite.png" alt="aceite" class="decoration-aceite" />
    <img src="@/assets/guacamole.png" alt="guacamole" class="decoration-guacamole" />
    <img src="@/assets/estrellas.png" alt="estrella" class="decoration-estrella1" />

    <!-- Contenido Principal -->
    <div class="main-content">
      <h1 class="page-title">Escribe tu Reseña</h1>
      <p class="page-subtitle">Elige tu reacción a nuestros productos</p>

      <!-- Emojis de Reacción CON IMÁGENES -->
      <div class="emojis-container">
        <button 
          :class="['emoji-btn', { 'active': reaccionSeleccionada === 'triste' }]"
          @click="seleccionarReaccion('triste')"
        >
          <img src="@/assets/triste.png" alt="Triste" class="emoji-img">
        </button>
        <button 
          :class="['emoji-btn', { 'active': reaccionSeleccionada === 'neutral' }]"
          @click="seleccionarReaccion('neutral')"
        >
          <img src="@/assets/neutral.png" alt="Neutral" class="emoji-img">
        </button>
        <button 
          :class="['emoji-btn', { 'active': reaccionSeleccionada === 'feliz' }]"
          @click="seleccionarReaccion('feliz')"
        >
          <img src="@/assets/feliz.png" alt="Feliz" class="emoji-img">
        </button>
      </div>

      <!-- Formulario de Reseña -->
      <div class="form-container">
        <textarea
          v-model="comentario"
          class="textarea-comentario"
          placeholder="Tu comentario nos ayuda a mejorar, cuéntanos tu opinión."
          rows="4"
        ></textarea>
          <button class="btn-aceptar" @click="enviarResena" :disabled="enviando">
            {{ enviando ? 'Enviando...' : 'Aceptar' }}
          </button>
      </div>
    </div>

    <!-- Modal de Confirmación -->
    <div v-if="mostrarModal" class="modal-overlay" @click="cerrarModal">
      <div class="modal-content" @click.stop>
        <h2 class="modal-title">¡Reseña enviada!</h2>
        <p class="modal-subtitle">Gracias por compartir tu opinión con nosotros.</p>
        <button class="btn-cerrar-modal" @click="cerrarModal">
          Cerrar
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { crearResena, listarProductos } from '@/services/productos';

const router = useRouter();

// Estados
const usuarioNombre = ref('');
const reaccionSeleccionada = ref(null);
const comentario = ref('');
const mostrarModal = ref(false);
const enviando = ref(false);
const productoIdPorDefecto = ref(null);

// Obtener nombre del usuario
const obtenerUsuario = () => {
  const usuario = JSON.parse(localStorage.getItem('user') || '{}');
  usuarioNombre.value = usuario.nombre || 'Invitado';
};

const obtenerProductoPorDefecto = async () => {
  try {
    const response = await listarProductos();
    if (response.data && response.data.length > 0) {
      productoIdPorDefecto.value = response.data[0].id;
      console.log('✅ Producto por defecto:', productoIdPorDefecto.value);
    }
  } catch (error) {
    console.error('❌ Error al obtener productos:', error);
  }
};

const obtenerCalificacion = (emoji) => {
  const mapeo = {
    'triste': 2,
    'neutral': 3,
    'feliz': 5
  };
  return mapeo[emoji] || 3;
};

// Cerrar sesión
const cerrarSesion = () => {
  if (localStorage.getItem('access_token')) {
    localStorage.removeItem('user');
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    sessionStorage.clear();
    alert('Sesión cerrada correctamente');
  }
  router.push('/');
};

// Seleccionar reacción
const seleccionarReaccion = (valor) => {
  reaccionSeleccionada.value = valor;
};

// Enviar reseña
const enviarResena = async () => {
  // Validaciones
  if (!reaccionSeleccionada.value) {
    alert('Por favor selecciona una reacción');
    return;
  }

  if (!comentario.value.trim()) {
    alert('Por favor escribe un comentario');
    return;
  }

  if (!localStorage.getItem('access_token')) {
    alert('Por favor inicia sesión para enviar una reseña');
    router.push('/');
    return;
  }

  try {
    // Aquí iría tu llamada a la API para guardar la reseña
    // const response = await crearResena({
    //   reaccion: reaccionSeleccionada.value,
    //   comentario: comentario.value
    // });

    // Mostrar modal de confirmación

    enviando.value = true;

    const datosResena = {
      producto: productoIdPorDefecto.value,
      emoji: reaccionSeleccionada.value,
      calificacion: obtenerCalificacion(reaccionSeleccionada.value),
      comentario: comentario.value.trim()
    };

    console.log('📤 Enviando reseña:', datosResena);

    await crearResena(datosResena);
    
    console.log('✅ Reseña creada exitosamente');

    mostrarModal.value = true;
    
    // Limpiar formulario
    reaccionSeleccionada.value = null;
    comentario.value = '';

  } catch (error) {
    console.error('Error al enviar reseña:', error);
    alert('Error al enviar la reseña. Por favor intenta nuevamente.');
    console.error('❌ Error al enviar reseña:', error);
    
    if (error.response?.data?.error?.includes('Ya has dejado una reseña')) {
      alert('Ya has dejado una reseña anteriormente. Solo puedes dejar una reseña por cuenta.');
    } else {
      const errorMsg = error.response?.data?.error || error.response?.data?.message || 'Error al enviar la reseña';
      alert(errorMsg);
    }
  } finally {
    enviando.value = false;
  }
};

// Cerrar modal
const cerrarModal = () => {
  mostrarModal.value = false;
  router.push('/');
};

onMounted(async () => {
  obtenerUsuario();
  await obtenerProductoPorDefecto();
});
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.resena-container {
  min-height: 100vh;
  background-color: #ffffff;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  position: relative;
  overflow-x: hidden;
}

/* ==================== NAVBAR ==================== */
.navbar {
  position: absolute;
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
  gap: 25px !important;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

.logo {
  font-size: 20px;
  font-weight: 700;
  color: #1a1a1a;
  letter-spacing: 2px;
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

.nav-links a {
  font-size: 14px;
  color: #666;
  text-decoration: none;
  transition: color 0.3s ease;
  white-space: nowrap;
  font-weight: 500;
}

.nav-links a:hover {
  color: #35a4ff;
}

.nav-links a.router-link-active {
  color: #ff6b35;
  font-weight: 600;
}

.btn-admin {
  padding: 8px 28px;
  font-size: 14px;
  color: #000;
  background-color: #ff6b35;
  border: none;
  border-radius: 50px;
  cursor: default;
  font-weight: 600;
  white-space: nowrap;
  flex-shrink: 0;
  margin-left: auto !important;
  margin-right: 10px !important;
}

.btn-invitado {
  padding: 8px 28px;
  font-size: 14px;
  color: #000;
  background-color: #e0e0e0;
  border: none;
  border-radius: 50px;
  cursor: default;
  font-weight: 600;
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
  color: #ffffff;
  border-color: #6d9fef;
}

/* ==================== DECORACIONES ==================== */
.decoration-naranja {
  position: absolute;
  top: 100px;
  left: 40px;
  width: 140px;
  z-index: 1;
  opacity: 0.9;
}

.decoration-aceite {
  position: absolute;
  top: 90px;
  right: 40px;
  width: 140px;
  z-index: 1;
  opacity: 0.9;
}

.decoration-guacamole {
  position: absolute;
  bottom: 100px;
  left: 60px;
  width: 150px;
  z-index: 1;
}

.decoration-estrella1 {
  position: absolute;
  bottom: 120px;
  right: 80px;
  width: 80px;
  z-index: 1;
  animation: float 3s ease-in-out infinite;
}

.decoration-estrella2 {
  position: absolute;
  bottom: 200px;
  right: 150px;
  width: 60px;
  z-index: 1;
  animation: float 4s ease-in-out infinite;
  animation-delay: 1s;
}

@keyframes float {
  0%, 100% {
    transform: translateY(0px);
  }
  50% {
    transform: translateY(-20px);
  }
}

/* ==================== CONTENIDO PRINCIPAL ==================== */
.main-content {
  margin-top: 120px;
  padding: 60px 20px 100px;
  text-align: center;
  position: relative;
  z-index: 10;
}

.page-title {
  font-size: 3.5rem;
  font-weight: 700;
  color: #2c3e50;
  margin-bottom: 15px;
}

.page-subtitle {
  font-size: 1.2rem;
  color: #999;
  margin-bottom: 50px;
}

/* ==================== EMOJIS ==================== */
.emojis-container {
  display: flex;
  justify-content: center;
  gap: 40px;
  margin-bottom: 60px;
}

.emoji-btn {
  width: 80px;
  height: 80px;
  background: transparent;
  border: 2px solid #ddd;
  border-radius: 50%;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0;
}

.emoji-btn:hover {
  transform: scale(1.1);
  border-color: #ff6b35;
}

.emoji-btn.active {
  border: 2px solid #ff6b35;
  transform: scale(1.15);
  box-shadow: 0 8px 20px rgba(255, 107, 53, 0.3);
}

.emoji-img {
  width: 50px;
  height: 50px;
  object-fit: contain;
}

/* ==================== FORMULARIO ==================== */
.form-container {
  max-width: 700px;
  margin: 0 auto;
  background: #fef5e7;
  padding: 40px;
  border-radius: 30px;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.3);
}

.textarea-comentario {
  width: 100%;
  padding: 20px;
  background: #FFB381;
  border: none;
  border-radius: 20px;
  font-size: 1rem;
  color: #8b6f47;
  font-family: 'Montserrat','inherit';
  resize: none;
  margin-bottom: 30px;
  outline: none;
  text-align: center;
}

.textarea-comentario::placeholder {
  color: #555252;
  opacity: 0.8;
}

.btn-aceptar {
  width: 100%;
  max-width: 300px;
  padding: 16px 40px;
  background: #ff6b35;
  color: white;
  border: none;
  border-radius: 30px;
  font-weight: 600;
  font-size: 18px;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 12px rgba(255, 107, 53, 0.3);
}

.btn-aceptar:hover {
  background: #e55a2b;
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(255, 107, 53, 0.4);
}

/* ==================== MODAL ==================== */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  backdrop-filter: blur(4px);
}

.modal-content {
  background: white;
  border-radius: 20px;
  padding: 50px 60px;
  max-width: 500px;
  width: 90%;
  text-align: center;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
  animation: modalSlideIn 0.3s ease;
}

@keyframes modalSlideIn {
  from {
    opacity: 0;
    transform: translateY(-30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.modal-title {
  font-size: 2.2rem;
  font-weight: 700;
  color: #2c3e50;
  margin-bottom: 15px;
}

.modal-subtitle {
  font-size: 1.1rem;
  color: #666;
  margin-bottom: 35px;
  line-height: 1.5;
}

.btn-cerrar-modal {
  padding: 16px 60px;
  background: #ff6b35;
  color: white;
  border: none;
  border-radius: 30px;
  font-weight: 600;
  font-size: 18px;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 12px rgba(255, 107, 53, 0.3);
}

.btn-cerrar-modal:hover {
  background: #e55a2b;
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(255, 107, 53, 0.4);
}

/* ==================== RESPONSIVE ==================== */

/* Pantallas 1440px */
@media (min-width: 1440px){
  .navbar {
    padding: 22px 0% !important;
    max-width: 1910px;
    margin-left: 0%;
    margin-right: 0%;
  }

  .logo {
    font-size: 25px;
    margin-left: 40px;
  }

  .nav-links {
    gap: 70px;
    position: center;
  }

  .nav-links a {
    font-size: 15px;
  }

  .btn-admin,
  .btn-invitado {
    padding: 9px 32px;
    font-size: 14px;
  }

  .btn-cerrar-sesion {
    padding: 9px 26px;
    font-size: 14px;
    margin-right: 40px;
  }

  .main-content {
    padding:45px 20px 120px;
  }

  .page-title {
    font-size: 3.4rem;
    margin-bottom: 20px;
  }

  .page-subtitle {
    font-size: 1.4rem;
    margin-bottom: 20px;
  }

  .decoration-naranja{
    width: 220px;
  }
  .decoration-aceite {
    width: 200px;
  }

  .decoration-naranja {
    top: 90px;
    left: 15px;
  }

  .decoration-aceite {
    top: 35px;
    right: 0;
  }

  .decoration-guacamole {
    width: 350px;
    bottom: 0;
    left: 140px;
  }

  .decoration-estrella1 {
    width: 180px;
    bottom: 40px;
    right: 20px;
  }

  .decoration-estrella2 {
    width: 70px;
    bottom: 220px;
    right: 170px;
  }

  .emojis-container {
    gap: 50px;
    margin-bottom: 70px;
  }

  .emoji-btn {
    width: 90px;
    height: 90px;
    border: none;
  }

  .emoji-img {
    width: 80px;
    height: 80px;
  }

  .form-container {
    max-width: 800px;
    padding: 50px;
    border-radius: 35px;
  }

  .textarea-comentario {
    padding: 25px;
    font-size: 1.1rem;
    border-radius: 25px;
    margin-bottom: 35px;
  }

  .btn-aceptar {
    max-width: 350px;
    padding: 18px 50px;
    font-size: 19px;
  }

  .modal-content {
    max-width: 550px;
    padding: 55px 70px;
  }

  .modal-title {
    font-size: 2.4rem;
  }

  .modal-subtitle {
    font-size: 1.2rem;
  }

  .btn-cerrar-modal {
    padding: 18px 70px;
    font-size: 19px;
  }
}

@media (max-width: 1024px) {
  .navbar {
    padding: 20px 2% !important;
  }

  .page-title {
    font-size: 2.8rem;
  }

  .decoration-naranja,
  .decoration-aceite {
    width: 100px;
  }
}

@media (max-width: 768px) {
  .navbar {
    flex-wrap: wrap;
  }

  .nav-links {
    order: 3;
    width: 100%;
    justify-content: center;
    margin-left: 0;
    gap: 30px;
  }

  .page-title {
    font-size: 2.2rem;
  }

  .page-subtitle {
    font-size: 1rem;
  }

  .emojis-container {
    gap: 25px;
  }

  .emoji-btn {
    width: 70px;
    height: 70px;
  }

  .emoji-img {
    width: 40px;
    height: 40px;
  }

  .form-container {
    padding: 30px 20px;
  }

  .decoration-naranja,
  .decoration-aceite {
    width: 80px;
  }

  .decoration-guacamole {
    width: 100px;
  }

  .decoration-estrella1,
  .decoration-estrella2 {
    width: 50px;
  }
}

@media (max-width: 480px) {
  .page-title {
    font-size: 1.8rem;
  }

  .emojis-container {
    gap: 15px;
  }

  .emoji-btn {
    width: 60px;
    height: 60px;
  }

  .emoji-img {
    width: 35px;
    height: 35px;
  }

  .form-container {
    padding: 25px 15px;
  }

  .modal-content {
    padding: 40px 30px;
  }

  .modal-title {
    font-size: 1.8rem;
  }
}
</style>