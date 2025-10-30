import { createApp } from 'vue'
import App from './App.vue'
import router from './routers'
import vue3GoogleLogin from 'vue3-google-login'

const app = createApp(App)

// Configurar Google Login
const GOOGLE_CLIENT_ID = process.env.VUE_APP_GOOGLE_CLIENT_ID

if (GOOGLE_CLIENT_ID) {
  app.use(vue3GoogleLogin, {
    clientId: GOOGLE_CLIENT_ID
  })
} else {
  console.warn('⚠️ GOOGLE_CLIENT_ID no está configurado en .env')
}

app.use(router)
app.mount('#app')