<template>
  <div class="protected-component">
    <h2>Componente Protegido</h2>
    <p>Este componente solo es accesible para usuarios autenticados.</p>
    
    <div class="user-info">
      <h3>Información del Usuario:</h3>
      <p><strong>Nombre:</strong> {{ user.nombre }}</p>
      <p><strong>Email:</strong> {{ user.correo }}</p>
      <p><strong>ID:</strong> {{ user.id }}</p>
    </div>
    
    <div class="actions">
      <button @click="makeAuthenticatedRequest" :disabled="loading" class="action-button">
        {{ loading ? 'Cargando...' : 'Hacer Petición Autenticada' }}
      </button>
      
      <button @click="logout" class="logout-button">
        Cerrar Sesión
      </button>
    </div>
    
    <div v-if="response" class="response">
      <h4>Respuesta del servidor:</h4>
      <pre>{{ JSON.stringify(response, null, 2) }}</pre>
    </div>
  </div>
</template>

<script>
import authService from '@/services/probar'

export default {
  name: 'ProtectedComponent',
  data() {
    return {
      user: null,
      loading: false,
      response: null
    }
  },
  mounted() {
    // Verificar autenticación
    if (!authService.isAuthenticated()) {
      this.$router.push('/login')
      return
    }
    
    this.user = authService.getUser()
  },
  methods: {
    async makeAuthenticatedRequest() {
      this.loading = true
      this.response = null
      
      try {
        // Ejemplo de petición autenticada
        const response = await authService.authenticatedRequest(
          'http://localhost:8000/api/usuarios/profile/',
          {
            method: 'GET'
          }
        )
        
        const data = await response.json()
        this.response = data
        
      } catch (error) {
        console.error('Error en petición autenticada:', error)
        this.response = { error: error.message }
      } finally {
        this.loading = false
      }
    },
    
    logout() {
      authService.logout()
      this.$router.push('/login')
    }
  }
}
</script>

<style scoped>
.protected-component {
  max-width: 600px;
  margin: 2rem auto;
  padding: 2rem;
  background: white;
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
  font-family: 'Poppins', sans-serif;
}

.protected-component h2 {
  color: #333;
  margin-bottom: 1rem;
  font-weight: 600;
}

.protected-component p {
  color: #666;
  margin-bottom: 1.5rem;
  line-height: 1.6;
}

.user-info {
  background: #f8f9fa;
  padding: 1.5rem;
  border-radius: 8px;
  margin-bottom: 2rem;
}

.user-info h3 {
  color: #333;
  margin-bottom: 1rem;
  font-weight: 600;
}

.user-info p {
  margin-bottom: 0.5rem;
  color: #555;
}

.actions {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
  flex-wrap: wrap;
}

.action-button {
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

.action-button:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(255, 107, 53, 0.3);
}

.action-button:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
}

.logout-button {
  background: #dc3545;
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
  box-shadow: 0 4px 12px rgba(220, 53, 69, 0.3);
}

.response {
  background: #f8f9fa;
  padding: 1.5rem;
  border-radius: 8px;
  border-left: 4px solid #ff6b35;
}

.response h4 {
  color: #333;
  margin-bottom: 1rem;
  font-weight: 600;
}

.response pre {
  background: #fff;
  padding: 1rem;
  border-radius: 6px;
  overflow-x: auto;
  font-size: 0.9rem;
  color: #555;
  border: 1px solid #e9ecef;
}

@media (max-width: 768px) {
  .protected-component {
    margin: 1rem;
    padding: 1.5rem;
  }
  
  .actions {
    flex-direction: column;
  }
  
  .action-button,
  .logout-button {
    width: 100%;
  }
}
</style>
