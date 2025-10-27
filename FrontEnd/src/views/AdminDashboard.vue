<template>
  <div class="admin-dashboard">
    <div class="admin-header">
      <h1>Panel de Administración</h1>
      <button @click="logout" class="logout-button">Cerrar Sesión</button>
    </div>
    
    <div class="admin-content">
      <div class="welcome-card">
        <h2>Bienvenido, Administrador</h2>
        <p>Desde aquí podrás gestionar usuarios, productos, pedidos y reseñas.</p>
      </div>
      
      <div class="admin-stats">
        <div class="stat-card">
          <h3>Usuarios</h3>
          <p class="stat-number">0</p>
        </div>
        <div class="stat-card">
          <h3>Productos</h3>
          <p class="stat-number">0</p>
        </div>
        <div class="stat-card">
          <h3>Pedidos</h3>
          <p class="stat-number">0</p>
        </div>
        <div class="stat-card">
          <h3>Reseñas</h3>
          <p class="stat-number">0</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AdminDashboard',
  methods: {
    logout() {
      localStorage.removeItem('access_token')
      localStorage.removeItem('refresh_token')
      localStorage.removeItem('user')
      this.$router.push('/')
    }
  }
}
</script>

<style scoped>
.admin-dashboard {
  min-height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 2rem;
  font-family: 'Poppins', sans-serif;
}

.admin-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
  background: white;
  padding: 1.5rem 2rem;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.admin-header h1 {
  font-size: 2rem;
  color: #333;
  margin: 0;
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
  cursor: pointer;
  transition: transform 0.2s ease;
}

.logout-button:hover {
  transform: translateY(-2px);
}

.admin-content {
  max-width: 1200px;
  margin: 0 auto;
}

.welcome-card {
  background: white;
  padding: 2rem;
  border-radius: 12px;
  margin-bottom: 2rem;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.welcome-card h2 {
  color: #333;
  margin-bottom: 1rem;
  font-weight: 600;
}

.welcome-card p {
  color: #666;
  font-size: 1.1rem;
}

.admin-stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
}

.stat-card {
  background: white;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.stat-card h3 {
  color: #666;
  font-size: 1rem;
  margin-bottom: 1rem;
  font-weight: 500;
}

.stat-number {
  color: #667eea;
  font-size: 3rem;
  font-weight: 600;
  margin: 0;
}
</style>