<template>
  <div id="app">
    <!-- Mostrar formulario de login o registro según el estado -->
    <LoginForm 
      v-if="!showRegister" 
      @login-success="handleLoginSuccess"
      @switch-to-register="showRegister = true"
    />
    <RegisterForm 
      v-else 
      @register-success="handleRegisterSuccess"
      @switch-to-login="showRegister = false"
    />
    
    <!-- Dashboard simple para usuarios autenticados -->
    <div v-if="user" class="dashboard">
      <div class="dashboard-header">
        <h1>¡Bienvenido, {{ user.nombre }}!</h1>
        <button @click="logout" class="logout-button">Cerrar Sesión</button>
      </div>
      <div class="dashboard-content">
        <p>Has iniciado sesión correctamente.</p>
        <p>Email: {{ user.correo }}</p>
        <p>ID: {{ user.id }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import LoginForm from './components/LoginForm.vue'
import RegisterForm from './components/RegisterForm.vue'
import authService from './services/authService'

export default {
  name: 'App',
  components: {
    LoginForm,
    RegisterForm
  },
  data() {
    return {
      showRegister: false,
      user: null
    }
  },
  mounted() {
    // Verificar si hay un usuario autenticado al cargar la app
    if (authService.isAuthenticated()) {
      this.user = authService.getUser()
    }
  },
  methods: {
    handleLoginSuccess(user) {
      this.user = user
      this.showRegister = false
    },
    
    handleRegisterSuccess() {
      // Después del registro exitoso, mostrar el formulario de login
      this.showRegister = false
    },
    
    logout() {
      authService.logout()
      this.user = null
    }
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@500;600&display=swap');

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

#app {
  height: 100vh;
  font-family: 'Poppins', sans-serif;
}

.dashboard {
  height: 100vh;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 2rem;
}

.dashboard-header {
  text-align: center;
  margin-bottom: 2rem;
}

.dashboard-header h1 {
  font-size: 2.5rem;
  color: #333;
  margin-bottom: 1rem;
  font-weight: 600;
}

.logout-button {
  background: linear-gradient(135deg, #ff6b35, #f7931e);
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 500;
  font-family: 'Poppins', sans-serif;
  cursor: pointer;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.logout-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(255, 107, 53, 0.3);
}

.dashboard-content {
  background: white;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  text-align: center;
  max-width: 500px;
  width: 100%;
}

.dashboard-content p {
  font-size: 1.1rem;
  color: #666;
  margin-bottom: 0.5rem;
  font-weight: 500;
}

.dashboard-content p:first-child {
  color: #333;
  font-weight: 600;
  margin-bottom: 1rem;
}
</style>
