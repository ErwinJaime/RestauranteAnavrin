import { createRouter, createWebHistory } from 'vue-router'
import Login from '@/views/LoginForm.vue'
import Home from '@/views/HomePage.vue'
import Platillos from '@/views/PlatillosPage.vue'
import Dashboard from '@/views/UserDashboard.vue'
import Registro from '@/views/RegisterForm.vue'
import Administrador from '@/views/InventarioPage.vue'
import ResenasAdmin from '@/views/ResenasAdmin.vue'
import About from '@/views/AboutPage.vue'
import AboutHome from '@/views/AboutPageHome.vue'
import ResenasHome from '@/views/ResenasHome.vue'

const routes = [
  { path: '/', name: 'Login', component: Login },
  { path: '/home', name: 'Home', component: Home },
  { path: '/platillos', name: 'Platillos', component: Platillos },
  { path: '/administracion', name: 'Administrador', component: Administrador},
  { path: '/resenasadmin', name: 'ResenasAdmin', component: ResenasAdmin},
  { path: '/resenashome', name: 'ResenasHome', component: ResenasHome},
  { path: '/about', name: 'About', component: About},
  { path: '/abouthome', name: 'AboutHome', component: AboutHome},
  { path: '/dashboard', name: 'Dashboard', component: Dashboard },
  { path: '/registro', name: 'Registro', component: Registro },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

// ✅ GUARD: Proteger rutas
router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('access_token')
  const user = JSON.parse(localStorage.getItem('user') || '{}')
  
  // Si la ruta requiere autenticación
  if (to.meta.requiresAuth && !token) {
    next('/')  // Redirigir al login
    return
  }
  
  // Si la ruta requiere ser admin
  if (to.meta.requiresAdmin && !user.es_admin) {
    next('/dashboard')  // Redirigir al dashboard normal
    return
  }
  
  next()  // Permitir acceso
})

export default router