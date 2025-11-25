<template>
  <div class="menu-container">
    <!-- Navegación -->
    <nav class="navbar">
      <h1 class="logo">ANAVRIN</h1>
      <div class="nav-links">
        <router-link to="/homecliente">Home</router-link>
        <router-link to="/aboutcliente">About</router-link>
        <router-link to="/resenascliente">Review</router-link>
      </div>
      <span v-if="usuarioNombre !== 'Invitado'" class="btn-admin">{{ usuarioNombre }}</span>
      <span v-else class="btn-invitado">Tatiana</span>
      <button class="btn-cerrar-sesion" @click="cerrarSesion">
        {{ 'Cerrar Sesión' }}
      </button>
    </nav>

    <!-- Hero Section con título Menú -->
    <div class="hero-section">
      <img src="@/assets/naranja.png" alt="citrus" class="img-naranja" />
      <h1 class="menu-title">Menú</h1>
      <img src="@/assets/aceite.png" alt="glass" class="img-aceite" />
    </div>

    <!-- Contenido Principal del Menú -->
    <div class="main-content">
      <!-- Filtros -->
      <div class="filtros-container">
        <button 
          v-for="categoria in categorias" 
          :key="categoria.key"
          :class="['filtro-btn', categoriaFiltro === categoria.key ? 'active' : '']"
          @click="filtrarPorCategoria(categoria.key)"
        >
          {{ categoria.label }}
        </button>
      </div>

      <!-- Loading State -->
      <div v-if="cargando" class="loading-container">
        <p>Cargando productos...</p>
      </div>

      <!-- Lista de Productos -->
      <div v-else class="productos-container">
        <div 
          v-for="producto in productosFiltrados" 
          :key="producto.id"
          class="producto-card"
        >
          <div class="producto-imagen-wrapper">
            <img 
              v-if="producto.imagen" 
              :src="producto.imagen" 
              :alt="producto.nombre"
              class="imagen-producto"
            />
            <div v-else class="imagen-placeholder">
              🍽️
            </div>
          </div>
          <div class="producto-info">
            <h3 class="producto-nombre">{{ producto.nombre }}</h3>
            <p class="producto-ingredientes">{{ producto.ingredientes }}</p>
            <div class="producto-footer">
              <span class="producto-precio">${{ formatPrecio(producto.precio) }}</span>
              <div class="cantidad-controls">
                <button 
                  class="btn-cantidad" 
                  @click="decrementarCantidad(producto)"
                  :disabled="getCantidad(producto.id) === 0"
                >
                  -
                </button>
                <span class="cantidad">{{ getCantidad(producto.id) }}</span>
                <button 
                  class="btn-cantidad" 
                  @click="incrementarCantidad(producto)"
                  :disabled="!producto.disponible"
                >
                  +
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- Mensaje cuando no hay productos -->
        <div v-if="productosFiltrados.length === 0 && !cargando" class="no-productos">
          <p>No hay productos disponibles en esta categoría.</p>
        </div>
      </div>

      <!-- Decoración hojas -->
      <img src="@/assets/hoja2.png" alt="leaf" class="leaf-decoration dos" />
      <img src="@/assets/huevosMenu.png" alt="huevo" class="decoration-huevos" />

    </div>

    <!-- Carrito Resumen - SOLO se muestra si hay productos en el carrito -->
    <div v-if="totalProductosEnCarrito > 0" class="carrito-resumen">
      <div class="carrito-content">
        <div class="carrito-info">
          <span class="carrito-total-items">{{ totalProductosEnCarrito }} producto(s) en carrito</span>
          <span class="carrito-total">Total: ${{ formatPrecio(totalCarrito) }}</span>
        </div>
        <button class="btn-confirmar-pedido" @click="confirmarPedido">
          {{ usuarioNombre !== 'Invitado' ? 'Confirmar Pedido' : 'Iniciar Sesión para Pedir' }}
        </button>
      </div>
    </div>

    <!-- Footer -->
    <footer class="footer">
      <div class="footer-bottom">
        <p class="footer-slogan">El encuentro perfecto entre lo auténtico y lo inolvidable</p>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import { useRouter } from 'vue-router';
import { crearPedido } from '@/services/productos';
import { listarProductosPublicos } from '@/services/publicApi';

const router = useRouter();

// Estados
const productos = ref([]);
const cargando = ref(false);
const categoriaFiltro = ref('platillo');
const carrito = ref({});
const usuarioNombre = ref('');

// Categorías disponibles
const categorias = ref([
  { key: 'platillo', label: 'Platillos' },
  { key: 'postre', label: 'Postre' },
  { key: 'bebida', label: 'Bebidas' }
]);

