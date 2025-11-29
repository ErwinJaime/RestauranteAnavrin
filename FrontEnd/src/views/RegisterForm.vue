<template>
  <div class="register-page">
    <!-- Imagen de fondo lado izquierdo -->
    <div class="left-section">
      <div class="orange-line"></div>
      <img src="@/assets/ImagenCrear.jpg" alt="Chef" class="chef-image">
      <div class="image-overlay"></div>
    </div>
    
    <!-- Formulario lado derecho -->
    <div class="right-section">
      <div class="header">
        <h1 class="brand">ANAVRIN</h1>
      </div>
      
      <div class="register-container">
        <!-- PASO 1: Formulario de Registro -->
        <div v-if="!mostrarVerificacion" class="form-step">
          <h2 class="register-title">Crear Cuenta</h2>
          
          <form @submit.prevent="handleRegister" class="register-form">
            <!-- Campo Nombre -->
            <div class="input-group">
              <div class="input-container">
                <svg class="input-icon" width="20" height="20" viewBox="0 0 24 24" fill="none">
                  <path d="M20 21V19C20 17.9391 19.5786 16.9217 18.8284 16.1716C18.0783 15.4214 17.0609 15 16 15H8C6.93913 15 5.92172 15.4214 5.17157 16.1716C4.42143 16.9217 4 17.9391 4 19V21M16 7C16 9.20914 14.2091 11 12 11C9.79086 11 8 9.20914 8 7C8 4.79086 9.79086 3 12 3C14.2091 3 16 4.79086 16 7Z" stroke="#666" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
                <input 
                  v-model="nombre"
                  type="text" 
                  placeholder="Nombre completo"
                  required
                  class="form-input"
                >
              </div>
            </div>

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

            <!-- Campo Confirmar Contraseña -->
            <div class="input-group">
              <div class="input-container">
                <svg class="input-icon" width="20" height="20" viewBox="0 0 24 24" fill="none">
                  <path d="M16 12V8C16 5.79086 14.2091 4 12 4C9.79086 4 8 5.79086 8 8V12M12 15C12.5523 15 13 14.5523 13 14C13 13.4477 12.5523 13 12 13C11.4477 13 11 13.4477 11 14C11 14.5523 11.4477 15 12 15ZM7 12H17C18.1046 12 19 12.8954 19 14V18C19 19.1046 18.1046 20 17 20H7C5.89543 20 5 19.1046 5 18V14C5 12.8954 5.89543 12 7 12Z" stroke="#666" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
                <input 
                  v-model="confirmPassword"
                  type="password" 
                  placeholder="Confirmar contraseña"
                  required
                  class="form-input"
                >
              </div>
            </div>
            
            <!-- Mensaje de error -->
            <div v-if="error" class="error-message">
              {{ error }}
            </div>
            
            <!-- Botón Registrarse -->
            <button type="submit" class="register-button" :disabled="loading">
              <span v-if="loading">Creando cuenta...</span>
              <span v-else>Crear Cuenta</span>
            </button>
            
            <!-- Login -->
            <div class="login-section">
              <span class="login-text">¿Ya tienes cuenta? </span>
              <a href="#" class="login-link" @click.prevent="$router.push('/login')">Inicia sesión</a>
            </div>
          </form>
        </div>

        <!-- PASO 2: Verificación de Código -->
        <div v-else class="form-step verification-step">
          <div class="verification-icon">📧</div>
          <h2 class="verification-title">Verifica tu correo</h2>
          <p class="verification-text">
            Hemos enviado un código de 6 dígitos a<br>
            <strong>{{ email }}</strong>
          </p>

          <form @submit.prevent="handleVerificarCodigo" class="verification-form">
            <!-- Input del código -->
            <div class="code-input-container">
              <input 
                v-model="codigoVerificacion"
                type="text" 
                maxlength="6"
                placeholder="000000"
                required
                class="code-input"
                @input="validarSoloNumeros"
              >
            </div>

            <!-- Mensaje de error -->
            <div v-if="error" class="error-message">
              {{ error }}
            </div>

            <!-- Mensaje de éxito -->
            <div v-if="success" class="success-message">
              {{ success }}
            </div>

            <!-- Botón Verificar -->
            <button type="submit" class="verify-button" :disabled="loading">
              <span v-if="loading">Verificando...</span>
              <span v-else>Verificar Código</span>
            </button>

            <!-- Reenviar código -->
            <div class="resend-section">
              <button 
                type="button" 
                class="resend-button" 
                @click="handleReenviarCodigo"
                :disabled="loading || tiempoEspera > 0"
              >
                <span v-if="tiempoEspera > 0">
                  Reenviar en {{ tiempoEspera }}s
                </span>
                <span v-else>
                  Reenviar código
                </span>
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { registro, verificarCodigo, reenviarCodigo } from '@/services/auth'

