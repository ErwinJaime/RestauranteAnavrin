<template>
  <div v-if="isOpen" class="confirmation-overlay" @click.self="$emit('cerrar')">
    <div class="confirmation-modal">
      <h3 class="confirmation-title">{{ titulo }}</h3>
      <p class="confirmation-text">{{ mensaje }}</p>
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
    titulo: { type: String, default: '¿Estás seguro?' },
    mensaje: { type: String, default: 'Esta acción no se puede deshacer.' },
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
}

.confirmation-modal {
  background-color: white;
  border-radius: 16px;
  padding: 25px;
  width: 90%;
  max-width: 350px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
}

.confirmation-title {
  font-size: 18px;
  font-weight: 700;
  color: #28233b;
  margin-bottom: 10px;
  text-align: center;
  font-family: 'Open Sans', sans-serif;
}

.confirmation-text {
  font-size: 13px;
  color: #666;
  text-align: center;
  margin-bottom: 20px;
  line-height: 1.5;
}

.confirmation-buttons {
  display: flex;
  gap: 10px;
  justify-content: center;
}

.btn-eliminar-confirm {
  padding: 8px 24px;
  font-size: 12px;
  color: white;
  background-color: #e74c3c;
  border: none;
  border-radius: 50px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 600;
  font-family: 'Montserrat', sans-serif;
}

.btn-eliminar-confirm:hover:not(:disabled) {
  background-color: #c0392b;
  transform: translateY(-2px);
}

.btn-eliminar-confirm:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.btn-cancelar-confirm {
  padding: 8px 24px;
  font-size: 12px;
  color: #666;
  background-color: #e3e1e1;
  border: none;
  border-radius: 50px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 600;
  font-family: 'Montserrat', sans-serif;
}

.btn-cancelar-confirm:hover:not(:disabled) {
  background-color: #d0d0d0;
  transform: translateY(-2px);
}

.btn-cancelar-confirm:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}
</style>