const obtenerUsuario = () => {
  const usuario = JSON.parse(localStorage.getItem('user') || '{}');
  usuarioNombre.value = usuario.nombre || 'Invitado';
};

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

const filtrarPorCategoria = (categoria) => {
  categoriaFiltro.value = categoria;
};

const productosFiltrados = computed(() => {
  return productos.value.filter(producto => 
    producto.categoria === categoriaFiltro.value
  );
});

const formatPrecio = (precio) => {
  return parseFloat(precio).toLocaleString('es-CO');
};

const incrementarCantidad = (producto) => {
  if (!producto.disponible) return;
  
  if (!carrito.value[producto.id]) {
    carrito.value[producto.id] = { 
      producto, 
      cantidad: 0,
      precio_unitario: parseFloat(producto.precio)
    };
  }
  carrito.value[producto.id].cantidad++;
};

const decrementarCantidad = (producto) => {
  if (carrito.value[producto.id] && carrito.value[producto.id].cantidad > 0) {
    carrito.value[producto.id].cantidad--;
    if (carrito.value[producto.id].cantidad === 0) {
      delete carrito.value[producto.id];
    }
  }
};

const getCantidad = (productoId) => {
  return carrito.value[productoId]?.cantidad || 0;
};

const totalProductosEnCarrito = computed(() => {
  return Object.values(carrito.value).reduce((total, item) => total + item.cantidad, 0);
});

const totalCarrito = computed(() => {
  return Object.values(carrito.value).reduce((total, item) => {
    return total + (item.cantidad * item.precio_unitario);
  }, 0);
});

const confirmarPedido = async () => {
  if (!localStorage.getItem('access_token')) {
    alert('Por favor inicia sesión para realizar un pedido');
    router.push('/');
    return;
  }

  if (totalProductosEnCarrito.value === 0) {
    alert('No hay productos en el carrito');
    return;
  }

  try {
    const pedidos = Object.values(carrito.value).map(item => ({
      producto: item.producto.id,
      cantidad: item.cantidad,
      direccion_entrega: "Recoger en tienda"
    }));

    for (const pedido of pedidos) {
      await crearPedido(pedido);
    }

    alert('Pedido confirmado correctamente!');
    carrito.value = {};
    
  } catch (error) {
    console.error('Error al confirmar pedido:', error);
    if (error.response?.status === 401) {
      alert('Sesión expirada. Por favor inicia sesión nuevamente.');
      cerrarSesion();
    } else {
      alert('Error al confirmar el pedido. Por favor intenta nuevamente.');
    }
  }
};

const cargarProductos = async () => {
  try {
    cargando.value = true;
    console.log('🔄 Cargando productos desde API pública...');
    const response = await listarProductosPublicos();
    productos.value = response.data;
    console.log('✅ Productos cargados:', response.data.length);
  } catch (error) {
    console.error('❌ Error cargando productos:', error);
    console.error('Detalles del error:', error.response?.data);
    alert('Error al cargar los productos. Verifica la conexión con el servidor.');
  } finally {
    cargando.value = false;
  }
};

onMounted(() => {
  obtenerUsuario();
  cargarProductos();
});
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.menu-container {
  min-height: 100vh;
  background-color: #ffffff;
  font-family: 'Open Sans', sans-serif;
}

/* ==================== NAVBAR ==================== */
.navbar {
  position: absolute !important;
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
  font-weight: 700;
  color: #1a1a1a;
  letter-spacing: 2px;
  margin-left: 10px;
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
  background-color: #ff6b35;
  border: none;
  border-radius: 50px;
  cursor: default;
  font-weight: 600;
  white-space: nowrap;
  flex-shrink: 0;
  margin-left: 10px;
  margin-right: 5px;
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
  margin-right: -60px;
}

.btn-cerrar-sesion:hover {
  background-color: #6d9fef;
  color: #ffffff;
  border-color: #6d9fef;
}

/* ==================== HERO SECTION ==================== */
.hero-section {
  margin-top: 80px;
  padding: 60px 20px 40px;
  text-align: center;
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 40px;
}

.menu-title {
  font-size: 4rem;
  font-weight: bold;
  color: #000000;
  letter-spacing: -1px;
  
}

.img-naranja{
  position: absolute;
  object-fit: contain;
  z-index: 10;
  opacity: 0.9;
  top: 80px;
  left: 40px;
  width: 140px;
}
.img-aceite {
  position: absolute;
  object-fit: contain;
  z-index: 10;
  opacity: 0.9;
  top: 70px;
  right: 40px;
  width: 140px;
}

