<template>
  <div v-if="isOpen" class="modal-overlay" @click.self="$emit('cerrar')">
    <div class="modal-content">
      <!-- Título -->
      <h2 class="modal-title">Agregar Nuevo Producto</h2>
      
      <!-- Upload de imagen -->
      <div class="upload-area" @click="$refs.fileInput.click()">
        <input
          ref="fileInput"
          type="file"
          accept="image/*"
          @change="handleImageUpload"
          style="display: none"
        />
        <img v-if="imagenPreview" :src="imagenPreview" alt="Preview" class="preview-image" />
        <div v-else class="upload-placeholder">
          <svg width="40" height="40" viewBox="0 0 24 24" fill="none">
            <path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z" stroke="#999" stroke-width="2"/>
            <circle cx="12" cy="13" r="4" stroke="#999" stroke-width="2"/>
          </svg>
          <p>Subir imagen del producto</p>
        </div>
      </div>
      
      <!-- Nombre del Producto -->
      <div class="form-group">
        <label>Nombre del Producto *</label>
        <input 
          type="text" 
          v-model="nombreProducto" 
          required
        />
      </div>
      
      <!-- Ingredientes -->
      <div class="form-group">
        <label>Ingredientes *</label>
        <textarea 
          v-model="ingredientes" 
          rows="3"
          required
        ></textarea>
      </div>

      <!-- Categoría -->
      <div class="form-group">
        <label>Categoría *</label>
        <select v-model="categoria" class="select-categoria" required>
          <option value="">Selecciona una categoría</option>
          <option value="platillo">Platillo</option>
          <option value="postre">Postre</option>
          <option value="bebida">Bebida</option>
        </select>
      </div>
      
      <!-- Precio -->
      <div class="form-group">
        <label>Precio ($) *</label>
        <input 
          type="number" 
          v-model="precio" 
          step="0.01"
          min="0"
          placeholder="0.00"
          required
        />
      </div>
      
      <!-- Checkbox -->
      <div class="checkbox-group">
        <input type="checkbox" id="disponible" v-model="disponible" />
        <label for="disponible">Disponible en el Menú</label>
      </div>

      <!-- Mensaje de error -->
      <div v-if="errorMsg" class="error-message">
        {{ errorMsg }}
      </div>
      
      <!-- Botones -->
      <div class="modal-buttons">
        <button class="btn-guardar" @click="handleGuardar" :disabled="guardando">
          {{ guardando ? 'Guardando...' : 'Guardar' }}
        </button>
        <button class="btn-cancelar" @click="handleCancelar" :disabled="guardando">
          Cancelar
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, watch } from 'vue'

export default {
  name: 'AgregarProductoModal',
  props: {
    isOpen: {
      type: Boolean,
      default: false
    }
  },
  emits: ['cerrar', 'guardar'],
  setup(props, { emit }) {
    const nombreProducto = ref('')
    const ingredientes = ref('')
    const categoria = ref('')
    const precio = ref('')
    const disponible = ref(true)
    const imagenFile = ref(null)
    const imagenPreview = ref(null)
    const errorMsg = ref('')
    const guardando = ref(false)

    // Limpiar formulario cuando se cierra el modal
    watch(() => props.isOpen, (newVal) => {
      if (!newVal) {
        limpiarFormulario()
      }
    })

    const handleImageUpload = (event) => {
      const file = event.target.files[0]
      if (file) {
        // Validar tipo de archivo
        if (!file.type.startsWith('image/')) {
          errorMsg.value = 'Por favor selecciona un archivo de imagen válido'
          return
        }

        // Validar tamaño (máx 5MB)
        if (file.size > 5 * 1024 * 1024) {
          errorMsg.value = 'La imagen no debe superar 5MB'
          return
        }

        imagenFile.value = file
        
        const reader = new FileReader()
        reader.onload = (e) => {
          imagenPreview.value = e.target.result
        }
        reader.readAsDataURL(file)
        errorMsg.value = ''
      }
    }

    const validarFormulario = () => {
      if (!nombreProducto.value.trim()) {
        errorMsg.value = 'El nombre del producto es obligatorio'
        return false
      }

      if (!ingredientes.value.trim()) {
        errorMsg.value = 'Los ingredientes son obligatorios'
        return false
      }

      if (!categoria.value) {
        errorMsg.value = 'Debes seleccionar una categoría'
        return false
      }

      if (!precio.value || parseFloat(precio.value) <= 0) {
        errorMsg.value = 'El precio debe ser mayor a 0'
        return false
      }

      return true
    }

    const handleGuardar = async () => {
      errorMsg.value = ''

      if (!validarFormulario()) {
        return
      }

      guardando.value = true

      try {
        const productoData = {
          nombreProducto: nombreProducto.value.trim(),
          ingredientes: ingredientes.value.trim(),
          categoria: categoria.value,
          precio: parseFloat(precio.value),
          disponible: disponible.value,
          imagen: imagenFile.value // Pasar el File directamente
        }

        emit('guardar', productoData)
      } catch (error) {
        console.error('Error al preparar datos:', error)
        errorMsg.value = 'Error al preparar los datos del producto'
        guardando.value = false
      }
    }

    const handleCancelar = () => {
      limpiarFormulario()
      emit('cerrar')
    }

    const limpiarFormulario = () => {
      nombreProducto.value = ''
      ingredientes.value = ''
      categoria.value = ''
      precio.value = ''
      disponible.value = true
      imagenFile.value = null
      imagenPreview.value = null
      errorMsg.value = ''
      guardando.value = false
    }

    return {
      nombreProducto,
      ingredientes,
      categoria,
      precio,
      disponible,
      imagenPreview,
      errorMsg,
      guardando,
      handleImageUpload,
      handleGuardar,
      handleCancelar
    }
  }
}
</script>

