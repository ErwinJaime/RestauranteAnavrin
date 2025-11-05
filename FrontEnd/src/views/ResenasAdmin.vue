<template>
  <div class="resenas-admin-container">
    <!-- Navegación -->
    <nav class="navbar">
      <h1 class="logo">ANAVRIN</h1>
      <div class="nav-links">
        <a href="#">Home</a>
        <a href="#">About</a>
        <a href="#">Review</a>
      </div>
      <button class="btn-admin">Admin</button>
      <button class="btn-cerrar-sesion">Cerrar Sesión</button>
    </nav>

    <!-- Contenido Principal -->
    <div class="main-content">
      <h1>Reseñas Admin</h1>
      <p>Contenido de la página de reseñas</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ResenasAdmin'
}
</script>

<style scoped>
/* General */
.resenas-admin-container {
  width: 100%;
  min-height: 100vh;
  background-color: #ffffff;
}

/* Navegación */
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 50;
  background-color: #ffffff;
  padding: 20px 80px;
  display: flex;
  justify-content: space-between;
  gap: 20px;
  margin-right: -500px;
}

.logo {
  font-size: 20px;
  font-weight: 600;
  color: #1a1a1a;
  letter-spacing: 1px;
  margin-left: 70px;
}

.nav-links {
  display: flex;
  gap: 60px;
  margin-left: 30px;
}

.nav-links a {
  font-size: 14px;
  color: #666;
  text-decoration: none;
  transition: color 0.3s ease;
}

.nav-links a:hover {
  color: #6d9fef;
}

.btn-admin {
  padding: 8px 28px;
  font-size: 14px;
  color: #000;
  background-color: #ff6b35;
  border: none;
  border-radius: 50px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 580;
  margin-right: -230px;
}

.btn-admin:hover {
  background-color: #3b82f6;
}

.btn-cerrar-sesion {
  padding: 8px 22px;
  font-size: 14px;
  color: #070707;
  border: 2px solid #ddd;
  background-color: transparent;
  border-radius: 50px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 600;
  margin-right: 440px;
}

.btn-cerrar-sesion:hover {
  background-color: #6d9fef;
  color: white;
}

/* Contenido Principal */
.main-content {
  padding-top: 120px;
  max-width: 1200px;
  margin: 0 auto;
  padding-left: 20px;
  padding-right: 20px;
}
</style>