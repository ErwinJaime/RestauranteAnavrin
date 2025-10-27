import { createRouter, createWebHistory } from 'vue-router'
import LoginForm from '@/views/LoginForm.vue'
import UserDashboard from '@/views/UserDashboard.vue'
import RegisterForm from '@/views/RegisterForm.vue'
import AdminDashboard from '@/views/AdminDashboard.vue'
const routes = [
  { 
    path: '/', 
    name: 'Login', 
    component: LoginForm  // ✅ Cambiar Login por LoginForm
  },
  { 
    path: '/login', 
    redirect: '/' 
  },
  { 
    path: '/dashboard', 
    name: 'Dashboard', 
    component: UserDashboard  // ✅ Nombre completo
  },
  { path: '/admin-dashboard',
    name: 'AdminDashboard',
    component: AdminDashboard,
    meta: { requiresAuth: true, requiresAdmin: true }
  },
  { 
    path: '/registro', 
    name: 'Registro', 
    component: RegisterForm  // ✅ Nombre completo
  },
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