export default {
  name: 'RegisterForm',
  data() {
    return {
      // Paso 1: Registro
      nombre: '',
      email: '',
      password: '',
      confirmPassword: '',
      
      // Paso 2: Verificación
      mostrarVerificacion: false,
      codigoVerificacion: '',
      usuarioId: null,
      tiempoEspera: 0,
      intervalId: null,
      
      // Estados
      loading: false,
      error: '',
      success: ''
    }
  },
  beforeUnmount() {
    if (this.intervalId) {
      clearInterval(this.intervalId)
    }
  },
  methods: {
    async handleRegister() {
      // Limpiar mensajes
      this.error = ''
      this.success = ''
      
      // Validaciones básicas
      if (!this.nombre || !this.email || !this.password || !this.confirmPassword) {
        this.error = 'Por favor, completa todos los campos'
        return
      }

      if (this.password !== this.confirmPassword) {
        this.error = 'Las contraseñas no coinciden'
        return
      }

      if (this.password.length < 6) {
        this.error = 'La contraseña debe tener al menos 6 caracteres'
        return
      }

      this.loading = true

      try {
        console.log('📝 Registrando usuario...', { nombre: this.nombre, email: this.email })
        
        const response = await registro(
          this.nombre, 
          this.email, 
          this.password,
          this.confirmPassword 
        )
        
        console.log('✅ Respuesta del servidor:', response.data)
        
        // Guardar ID del usuario
        this.usuarioId = response.data.usuario_id
        
        // Cambiar a pantalla de verificación
        this.mostrarVerificacion = true
        
        // Iniciar temporizador
        this.iniciarTemporizador()
        
        console.log('✅ Pantalla de verificación mostrada')
        
      } catch (error) {
        console.error('❌ Error al registrar:', error)
        console.error('❌ Respuesta completa:', error.response)
        
        // Manejar errores específicos
        if (error.response?.data?.password) {
          this.error = error.response.data.password[0]
        } else if (error.response?.data?.correo) {
          this.error = 'Este correo ya está registrado'
        } else if (error.response?.data?.error) {
          this.error = error.response.data.error
        } else {
          this.error = 'Error al registrar usuario. Intenta nuevamente.'
        }
      } finally {
        this.loading = false
      }
    },

    async handleVerificarCodigo() {
      // Validar código
      if (!this.codigoVerificacion || this.codigoVerificacion.length !== 6) {
        this.error = 'El código debe tener 6 dígitos'
        return
      }

      this.loading = true
      this.error = ''
      this.success = ''

      try {
        console.log('🔍 Verificando código:', this.codigoVerificacion)
        
        const response = await verificarCodigo(this.usuarioId, this.codigoVerificacion)
        
        console.log('✅ Código verificado:', response.data)
        
        // Guardar tokens
        localStorage.setItem('access_token', response.data.access)
        localStorage.setItem('refresh_token', response.data.refresh)
        localStorage.setItem('user', JSON.stringify(response.data.usuario))
        
        // Mostrar mensaje de éxito
        this.success = '¡Cuenta verificada! Redirigiendo...'
        
        // Redirigir después de 1.5 segundos
        setTimeout(() => {
          this.$router.push('/dashboard')
        }, 1500)
        
      } catch (error) {
        console.error('❌ Error al verificar código:', error)
        console.error('❌ Respuesta completa:', error.response)
        
        // Mostrar error pero permitir reintentar
        this.error = error.response?.data?.error || 'Código incorrecto o expirado. Intenta de nuevo.'
        
        // ✅ IMPORTANTE: Limpiar el código para permitir reintentar
        this.codigoVerificacion = ''
        
        // ✅ NO redirigir, mantener en la misma pantalla
        
      } finally {
        this.loading = false
      }
    },

    async handleReenviarCodigo() {
      // Verificar si puede reenviar
      if (this.tiempoEspera > 0) {
        this.error = `Espera ${this.tiempoEspera} segundos antes de reenviar`
        return
      }

      this.loading = true
      this.error = ''
      this.success = ''

      try {
        console.log('📧 Reenviando código al usuario:', this.usuarioId)
        
        await reenviarCodigo(this.usuarioId)
        
        console.log('✅ Código reenviado')
        
        this.success = 'Código reenviado. Revisa tu correo.'
        this.codigoVerificacion = ''
        
        // Reiniciar temporizador
        this.iniciarTemporizador()
        
        // Limpiar mensaje de éxito después de 3 segundos
        setTimeout(() => {
          this.success = ''
        }, 3000)
        
      } catch (error) {
        console.error('❌ Error al reenviar código:', error)
        console.error('❌ Respuesta completa:', error.response)
        
        this.error = error.response?.data?.error || 'Error al reenviar el código'
        
      } finally {
        this.loading = false
      }
    },

    iniciarTemporizador() {
      this.tiempoEspera = 60
      
      // Limpiar temporizador anterior si existe
      if (this.intervalId) {
        clearInterval(this.intervalId)
      }
      
      // Iniciar nuevo temporizador
      this.intervalId = setInterval(() => {
        this.tiempoEspera--
        if (this.tiempoEspera <= 0) {
          clearInterval(this.intervalId)
        }
      }, 1000)
    },

    validarSoloNumeros(event) {
      // Filtrar solo números
      this.codigoVerificacion = event.target.value.replace(/[^0-9]/g, '')
    }
  }
}
</script>

