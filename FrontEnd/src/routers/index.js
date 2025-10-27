import { createRouter, createWebHistory } from 'vue-router'
import LoginForm from '@/views/LoginForm.vue'
import UserDashboard from '@/views/UserDashboard.vue'
import RegisterForm from '@/views/RegisterForm.vue'

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

export default router