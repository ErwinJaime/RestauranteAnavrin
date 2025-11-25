import { createRouter, createWebHistory } from 'vue-router'
import Login from '@/views/LoginForm.vue'
import Home from '@/views/HomePage.vue'
import Dashboard from '@/views/UserDashboard.vue'
import Registro from '@/views/RegisterForm.vue'
import Administrador from '@/views/InventarioPage.vue'
import ResenasAdmin from '@/views/ResenasAdmin.vue'
import About from '@/views/AboutPage.vue'
// Agregar las importaciones que faltan
import ResenasHome from '@/views/ResenasHome.vue'
import AboutHome from '@/views/AboutPageHome.vue'
import Menu from '@/views/MenuPage.vue'

const routes = [
  { path: '/', name: 'Menu', component: Menu },
  { path: '/login', name: 'Login', component: Login },
  { path: '/home', name: 'Home', component: Home },
  { path: '/administracion', name: 'Administrador', component: Administrador},
  { path: '/resenasadmin', name: 'ResenasAdmin', component: ResenasAdmin},
  { path: '/resenashome', name: 'ResenasHome', component: ResenasHome},
  { path: '/about', name: 'About', component: About},
  { path: '/abouthome', name: 'AboutHome', component: AboutHome},
  { path: '/dashboard', name: 'Dashboard', component: Dashboard },
  { path: '/registro', name: 'Registro', component: Registro },
  { path: '/menu', name: 'Menu', component: Menu },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

// ✅ GUARD: Proteger rutas
router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('access_token')
  const user = JSON.parse(localStorage.getItem('user') || '{}')
  
  // Definir rutas protegidas
  const protectedRoutes = ['/dashboard', '/administracion', '/resenasadmin', '/menu']
  const adminRoutes = ['/administracion', '/resenasadmin']
  
  // Si la ruta requiere autenticación
  if (protectedRoutes.includes(to.path) && !token) {
    next('/')  // Redirigir al login
    return
  }
  
  // Si la ruta requiere ser admin
  if (adminRoutes.includes(to.path) && !user.es_admin) {
    next('/dashboard')  // Redirigir al dashboard normal
    return
  }
  
  next()  // Permitir acceso
})

export default router