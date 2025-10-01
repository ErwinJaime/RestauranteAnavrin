import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue'
import Registro from '../views/RegistroUsuario.vue'
import Home from '../views/HomePage.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/login', component: Login },
  { path: '/registro', component: Registro }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
