// Middleware de autenticación para Vue
import authService from '@/services/probar'

export function requireAuth(to, from, next) {
  if (authService.isAuthenticated()) {
    next()
  } else {
    next('/login')
  }
}

export function requireGuest(to, from, next) {
  if (!authService.isAuthenticated()) {
    next()
  } else {
    next('/dashboard')
  }
}
