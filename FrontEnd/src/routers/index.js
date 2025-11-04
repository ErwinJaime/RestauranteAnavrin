import { createRouter, createWebHistory } from 'vue-router'
/*import Login from '@/views/LoginForm.vue'*/
import Dashboard from '@/views/UserDashboard.vue'
import Registro from '@/views/RegisterForm.vue'
import Administrador from '@/views/InventarioPage.vue'

const routes = [
  { path: '/', name: 'Administrador', component: Administrador},
  /*{ path: '/', name: 'Login', component: Login },*/
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