import { createRouter, createWebHistory } from 'vue-router'
import Login from '@/views/LoginForm.vue'
import Dashboard from '@/views/UserDashboard.vue'
import Registro from '@/views/RegisterForm.vue'

const routes = [
  { path: '/', name: 'Login', component: Login },
  { path: '/dashboard', name: 'Dashboard', component: Dashboard },
  { path: '/registro', name: 'Registro', component: Registro },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