<style scoped>
/* revisar toda la parte del frontend por q no funciono*/
/* Importar Poppins */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@500;600&display=swap');

.register-page {
  display: flex;
  height: 100vh;
  width: 100vw;
  font-family: 'Poppins', sans-serif;
  overflow: hidden;
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

.orange-line {
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 30px;
  background: linear-gradient(135deg, #FF6B35, #F7931E);
  z-index: 3;
}

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
  overflow: hidden;
}

.header {
  position: absolute;
  top: 2rem;
  right: 2rem;
}

.register-container {
  width: 100%;
  max-width: 400px;
  margin: auto;
  display: flex;
  flex-direction: column;
  justify-content: center;
  height: 100%;
  padding-top: 4rem;
}

.brand {
  font-size: 20px;
  font-weight: 600;
  color: #1a1a1a;
  margin: 0;
  letter-spacing: 2px;
  font-family: 'Poppins', sans-serif;
}

.register-title {
  font-size: 28px;
  font-weight: 600;
  color: #1a1a1a;
  margin-bottom: 2rem;
  text-align: center;
  font-family: 'Poppins', sans-serif;
  line-height: 1.1;
}

.register-form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
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
  padding: 1rem 1rem 1rem 3rem;
  border: 2px solid #e5e5e5;
  border-radius: 8px;
  font-size: 12px;
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
  font-size: 16px;
  font-weight: 500;
  font-family: 'Poppins', sans-serif;
}

