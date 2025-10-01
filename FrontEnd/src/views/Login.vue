<template>
  <div class="login-page">
    <!-- Imagen de fondo lado izquierdo -->
    <div class="left-section">
      <!-- Línea naranja lateral -->
      <div class="orange-line"></div>
      <!-- Imagen del chef -->
      <img src="@/assets/chef-image.jpg" alt="Chef" class="chef-image">
      <div class="image-overlay"></div>
    </div>
    
    <!-- Formulario lado derecho -->
    <div class="right-section">
      <!-- Logo/Título en esquina superior derecha -->
      <div class="header">
        <h1 class="brand">ANAVRIN</h1>
      </div>
      
      <div class="login-container">
        <!-- Título del formulario -->
        <h2 class="login-title">Inicia Sesión</h2>
        
        <!-- Formulario -->
        <form @submit.prevent="handleLogin" class="login-form">
          <!-- Campo Email -->
          <div class="input-group">
            <div class="input-container">
              <svg class="input-icon" width="20" height="20" viewBox="0 0 24 24" fill="none">
                <path d="M3 8L10.89 13.26C11.2187 13.4793 11.6049 13.5963 12 13.5963C12.3951 13.5963 12.7813 13.4793 13.11 13.26L21 8M5 19H19C20.1046 19 21 18.1046 21 17V7C21 5.89543 20.1046 5 19 5H5C3.89543 5 3 5.89543 3 7V17C3 18.1046 3.89543 19 5 19Z" stroke="#666" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              <input 
                v-model="email"
                type="email" 
                placeholder="Correo electrónico"
                required
                class="form-input"
              >
            </div>
          </div>
          
          <!-- Campo Contraseña -->
          <div class="input-group">
            <div class="input-container">
              <svg class="input-icon" width="20" height="20" viewBox="0 0 24 24" fill="none">
                <path d="M16 12V8C16 5.79086 14.2091 4 12 4C9.79086 4 8 5.79086 8 8V12M12 15C12.5523 15 13 14.5523 13 14C13 13.4477 12.5523 13 12 13C11.4477 13 11 13.4477 11 14C11 14.5523 11.4477 15 12 15ZM7 12H17C18.1046 12 19 12.8954 19 14V18C19 19.1046 18.1046 20 17 20H7C5.89543 20 5 19.1046 5 18V14C5 12.8954 5.89543 12 7 12Z" stroke="#666" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              <input 
                v-model="password"
                type="password" 
                placeholder="Contraseña"
                required
                class="form-input"
              >
            </div>
          </div>
          
          <!-- Enlace olvidé contraseña -->
          <div class="forgot-password">
            <a href="#" class="forgot-link">Olvidé mi contraseña</a>
          </div>
          
          <!-- Botón Entrar -->
          <button type="submit" class="login-button" :disabled="loading">
            <span v-if="loading">Cargando...</span>
            <span v-else>Entrar</span>
          </button>
          
          <!-- Divisor -->
          <div class="divider">
            <span class="divider-text">-O-</span>
          </div>
          
          <!-- Botón Google -->
          <button type="button" class="google-button" @click="loginWithGoogle">
            <svg class="google-icon" width="20" height="20" viewBox="0 0 24 24">
              <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
              <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
              <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"/>
              <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"/>
            </svg>
            Continúa con Google
          </button>
          
          <!-- Registro -->
          <div class="register-section">
            <span class="register-text">¿No tienes cuenta? </span>
            <a href="#" class="register-link">Regístrate</a>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoginForm',
  data() {
    return {
      email: '',
      password: '',
      loading: false
    }
  },
  methods: {
    async handleLogin() {
      this.loading = true
      
      try {
        // Conectar con tu API de Django
        const response = await fetch('http://localhost:8000/api/login/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            email: this.email,
            password: this.password
          })
        })
        
        const data = await response.json()
        
        if (response.ok) {
          // Login exitoso
          console.log('Login exitoso:', data)
          
          // Guardar token en localStorage
          localStorage.setItem('token', data.token)
          localStorage.setItem('user', JSON.stringify(data.user))
          
          // Mostrar mensaje de éxito
          alert(`¡Bienvenido ${data.user.first_name || data.user.username}!`)
          
          // Aquí puedes redirigir cuando tengas Vue Router
          // this.$router.push('/dashboard')
          
        } else {
          // Error en login
          console.error('Error en login:', data)
          alert(data.error || 'Credenciales incorrectas')
        }
      } catch (error) {
        console.error('Error de conexión:', error)
        alert('Error de conexión. Verifica que tu servidor Django esté ejecutándose.')
      } finally {
        this.loading = false
      }
    },
    
    loginWithGoogle() {
      // Implementar login con Google
      console.log('Login con Google')
    }
  }
}
</script>

<style scoped>
/* Importar Poppins */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@500;600&display=swap');

.login-page {
  display: flex;
  height: 100vh;
  width: 100vw;
  font-family: 'Poppins', sans-serif;
  overflow: hidden; /* Elimina el scroll */
}

.left-section {
  flex: 1;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #FF6B35, #F7931E);
  overflow: hidden;
}

/* Línea naranja lateral */
.orange-line {
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 30px; /* Más ancha */
  background: linear-gradient(135deg, #FF6B35, #F7931E);
  z-index: 3;
}

/* Aquí colocas tu imagen del chef */
.chef-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  position: absolute;
  top: 0;
  left: 0;
}

