import { createRouter, createWebHistory } from 'vue-router'
import Login from '@/views/LoginForm.vue'
import Home from '@/views/HomePage.vue'
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

const routes = [
  { path: '/', name: 'homeCliente', component: homeCliente},
  { path: '/registro', name: 'Registro', component: Registro },
  { path: '/login', name: 'Login', component: Login },
  { path: '/home', name: 'Home', component: Home },
  { path: '/platillos', name: 'Platillos', component: Platillos },
  { path: '/administracion', name: 'Administrador', component: Administrador},
  { path: '/resenasadmin', name: 'ResenasAdmin', component: ResenasAdmin}, 
  { path: '/aboutadmin', name: 'About', component: About},
  { path: '/dashboard', name: 'Dashboard', component: Dashboard },
  { path: '/resenashome', name: 'ResenasHome', component: ResenasHome},
  { path: '/abouthome', name: 'AboutHome', component: AboutHome},
  { path: '/menu', name: 'Menu', component: Menu }, 
  { path: '/aboutcliente', name: 'AboutCliente', component: AboutCliente},
  { path: '/resenascliente', name: 'ResenasCliente', component: ResenasCliente}, 
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

// ✅ GUARD: Proteger rutas
router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('access_token')
  const user = JSON.parse(localStorage.getItem('user') || '{}')
  
  // Definir rutas protegidas (QUITÉ /menu de aquí)
  const protectedRoutes = ['/dashboard', '/administracion', '/resenasadmin']
  const adminRoutes = ['/administracion', '/resenasadmin']
  
  // Si la ruta requiere autenticación
  if (protectedRoutes.includes(to.path) && !token) {
    next('/login')  // ✅ Redirigir al login, no a '/'
    return
  }
  
  // Si la ruta requiere ser admin
  if (adminRoutes.includes(to.path) && !user.es_admin) {
    next('/dashboard')
    return
  }
  
  next()
})

export default router