/* ==================== MAIN CONTENT ==================== */
.main-content {
  padding: 40px 0px 100px;
  position: relative;
  min-height: 800px;
}

/* ==================== FILTROS ==================== */
.filtros-container {
  display: flex;
  justify-content: center;
  gap: 20px;
  margin-bottom: 60px;
  padding: 0;
}

.filtro-btn {
  margin-right: 100px;
  margin-left: 100px;
  padding: 14px 40px;
  border: none;
  background-color: #7cb342;
  color: white;
  border-radius: 30px;
  cursor: pointer;
  font-weight: 600;
  font-size: 17px;
  transition: all 0.3s ease;
  box-shadow: 0 2px 8px rgba(124, 179, 66, 0.3);
}

.filtro-btn.active {
  background-color: #ff6b35;
  box-shadow: 0 4px 12px rgba(255, 107, 53, 0.4);
  transform: translateY(-2px);
}

.filtro-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(124, 179, 66, 0.5);
}

.filtro-btn.active:hover {
  box-shadow: 0 4px 12px rgba(255, 107, 53, 0.6);
}

/* ==================== LOADING ==================== */
.loading-container {
  text-align: center;
  padding: 80px 20px;
  color: #666;
  font-size: 1.2rem;
}

/* ==================== PRODUCTOS ==================== */
.productos-container {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 40px 20px;  
  max-width: 1100px;
  margin: 0 auto;
  padding: 0 20px;
  justify-items: center;
}

.producto-card {
  position: relative;
  background: transparent;
  width: 100%;
  max-width: 340px;
  padding-top: 120px;
  transition: transform 0.3s ease;
}

.producto-card:hover {
  transform: translateY(-5px);
}

.producto-imagen-wrapper {
  position: absolute;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 240px;
  height: 240px;
  z-index: 2;
}

.imagen-producto {
  width: 240px;
  height: 240px;
  border-radius: 50%;
  object-fit: cover;
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.15);
}

.imagen-placeholder {
  width: 240px;
  height: 240px;
  border-radius: 50%;
  background: #e0e0e0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 4rem;
  color: #999;
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.15);
}

.producto-info {
  background: #F5EFEF;
  border-radius: 20px;
  padding: 140px 25px 25px;
  position: relative;
  z-index: 1;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
}

.producto-nombre {
  font-size: 1.4rem;
  font-weight: 700;
  color: #000000;
  margin-bottom: 10px;
  text-align: center;
  font-family: 'Source Serif Pro', serif;
}

.producto-ingredientes {
  color: #6b6b6b;
  margin-bottom: 20px;
  font-size: 0.85rem;
  line-height: 1.6;
  text-align: center;
  min-height: 80px;
  font-family: 'Source Serif Pro', serif;
}

.producto-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 15px;
}

.producto-precio {
  font-size: 1.5rem;
  font-weight: 700;
  color: #7cb342;
  font-family: 'Source Serif Pro', serif;
}

.cantidad-controls {
  display: flex;
  align-items: center;
  gap: 12px;
}

.btn-cantidad {
  width: 36px;
  height: 36px;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s ease;
  font-weight: 600;
  font-size: 20px;
  color: #ff6b35;
}

.btn-cantidad:hover:not(:disabled) {
  background: #ff6b35;
  color: white;
  transform: scale(1.05);
}

.btn-cantidad:disabled {
  cursor: not-allowed;
  box-shadow: none;
  
}

.cantidad {
  background: #ffffff;
  width: 36px;
  height: 36px;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  min-width: 25px;
  text-align: center;
  font-size: 1.1rem;
  color: #2c3e50;
}

/* ==================== NO PRODUCTOS ==================== */
.no-productos {
  grid-column: 1 / -1;
  text-align: center;
  padding: 80px 20px;
  color: #999;
  font-size: 1.2rem;
}

/* ==================== DECORACIONES ==================== */
.leaf-decoration {
  position: absolute;
  width: 80px;
  height: auto;
  pointer-events: none;
  z-index: 5;
}

.leaf-decoration.left {
  left: 20px;
  top:  200px;
  margin-left: -82px;
  transform: rotate(-130deg);
}
.leaf-decoration.dos{
  width: 130px;
  height: auto;
  left: 20px;
  top: 600px;
  margin-left: -82px;
}

.leaf-decoration.right {
  right: 20px;
  bottom: 200px;
}
.decoration-guacamole {
  position: absolute;
  margin-left: -82px;
  width: 200px;
  height: auto;
  pointer-events: none;
  z-index: 5;
  left: 20px;
  bottom: 600px;  /* ← Fijo desde el bottom del contenedor */
  transform: rotate(90deg);
}

