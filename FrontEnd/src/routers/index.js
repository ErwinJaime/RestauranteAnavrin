/*FrontEnd\src\routers\index.js*/
import { createRouter, createWebHistory } from 'vue-router'
import Login from '@/views/LoginForm.vue'
import Home from '@/views/HomePage.vue'
import Bebidas from '@/views/BebidasPage.vue'
import Postres from '@/views/PostresPage.vue'
import Platillos from '@/views/PlatillosPage.vue'
import Dashboard from '@/views/UserDashboard.vue'
import Registro from '@/views/RegisterForm.vue'
import Administrador from '@/views/InventarioPage.vue'
import ResenasAdmin from '@/views/ResenasAdmin.vue'
import About from '@/views/AboutPage.vue'
import ResenasHome from '@/views/ResenasHome.vue'
import AboutHome from '@/views/AboutPageHome.vue'
import Menu from '@/views/MenuPage.vue'
import ResenasCliente from '@/views/ResenasCliente.vue'
import AboutCliente from '@/views/AboutCliente.vue'
import homeCliente from '@/views/homeCliente.vue'
import CrearResena from '@/views/CrearResena.vue'

const routes = [
  // ========== RUTAS PÚBLICAS ==========
  { 
    path: '/', 
    name: 'Home', 
    component: Home,
    meta: { requiresAuth: false }
  },
    { 
    path: '/resenashome', 
    name: 'ResenasHome', 
    component: ResenasHome,
    meta: { requiresAuth: false }
  },
  { 
    path: '/abouthome', 
    name: 'AboutHome', 
    component: AboutHome,
    meta: { requiresAuth: false }
  },
  { 
    path: '/registro', 
    name: 'Registro', 
    component: Registro,
    meta: { requiresAuth: false }
  },
  { 
    path: '/login', 
    name: 'Login', 
    component: Login,
    meta: { requiresAuth: false }
  },
    { 
    path: '/bebidas', 
    name: 'Bebidas', 
    component: Bebidas,
    meta: { requiresAuth: false}
  },
  { 
    path: '/postres', 
    name: 'Postres', 
    component: Postres,
    meta: { requiresAuth: false}
  },
  { 
    path: '/platillos', 
    name: 'Platillos', 
    component: Platillos,
    meta: { requiresAuth: false}
  },

  // ========== RUTAS DE CLIENTE (requieren autenticación) ==========
  { 
    path: '/homeCliente', 
    name: 'homeCliente', 
    component: homeCliente,
    meta: { requiresAuth: true, role: 'cliente' }
  },
  { 
    path: '/menu', 
    name: 'Menu', 
    component: Menu,
    meta: { requiresAuth: true, role: 'cliente' }
  },
  { 
    path: '/aboutcliente', 
    name: 'AboutCliente', 
    component: AboutCliente,
    meta: { requiresAuth: false, role: 'cliente' }
  },
  { 
    path: '/resenascliente', 
    name: 'ResenasCliente', 
    component: ResenasCliente,
    meta: { requiresAuth: false, role: 'cliente' }
  },
  { 
    path: '/crearresena', 
    name: 'CrearResena', 
    component: CrearResena,
    meta: { requiresAuth: true, role: 'cliente' }
  },
  { 
    path: '/dashboard', 
    name: 'Dashboard', 
    component: Dashboard,
    meta: { requiresAuth: true, role: 'cliente' }
  },

  // ========== RUTAS DE ADMINISTRADOR ==========
  { 
    path: '/administracion', 
    name: 'Administrador', 
    component: Administrador,
    meta: { requiresAuth: true, role: 'admin' }
  },
  { 
    path: '/resenasadmin', 
    name: 'ResenasAdmin', 
    component: ResenasAdmin,
    meta: { requiresAuth: true, role: 'admin' }
  },
  { 
    path: '/aboutadmin', 
    name: 'About', 
    component: About,
    meta: { requiresAuth: true, role: 'admin' }
  },


  // ========== RUTA 404 - NO ENCONTRADO ==========
  { 
    path: '/:pathMatch(.*)*', 
    name: 'NotFound',
    component: () => import('@/views/NotFound.vue'),
    meta: { requiresAuth: false }
  },
  // ========== Contenido no disponible
  { 
  path: '/contenido-no-disponible', 
  name: 'ContenidoNoDisponible',
  component: () => import('@/views/ContenidoNoDisponible.vue'),
  meta: { requiresAuth: false }
}
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

// ========== FUNCIONES AUXILIARES ==========
const verificarToken = () => {
  const token = localStorage.getItem('access_token')
  if (!token) return false
  
  try {
    // Verificar si el token está expirado (si usas JWT)
    const payload = JSON.parse(atob(token.split('.')[1]))
    const expiracion = payload.exp * 1000 // Convertir a milisegundos
    
    if (Date.now() >= expiracion) {
      // Token expirado, limpiar localStorage
      localStorage.removeItem('access_token')
      localStorage.removeItem('refresh_token')
      localStorage.removeItem('user')
      return false
    }
    
    return true
  } catch (error) {
    // Si hay error al decodificar, asumir token inválido
    console.error('Token inválido:', error)
    localStorage.removeItem('access_token')
    localStorage.removeItem('refresh_token')
    localStorage.removeItem('user')
    return false
  }
}

const obtenerUsuario = () => {
  try {
    return JSON.parse(localStorage.getItem('user') || '{}')
  } catch {
    return {}
  }
}

// ========== GUARDIA DE NAVEGACIÓN GLOBAL ==========
router.beforeEach((to, from, next) => {
  const tokenValido = verificarToken()
  const user = obtenerUsuario()
  const esAdmin = user.es_admin === true || user.role === 'admin'
  
  // ========== 1. VERIFICAR SI LA RUTA REQUIERE AUTENTICACIÓN ==========
  if (to.meta.requiresAuth && !tokenValido) {
    next('/login')
    return
  }
  
  // ========== 2. VERIFICAR PERMISOS DE ROL ==========
  if (to.meta.role === 'admin' && !esAdmin) {
    next('/contenido-no-disponible')
    return
  }
  
  if (to.meta.role === 'cliente' && esAdmin) {
    // Si un admin intenta acceder a rutas de cliente, redirigir a admin
    next('/administracion')
    return
  }
  
  // ========== 3. EVITAR QUE USUARIOS LOGUEADOS VEAN LOGIN/REGISTRO ==========
  if ((to.path === '/login' || to.path === '/registro') && tokenValido) {
    if (esAdmin) {
      next('/administracion')
    } else {
      next('/homeCliente')
    }
    return
  }
  
  // ========== 4. REDIRIGIR HOME SEGÚN ROL ==========
  if (to.path === '/' && tokenValido) {
    if (esAdmin) {
      next('/administracion')
    } else {
      next('/homeCliente')
    }
    return
  }
  
  // ========== 5. PERMITIR NAVEGACIÓN ==========
  next()
})

export default router