<style scoped>
/* Modal overlay */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #e8e8e88e;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  font-family: 'Montserrat', sans-serif;
}

.modal-content {
  background-color: #fff8f8;
  border-radius: 20px;
  padding: 20px 25px;
  width: 90%;
  max-width: 450px;
  position: relative;
  box-shadow: 0 10px 40px #00000014;
}

.modal-title {
  font-size: 20px;
  font-weight: 700;
  color: #28233b;
  margin-bottom: 12px; 
  text-align: center;
  font-family: 'Open Sans', sans-serif;
}

.select-categoria {
  width: 100%;
  padding: 8px 12px;
  border: 2px solid #e5e5e5;
  border-radius: 10px;
  font-size: 12px;
  font-family: 'Montserrat', sans-serif;
  transition: border-color 0.3s ease;
  box-sizing: border-box;
  background-color: white;
  cursor: pointer;
}

.select-categoria:focus {
  outline: none;
  border-color: #7cb342;
}

/* Upload área */
.upload-area {
  border: 2px dashed #ddd;
  border-radius: 12px;
  padding: 12px;
  text-align: center;
  margin-bottom: 12px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.upload-area:hover {
  border-color: #7cb342;
}

.upload-placeholder svg {
  width: 32px;
  height: 32px;
  margin-bottom: 5px;
}

.upload-placeholder p {
  color: #999;
  font-size: 11px;
  margin: 5px 0 0 0;
}

.preview-image {
  max-width: 100%;
  max-height: 90px;
  border-radius: 8px;
}

/* Form groups */
.form-group {
  margin-bottom: 10px;
}

.form-group label {
  display: block;
  font-size: 12px;
  color: #666;
  margin-bottom: 4px;
  font-weight: 500;
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 7px 10px;
  border: 2px solid #e5e5e5;
  border-radius: 10px;
  font-size: 12px;
  font-family: 'Montserrat', sans-serif;
  transition: border-color 0.3s ease;
  box-sizing: border-box;
}

.form-group input:focus,
.form-group textarea:focus {
  outline: none;
  border-color: #7cb342;
}

.form-group textarea {
  resize: vertical;
  min-height: 50px;
}

/* Checkbox */
.checkbox-group {
  margin-bottom: 12px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.checkbox-group input[type="checkbox"] {
  width: 15px;
  height: 15px;
  cursor: pointer;
}

.checkbox-group label {
  font-size: 12px;
  color: #666;
  cursor: pointer;
  user-select: none;
}

/* Mensaje de error */
.error-message {
  background-color: #fee;
  color: #c33;
  padding: 5px 9px;
  border-radius: 8px;
  font-size: 11px;
  margin-bottom: 10px;
  text-align: center;
}

/* Botones */
.modal-buttons {
  display: flex;
  gap: 10px;
  justify-content: center;
  margin-top: 8px;
}

.btn-guardar,
.btn-cancelar {
  padding: 8px 28px;
  font-size: 11px;
  font-weight: 600;
  border: none;
  border-radius: 50px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-family: 'Montserrat', sans-serif;
}

.btn-guardar {
  color: white;
  background-color: #7cb342;
}

.btn-guardar:hover:not(:disabled) {
  background-color: #6d9fef;
  transform: translateY(-2px);
}

.btn-guardar:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.btn-cancelar {
  color: #666;
  background-color: #e3e1e1;
}

.btn-cancelar:hover:not(:disabled) {
  background-color: #6d9fef;
  color: white;
}

.btn-cancelar:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}
</style>