.decoration-huevos {
  position: absolute;
  width: 120px;
  height: auto;
  pointer-events: none;
  z-index: 5;
  right: 20px;
  margin-right: -20px;
  bottom: 500px;  /* ← Fijo desde el bottom del contenedor */
}
/* ==================== CARRITO RESUMEN ==================== */
.carrito-resumen {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  background: white;
  box-shadow: 0 -4px 15px rgba(0, 0, 0, 0.1);
  padding: 20px;
  z-index: 40;
}

.carrito-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1200px;
  margin: 0 auto;
  gap: 20px;
}

.carrito-info {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.carrito-total-items {
  font-size: 0.9rem;
  color: #666;
  font-weight: 500;
}

.carrito-total {
  font-size: 1.5rem;
  font-weight: 700;
  color: #ff6b35;
}

.btn-confirmar-pedido {
  padding: 14px 40px;
  background: #ff6b35;
  color: white;
  border: none;
  border-radius: 30px;
  font-weight: 600;
  font-size: 16px;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 12px rgba(255, 107, 53, 0.3);
}

.btn-confirmar-pedido:hover {
  background: #e55a2b;
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(255, 107, 53, 0.4);
}

/* ==================== FOOTER ==================== */
.footer {
  background: #ffffff;
  padding: 80px 20px 0;
  margin-top: 100px;
  position: relative;
}

.footer-content {
  max-width: 1000px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 30px;
  padding: 0 0px 60px;
}

.footer-hojas-left {
  display: flex;
  align-items: center;
  gap: 15px;
  flex-shrink: 0;
}

.footer-icon-heart {
  margin-top: -200px;
  width: 200px;
  height: auto;
}

.footer-icon-leaf {
  margin-top: -300px;
  width: 55px;
  height: auto;
}

.footer-center {
  flex: 1;
  display: flex;
  align-items: center;
  gap: 30px;
  max-width: 500px;
}

.footer-title {
  font-size: 2.5rem;
  color: #000000;
  line-height: 1.4;
  font-weight: 700;
  margin: 0;
}

.btn-crear-resena {
  padding: 14px 40px;
  background: #ff6b35;
  color: white;
  border: none;
  border-radius: 30px;
  font-weight: 600;
  font-size: 16px;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 12px rgba(255, 107, 53, 0.3);
  white-space: nowrap;
  flex-shrink: 0;
}

.btn-crear-resena:hover {
  background: #6d9fef;
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(255, 107, 53, 0.4);
}

.footer-hojas-right {
  
  display: flex;
  flex-direction: column;
  gap: 10px;
  align-items: flex-end;
  flex-shrink: 0;
}

.footer-leaf-top {
  
  width: 70px;
  height: auto;
  margin-right: 20px;
}

.footer-leaf-bottom {
  width: 75px;
  height: auto;
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

/* ==================== RESPONSIVE ==================== */


/* Pantallas grandes (1600px o más) */
@media (min-width: 1440px) {
  .navbar {
    padding: 25px 8% !important;
    max-width: 2000px;
    margin: 0 auto;
  }

  .logo {
    font-size: 24px;
    margin-left: -45px;
  }

  .nav-links {
    gap: 100px;
  }

  .nav-links a {
    font-size: 16px;
  }

  .btn-admin,
  .btn-invitado {
    padding: 10px 35px;
    font-size: 15px;
  }

  .btn-cerrar-sesion {
    padding: 10px 28px;
    font-size: 15px;
  }

  .hero-section {
    padding: 80px 40px 30px;
    gap: 60px;
  }

  .menu-title {
    font-size: 3.4rem;
  }

  .img-naranja{
    margin-top: -80px;
    margin-left: -100px;
    width: 200px;
  }
  .img-aceite {
    width: 200px;
    margin-right: -40px;
  }

  .filtros-container {
    gap: 30px 40px;
    margin-bottom: 80px;
  }

  .filtro-btn {
    padding: 16px 40px;
    font-size: 18px;
  }

  .productos-container {
    grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
    gap: 90px 5px;  
    max-width: 1300px;
    margin-bottom: 10px;
  }

  .producto-card {
    max-width:320px;
    padding-top: 160px;
  }

  .producto-imagen-wrapper {
    width: 200px;
    height: 220px;
  }

  .imagen-producto,
  .imagen-placeholder {
    width: 200px;
    height: 200px;
  }

  .producto-info {
    padding: 80px 30px 30px;
  }

  .producto-nombre {
    font-size: 1.6rem;
    margin-bottom: 10px;
  }

  .producto-ingredientes {
    font-size: 0.95rem;
    line-height: 1.7;
    min-height: 90px;
  }

  .producto-precio {
    font-size: 1.7rem;
  }

  .btn-cantidad {
    width: 40px;
    height: 40px;
    font-size: 22px;
  }

  .cantidad {
    font-size: 1.2rem;
    min-width: 30px;
  }

  .leaf-decoration {
    width: 100px;
  }

  .leaf-decoration.left {
    left: 50px;
    bottom: 250px;
  }

  .leaf-decoration.right {
    right: 50px;
    top: 350px;
  }

  .carrito-resumen {
    padding: 25px 40px;
  }

  .carrito-content {
    max-width: 1600px;
  }

  .carrito-total-items {
    font-size: 1rem;
  }

  .carrito-total {
    font-size: 1.7rem;
  }

  .btn-confirmar-pedido {
    padding: 16px 50px;
    font-size: 18px;
  }

  .footer {
    padding: 0 0 0;
    margin-top:40px;
  }

  .footer-content {
    max-width: 1400px;
    gap: 50px;
    padding: -20px 10px 80px;   
  }
 
  .footer-icon-heart {
    width: 280px;
    margin-top: -60px;
    margin-left: -30px;
  }

  .footer-icon-leaf {
    width: 100px;
  }

  .footer-title {
    font-size: 3rem;
    margin-bottom: 30px;
    margin-left: -120px;
    margin-right: 1px;

  }

  .btn-crear-resena {
    padding: 14px 30px;
    font-size: 18px;
    margin-right: -135px;
  }
/*hoja pequeña de la derecha*/
  .footer-leaf-top {
    width: 85px;
    margin-right: 0px;
  }
/*hoja grande de la derecha*/ 
  .footer-leaf-bottom {
    width: 280px;
    margin-right: -80px;
  }

  .footer-bottom {
    padding: 30px 20px;
  }

  .footer-slogan {
    font-size: 1.05rem;
  }
}
@media (max-width: 1200px) {
  .navbar {
    padding: 20px 2% !important;
    gap: 10px !important;
  }

  .logo {
    font-size: 17px;
  }

  .nav-links {
    gap: 40px;
    margin-left: 50px;
  }

  .nav-links a {
    font-size: 13px;
  }

  .btn-admin,
  .btn-invitado {
    padding: 7px 20px;
    font-size: 12px;
  }

  .btn-cerrar-sesion {
    padding: 7px 16px;
    font-size: 12px;
  }

  .menu-title {
    font-size: 3rem;
  }

  .img-naranja,
  .img-aceite {
    width: 0px;
  }
}

@media (max-width: 768px) {
  .hero-section {
    gap: 20px;
    padding: 40px 20px 30px;
  }

  .menu-title {
    font-size: 2.5rem;
  }

  .img-naranja,
  .img-aceite {
    width: 60px;
  }

  .productos-container {
    grid-template-columns: 1fr;
    gap: 30px;
    padding: 0 10px;
  }

  .producto-card {
    max-width: 100%;
  }

  .filtros-container {
    flex-wrap: wrap;
    gap: 12px;
  }

  .filtro-btn {
    padding: 12px 30px;
    font-size: 14px;
  }

  .carrito-content {
    flex-direction: column;
    gap: 15px;
    text-align: center;
  }

  .main-content {
    padding: 30px 0px 120px;
  }

  .footer {
    padding: 60px 20px 0;
  }

  .footer-content {
    flex-direction: column;
    gap: 30px;
    padding: 0 20px 40px;
    text-align: center;
  }

  .footer-center {
    text-align: center;
  }

  .footer-hojas-left,
  .footer-hojas-right {
    justify-content: center;
  }

  .footer-icon-heart,
  .footer-icon-leaf {
    width: 40px;
  }

  .footer-leaf-top,
  .footer-leaf-bottom {
    width: 50px;
  }

  .footer-title {
    font-size: 1.3rem;
  }

  .leaf-decoration {
    display: none;
  }

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
}

@media (max-width: 480px) {
  .menu-title {
    font-size: 2rem;
  }

  .img-naranja,
  .img-aceite {
    width: 40px;
  }

  .producto-nombre {
    font-size: 1.3rem;
  }

  .producto-precio {
    font-size: 1.3rem;
  }

  .footer-title {
    font-size: 1.1rem;
  }

  .footer-icon-heart,
  .footer-icon-leaf {
    width: 35px;
  }

  .footer-leaf-top,
  .footer-leaf-bottom {
    width: 45px;
  }

  .btn-crear-resena {
    padding: 12px 30px;
    font-size: 14px;
  }
}
</style>