<template>
  <div v-if="isOpen" class="confirmation-overlay" @click.self="$emit('cerrar')">
    <div class="confirmation-modal">
      <!-- Icono de alerta -->
      <div class="alert-icon">
        <img src="@/assets/alerta.png" alt="Alerta" width="55" height="55" />
      </div>

      <!-- Título -->
      <h3 class="confirmation-title">{{ titulo }}</h3>
      
      <!-- Mensaje -->
      <p class="confirmation-text">{{ mensaje }}</p>
      
      <!-- Botones -->
      <div class="confirmation-buttons">
        <button 
          class="btn-eliminar-confirm" 
          @click="$emit('confirmar')"
          :disabled="cargando"
        >
          {{ cargando ? 'Procesando...' : textoConfirmar }}
        </button>
        <button 
          class="btn-cancelar-confirm" 
          @click="$emit('cerrar')"
          :disabled="cargando"
        >
          Cancelar
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ModalConfirmacion',
  props: {
    isOpen: { type: Boolean, default: false },
    titulo: { type: String, default: '¿Estás seguro de que quieres eliminar el producto?'},
    mensaje: { type: String, default: 'Esta acción es permanente. Una vez eliminado, el producto no estará disponible, ni aparecerá en el menú.'},
    textoConfirmar: { type: String, default: 'Confirmar' },
    cargando: { type: Boolean, default: false }
  },
  emits: ['cerrar', 'confirmar']
}
</script>

<style scoped>
.confirmation-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1100;
  font-family: 'Montserrat', sans-serif;
}

.confirmation-modal {
  background-color: white;
  border-radius: 16px;
  padding: 35px 30px 25px;
  width: 90%;
  max-width: 380px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
  text-align: center;
}

/* Icono de alerta */
.alert-icon {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.alert-icon img {
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0%, 100% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.05);
  }
}

/* Título */
.confirmation-title {
  font-size: 25px;
  font-weight: 700;
  color: #2c3e50;
  margin-bottom: 12px;
  text-align: left;
  font-family: 'Open Sans', sans-serif;
  line-height: 1.3;
}


/* Texto del mensaje */
.confirmation-text {
  font-size: 14px;
  color: #555;
  text-align: center;
  margin-bottom: 25px;
  line-height: 1.6;
  font-weight: 400;
}

/* Botones */
.confirmation-buttons {
  display: flex;
  gap: 12px;
  justify-content: center;
}

.btn-eliminar-confirm {
  padding: 11px 30px;
  font-size: 14px;
  color: white;
  background-color: #e74c3c;
  border: none;
  border-radius: 50px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 600;
  font-family: 'Montserrat', sans-serif;
  box-shadow: 0 2px 8px rgba(231, 76, 60, 0.3);
}

.btn-eliminar-confirm:hover:not(:disabled) {
  background-color: #c0392b;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(231, 76, 60, 0.4);
}

.btn-eliminar-confirm:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.btn-cancelar-confirm {
  padding: 11px 30px;
  font-size: 14px;
  color: #555;
  background-color: #e0e0e0;
  border: none;
  border-radius: 50px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 600;
  font-family: 'Montserrat', sans-serif;
}

.btn-cancelar-confirm:hover:not(:disabled) {
  background-color: #bdbdbd;
  transform: translateY(-2px);
}

.btn-cancelar-confirm:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

/* Responsive */
@media (max-width: 480px) {
  .confirmation-modal {
    max-width: 320px;
    padding: 30px 25px 20px;
  }

  .alert-icon svg {
    width: 45px;
    height: 45px;
  }

  .confirmation-title {
    font-size: 18px;
  }

  .confirmation-text {
    font-size: 13px;
  }

  .confirmation-buttons {
    flex-direction: column;
    gap: 10px;
  }

  .btn-eliminar-confirm,
  .btn-cancelar-confirm {
    width: 100%;
    padding: 10px 24px;
    font-size: 13px;
  }
}
</style>