.error-message {
  background-color: #fee;
  color: #c33;
  padding: 0.75rem;
  border-radius: 6px;
  font-size: 16px;
  font-weight: 500;
  font-family: 'Poppins', sans-serif;
  text-align: center;
  margin: 0.5rem 0;
  border: 1px solid #fcc;
}

.success-message {
  background-color: #efe;
  color: #363;
  padding: 0.75rem;
  border-radius: 6px;
  font-size: 16px;
  font-weight: 500;
  font-family: 'Poppins', sans-serif;
  text-align: center;
  margin: 0.5rem 0;
  border: 1px solid #cfc;
}

.register-button {
  width: 100%;
  padding: 1rem;
  background: linear-gradient(150deg, #ff6b35, #f7931e);
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 16px;
  font-weight: 500;
  font-family: 'Poppins', sans-serif;
  cursor: pointer;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  margin-top: 1rem;
}

.register-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(255, 107, 53, 0.3);
}

.register-button:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
}

.login-section {
  text-align: center;
  margin-top: 2rem;
}

.login-text {
  color: #666;
  font-size: 16px;
  font-weight: 500;
  font-family: 'Poppins', sans-serif;
}

.login-link {
  color: #ff6b35;
  text-decoration: none;
  font-weight: 500;
  font-size: 16px;
  font-family: 'Poppins', sans-serif;
  cursor: pointer;
}
/* Nuevos estilos para verificación */
.verification-step {
  text-align: center;
  max-width: 400px;
}

.verification-icon {
  font-size: 64px;
  margin-bottom: 20px;
}

.verification-title {
  font-size: 28px;
  font-weight: 600;
  color: #1a1a1a;
  margin-bottom: 16px;
  font-family: 'Poppins', sans-serif;
}

.verification-text {
  font-size: 14px;
  color: #666;
  margin-bottom: 32px;
  line-height: 1.6;
  font-family: 'Poppins', sans-serif;
}

.verification-text strong {
  color: #ff6b35;
  font-weight: 600;
}

.verification-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.code-input-container {
  display: flex;
  justify-content: center;
}

.code-input {
  width: 100%;
  max-width: 280px;
  padding: 20px;
  font-size: 32px;
  font-weight: 600;
  text-align: center;
  letter-spacing: 12px;
  border: 2px solid #e0e0e0;
  border-radius: 12px;
  font-family: 'Poppins', sans-serif;
  transition: border-color 0.3s ease;
}

.code-input:focus {
  outline: none;
  border-color: #ff6b35;
}

.code-input::placeholder {
  color: #ddd;
  letter-spacing: 8px;
}

.verify-button {
  width: 100%;
  padding: 16px;
  background: linear-gradient(90deg, #ff6b35, #ff8c5a);
  color: white;
  border: none;
  border-radius: 10px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  font-family: 'Poppins', sans-serif;
}

.verify-button:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(255, 107, 53, 0.4);
}

.verify-button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
  transform: none;
}

.resend-section {
  margin-top: 16px;
}

.resend-button {
  background: none;
  border: none;
  color: #ff6b35;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  font-family: 'Poppins', sans-serif;
  text-decoration: underline;
  transition: color 0.3s ease;
}

.resend-button:hover:not(:disabled) {
  color: #e55a2b;
}

.resend-button:disabled {
  color: #999;
  cursor: not-allowed;
  text-decoration: none;
}
.login-link:hover {
  text-decoration: underline;
}

/* Responsive */
@media (max-width: 768px) {
  .register-page {
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
  
  .register-container {
    padding-top: 3rem;
    height: 70vh;
  }
  
  .register-title {
    font-size: 32px;
  }
  
  .form-input,
  .form-input::placeholder,
  .login-text,
  .login-link {
    font-size: 16px;
  }
}

@media (max-width: 480px) {
  .right-section {
    padding: 1rem;
  }
  
  .register-title {
    font-size: 28px;
  }
  
  .orange-line {
    width: 15px;
  }
}
</style>