.image-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.15);
}

.right-section {
  flex: 1;
  display: flex;
  flex-direction: column;
  background-color: #ffffff;
  padding: 2rem;
  max-height: 100vh;
  position: relative;
  overflow: hidden; /* Elimina el scroll completamente */
}

.header {
  position: absolute;
  top: 1.5rem; /* Más arriba */
  right: 2rem;
}

.login-container {
  width: 100%;
  max-width: 350px; 
  margin: auto;
  display: flex;
  flex-direction: column;
  justify-content: center;
  height: 100%;
  padding-top: 3rem; /* Menos espacio para mover hacia arriba */
}

.brand {
  font-size: 16px; /* ANAVRIN más pequeño */
  font-weight: 600;
  color: #1a1a1a;
  margin: 0;
  letter-spacing: 2px;
  font-family: 'Poppins', sans-serif;
}

.login-title {
  font-size: 24px; /* Más pequeño */
  font-weight: 600; 
  color: #1a1a1a;
  margin-bottom: 1.5rem; 
  text-align: center; 
  font-family: 'Poppins', sans-serif;
  line-height: 1.1;
}

.login-form {
  display: flex;
  flex-direction: column;
  gap: 0.75rem; 
}

.input-group {
  display: flex;
  flex-direction: column;
}

.input-container {
  position: relative;
  display: flex;
  align-items: center;
}

.input-icon {
  position: absolute;
  left: 1rem;
  z-index: 1;
}

.form-input {
  width: 100%;
  padding: 0.7rem 0.7rem 0.7rem 2.6rem; /* Cuadros más pequeños */
  border: 2px solid #e5e5e5;
  border-radius: 8px;
  font-size: 14px; /* Fuente más pequeña */
  font-weight: 500; 
  font-family: 'Poppins', sans-serif;
  transition: border-color 0.3s ease;
  background-color: #ffffff;
}

.form-input:focus {
  outline: none;
  border-color: #ff6b35;
}

.form-input::placeholder {
  color: #999;
  font-size: 14px; /* Placeholder más pequeño también */
  font-weight: 500;
  font-family: 'Poppins', sans-serif;
}

.forgot-password {
  text-align: left;
  margin: 0.25rem 0 0.75rem 0; 
}

.forgot-link {
  color: #666;
  text-decoration: underline;
  font-size: 13px; /* Más pequeño */
  font-weight: 500;
  font-family: 'Poppins', sans-serif;
}

.forgot-link:hover {
  color: #ff6b35;
}

.login-button {
  width: 100%;
  padding: 0.6rem; /* Botón más pequeño */
  background: linear-gradient(135deg, #ff6b35, #f7931e);
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 14px; /* Fuente más pequeña */
  font-weight: 500;
  font-family: 'Poppins', sans-serif;
  cursor: pointer;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  margin-top: 0.5rem; 
}

.login-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(255, 107, 53, 0.3);
}

.login-button:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
}

.divider {
  display: flex;
  align-items: center;
  margin: 1rem 0; 
}

.divider::before,
.divider::after {
  content: '';
  flex: 1;
  height: 1px;
  background: #e5e5e5;
}

.divider-text {
  margin: 0 1rem;
  color: #999;
  font-size: 12px; 
  font-weight: 500;
  font-family: 'Poppins', sans-serif;
}

.google-button {
  width: 100%;
  padding: 0.6rem; /* Botón más pequeño */
  background-color: #ffffff;
  border: 2px solid #e5e5e5;
  border-radius: 8px;
  font-size: 14px; /* Fuente más pequeña */
  font-weight: 500;
  font-family: 'Poppins', sans-serif;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.75rem;
  transition: border-color 0.3s ease, background-color 0.3s ease;
}

.google-button:hover {
  border-color: #d0d0d0;
  background-color: #f8f8f8;
}

.google-icon {
  width: 20px;
  height: 20px;
}

.register-section {
  text-align: center;
  margin-top: 1.5rem; /* Más pegado hacia arriba */
}

.register-text {
  color: #666;
  font-size: 13px; /* Más pequeño */
  font-weight: 500;
  font-family: 'Poppins', sans-serif;
}

.register-link {
  color: #ff6b35;
  text-decoration: none;
  font-weight: 500;
  font-size: 13px; /* Más pequeño */
  font-family: 'Poppins', sans-serif;
}

.register-link:hover {
  text-decoration: underline;
}

/* Responsive */
@media (max-width: 768px) {
  .login-page {
    flex-direction: column;
  }
  
  .left-section {
    height: 30vh;
    min-height: 200px;
  }
  
  .orange-line {
    width: 20px; 
  }
  
  .right-section {
    flex: 1;
    height: 70vh;
  }
  
  .header {
    top: 1rem;
    right: 1rem;
  }
  
  .login-container {
    padding-top: 3rem;
    height: 70vh;
  }
  
  .login-title {
    font-size: 24px;
  }
  
  .form-input,
  .form-input::placeholder {
    font-size: 14px;
  }
  
  .forgot-link,
  .register-text,
  .register-link {
    font-size: 12px;
  }
}

@media (max-width: 480px) {
  .right-section {
    padding: 1rem;
  }
  
  .login-title {
    font-size: 22px;
  }
  
  .orange-line {
    width: 15px; 
  }
}
</style>