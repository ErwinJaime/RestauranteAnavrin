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
          <option value="">Platillo</option>
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
        <label class="custom-checkbox">
          <input type="checkbox" v-model="disponible" />
          <span class="checkmark"></span>
          <span class="checkbox-label">Disponible en el Menú</span>
        </label>
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
          nombre: nombreProducto.value.trim(), // ✅ CAMBIO: era "nombreProducto", ahora es "nombre"
          ingredientes: ingredientes.value.trim(),
          categoria: categoria.value,
          precio: parseFloat(precio.value),
          disponible: disponible.value,
          imagen: imagenFile.value
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
  padding: 14px 18px;
  width: 90%;
  max-width: 400px;
  position: relative;
  box-shadow: 0 10px 40px #00000014;
}

.modal-title {
  font-size: 18px;
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
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23666' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
  background-repeat: no-repeat;
  background-position: right 10px center;
  background-size: 16px;
  padding-right: 35px;
}

.select-categoria:focus {
  outline: none;
  border-color: #7cb342;
}

/* Upload área */
.upload-area {
  border: none;
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

.upload-placeholder {
  border: 2px dashed #ddd;
  border-radius: 12px;
  padding: 12px;
  text-align: center;
  margin-bottom: 12px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.upload-placeholder:hover {
  border-color: #bdbdbd;
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
  width: 100px;           
  height: 100px;
  border-radius: 50%;     
  object-fit: cover;     
  border: 3px solid #ddd;
  display: block;
  margin: 0 auto 10px auto; 
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.15);
}

/* Form groups */
.form-group {
  margin-bottom: 10px;
}

.form-group label {
  display: block;
  font-size: 13px;
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
}

.custom-checkbox {
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  user-select: none;
  position: relative;
}

/* Ocultar checkbox original */
.custom-checkbox input[type="checkbox"] {
  position: absolute;
  opacity: 0;
  cursor: pointer;
  height: 0;
  width: 0;
}

/* Crear checkbox personalizado */
.checkmark {
  position: relative;
  height: 18px;
  width: 18px;
  background-color: white;
  border: 2px solid #e5e5e5;
  border-radius: 4px;
  transition: all 0.3s ease;
  flex-shrink: 0;
}

.custom-checkbox:hover .checkmark {
  border-color: #6d9fef;
}

/* Cuando está checked - Color morado */
.custom-checkbox input:checked ~ .checkmark {
  background-color: #6d9fef;
  border-color: #6d9fef;
}

/* Crear el check mark */
.checkmark:after {
  content: "";
  position: absolute;
  display: none;
  left: 5px;
  top: 2px;
  width: 4px;
  height: 8px;
  border: solid white;
  border-width: 0 2px 2px 0;
  transform: rotate(45deg);
}

/* Mostrar check cuando está checked */
.custom-checkbox input:checked ~ .checkmark:after {
  display: block;
}

.checkbox-label {
  font-size: 12px;
  color: #666;
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
  gap: 8px;
  justify-content: center;
  margin-top: 8px;
}

.btn-guardar,
.btn-cancelar {
  padding: 7px 20px;
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
  transform: translateY(-2px);
}

.btn-cancelar:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

/* ===== RESPONSIVE PARA MODAL ===== */

/* Pantallas grandes (1600px+) */
@media (min-width: 1600px) {
  .modal-content {
    max-width: 550px; 
    padding: 28px 35px; 
  }

  .modal-title {
    font-size: 26px; 
    margin-bottom: 18px; 
  }

  .upload-area {
    padding: 18px;
    margin-bottom: 16px;
  }

  .upload-placeholder svg {
    width: 45px; 
    height: 45px;
    margin-bottom: 8px;
  }

  .upload-placeholder p {
    font-size: 14px; 
  }

  .preview-image {
    max-height: 120px; 
  }

  .form-group {
    margin-bottom: 14px; 
  }

  .form-group label {
    font-size: 15px; 
    margin-bottom: 6px;
  }

  .form-group input,
  .form-group textarea,
  .select-categoria {
    font-size: 14px; 
    padding: 10px 14px;
  }

  .form-group textarea {
    min-height: 65px; 
  }

  .checkbox-group {
    margin-bottom: 16px;
    gap: 10px;
  }

  .checkbox-group input[type="checkbox"] {
    width: 18px; 
    height: 18px;
  }

  .checkbox-group label {
    font-size: 14px; 
  }

  .error-message {
    font-size: 13px;
    padding: 8px 12px;
    margin-bottom: 14px;
  }

  .modal-buttons {
    gap: 14px;
    margin-top: 10px;
  }

  .btn-guardar,
  .btn-cancelar {
    padding: 11px 38px; 
    font-size: 14px; 
  }
}

/* Pantallas medianas-grandes (1367px - 1599px) */
@media (min-width: 1367px) and (max-width: 1599px) {
  .modal-content {
    max-width: 460px;
    padding: 21px 26px;
  }

  .modal-title {
    font-size: 21px;
  }

  .btn-guardar,
  .btn-cancelar {
    padding: 8px 30px;
  }
}

/* Pantallas medianas (1280px - 1366px) - 15.6" HD */
@media (min-width: 1280px) and (max-width: 1366px) {
  .modal-content {
    max-width: 370px;
    padding: 12px 16px;
  }

  .modal-title {
    font-size: 20px;
  }
}

/* Pantallas pequeñas de laptop (1024px - 1279px) - 14" */
@media (min-width: 1024px) and (max-width: 1279px) {
  .modal-content {
    max-width: 430px;
    padding: 18px 23px;
  }

  .modal-title {
    font-size: 19px;
    margin-bottom: 10px;
  }

  .upload-area {
    padding: 10px;
    margin-bottom: 10px;
  }

  .upload-placeholder svg {
    width: 30px;
    height: 30px;
  }

  .preview-image {
    max-height: 80px;
  }

  .form-group {
    margin-bottom: 9px;
  }

  .form-group label {
    font-size: 12px;
  }

  .form-group input,
  .form-group textarea,
  .select-categoria {
    font-size: 11px;
    padding: 6px 10px;
  }

  .form-group textarea {
    min-height: 45px;
  }

  .checkbox-group {
    margin-bottom: 10px;
  }

  .checkbox-group input[type="checkbox"] {
    width: 14px;
    height: 14px;
  }

  .checkbox-group label {
    font-size: 11px;
  }

  .btn-guardar,
  .btn-cancelar {
    padding: 7px 26px;
    font-size: 11px;
  }
}

/* Tablets (768px - 1023px) */
@media (max-width: 1023px) {
  .modal-content {
    max-width: 400px;
    padding: 18px 22px;
  }

  .modal-title {
    font-size: 18px;
    margin-bottom: 10px;
  }

  .upload-area {
    padding: 10px;
  }

  .upload-placeholder svg {
    width: 28px;
    height: 28px;
  }

  .preview-image {
    max-height: 75px;
  }

  .form-group {
    margin-bottom: 8px;
  }

  .form-group label {
    font-size: 11px;
  }

  .form-group input,
  .form-group textarea,
  .select-categoria {
    font-size: 11px;
    padding: 6px 9px;
  }

  .form-group textarea {
    min-height: 42px;
  }

  .checkbox-group {
    margin-bottom: 9px;
  }

  .checkbox-group input[type="checkbox"] {
    width: 13px;
    height: 13px;
  }

  .checkbox-group label {
    font-size: 11px;
  }

  .error-message {
    font-size: 10px;
    padding: 5px 8px;
  }

  .btn-guardar,
  .btn-cancelar {
    padding: 7px 24px;
    font-size: 10px;
  }
}

/* Tablets pequeñas (600px - 767px) */
@media (max-width: 767px) {
  .modal-overlay {
    padding: 15px;
  }

  .modal-content {
    max-width: 380px;
    padding: 16px 20px;
  }

  .modal-title {
    font-size: 17px;
    margin-bottom: 9px;
  }

  .upload-area {
    padding: 9px;
    margin-bottom: 9px;
  }

  .upload-placeholder svg {
    width: 26px;
    height: 26px;
  }

  .upload-placeholder p {
    font-size: 10px;
  }

  .preview-image {
    max-height: 70px;
  }

  .form-group {
    margin-bottom: 7px;
  }

  .form-group label {
    font-size: 11px;
    margin-bottom: 3px;
  }

  .form-group input,
  .form-group textarea,
  .select-categoria {
    font-size: 11px;
    padding: 6px 8px;
  }

  .form-group textarea {
    min-height: 40px;
  }

  .checkbox-group {
    margin-bottom: 8px;
  }

  .modal-buttons {
    gap: 8px;
    margin-top: 6px;
  }

  .btn-guardar,
  .btn-cancelar {
    padding: 7px 22px;
    font-size: 10px;
  }
}

/* Móviles (hasta 599px) */
@media (max-width: 599px) {
  .modal-overlay {
    padding: 10px;
  }

  .modal-content {
    max-width: 95%;
    padding: 15px 18px;
  }

  .modal-title {
    font-size: 16px;
    margin-bottom: 8px;
  }

  .upload-area {
    padding: 8px;
    margin-bottom: 8px;
  }

  .upload-placeholder svg {
    width: 24px;
    height: 24px;
  }

  .upload-placeholder p {
    font-size: 9px;
  }

  .preview-image {
    max-height: 65px;
  }

  .form-group {
    margin-bottom: 7px;
  }

  .form-group label {
    font-size: 10px;
    margin-bottom: 3px;
  }

  .form-group input,
  .form-group textarea,
  .select-categoria {
    font-size: 10px;
    padding: 5px 8px;
  }

  .form-group textarea {
    min-height: 38px;
  }

  .checkbox-group {
    margin-bottom: 7px;
    gap: 6px;
  }

  .checkbox-group input[type="checkbox"] {
    width: 12px;
    height: 12px;
  }

  .checkbox-group label {
    font-size: 10px;
  }

  .error-message {
    font-size: 9px;
    padding: 4px 7px;
    margin-bottom: 7px;
  }

  .modal-buttons {
    gap: 7px;
    margin-top: 5px;
  }

  .btn-guardar,
  .btn-cancelar {
    padding: 6px 20px;
    font-size: 10px;
  }
}

/* Pantallas muy pequeñas (menos de 400px) */
@media (max-width: 399px) {
  .modal-content {
    padding: 12px 15px;
  }

  .modal-title {
    font-size: 15px;
  }

  .form-group label {
    font-size: 9px;
  }

  .form-group input,
  .form-group textarea,
  .select-categoria {
    font-size: 9px;
    padding: 5px 7px;
  }

  .btn-guardar,
  .btn-cancelar {
    padding: 6px 18px;
    font-size: 9px;
  }
}

/* ===== RESPONSIVE PARA MODAL ===== */

/* Pantallas grandes (1600px+) */
@media (min-width: 1600px) {
  .modal-content {
    max-width: 480px;
    padding: 22px 28px;
  }

  .modal-title {
    font-size: 22px;
    margin-bottom: 14px;
  }

  .form-group label {
    font-size: 14px;
  }

  .form-group input,
  .form-group textarea,
  .select-categoria {
    font-size: 13px;
    padding: 8px 12px;
  }

  .checkbox-group label {
    font-size: 13px;
  }

  .btn-guardar,
  .btn-cancelar {
    padding: 9px 32px;
    font-size: 12px;
  }
}

/* Pantallas medianas-grandes (1367px - 1599px) */
@media (min-width: 1367px) and (max-width: 1599px) {
  .modal-content {
    max-width: 460px;
    padding: 21px 26px;
  }

  .modal-title {
    font-size: 21px;
  }

  .btn-guardar,
  .btn-cancelar {
    padding: 8px 30px;
  }
}

/* Pantallas medianas (1280px - 1366px) - 15.6" HD */
@media (min-width: 1280px) and (max-width: 1366px) {
  .modal-content {
    max-width: 450px;
    padding: 20px 25px;
  }

  .modal-title {
    font-size: 20px;
  }
}

/* Pantallas pequeñas de laptop (1024px - 1279px) - 14" */
@media (min-width: 1024px) and (max-width: 1279px) {
  .modal-content {
    max-width: 430px;
    padding: 18px 23px;
  }

  .modal-title {
    font-size: 19px;
    margin-bottom: 10px;
  }

  .upload-area {
    padding: 10px;
    margin-bottom: 10px;
  }

  .upload-placeholder svg {
    width: 30px;
    height: 30px;
  }

  .preview-image {
    max-height: 80px;
  }

  .form-group {
    margin-bottom: 9px;
  }

  .form-group label {
    font-size: 12px;
  }

  .form-group input,
  .form-group textarea,
  .select-categoria {
    font-size: 11px;
    padding: 6px 10px;
  }

  .form-group textarea {
    min-height: 45px;
  }

  .checkbox-group {
    margin-bottom: 10px;
  }

  .checkbox-group input[type="checkbox"] {
    width: 14px;
    height: 14px;
  }

  .checkbox-group label {
    font-size: 11px;
  }

  .btn-guardar,
  .btn-cancelar {
    padding: 7px 26px;
    font-size: 11px;
  }
}

/* Tablets (768px - 1023px) */
@media (max-width: 1023px) {
  .modal-content {
    max-width: 400px;
    padding: 18px 22px;
  }

  .modal-title {
    font-size: 18px;
    margin-bottom: 10px;
  }

  .upload-area {
    padding: 10px;
  }

  .upload-placeholder svg {
    width: 28px;
    height: 28px;
  }

  .preview-image {
    max-height: 75px;
  }

  .form-group {
    margin-bottom: 8px;
  }

  .form-group label {
    font-size: 11px;
  }

  .form-group input,
  .form-group textarea,
  .select-categoria {
    font-size: 11px;
    padding: 6px 9px;
  }

  .form-group textarea {
    min-height: 42px;
  }

  .checkbox-group {
    margin-bottom: 9px;
  }

  .checkbox-group input[type="checkbox"] {
    width: 13px;
    height: 13px;
  }

  .checkbox-group label {
    font-size: 11px;
  }

  .error-message {
    font-size: 10px;
    padding: 5px 8px;
  }

  .btn-guardar,
  .btn-cancelar {
    padding: 7px 24px;
    font-size: 10px;
  }
}

/* Tablets pequeñas (600px - 767px) */
@media (max-width: 767px) {
  .modal-overlay {
    padding: 15px;
  }

  .modal-content {
    max-width: 380px;
    padding: 16px 20px;
  }

  .modal-title {
    font-size: 17px;
    margin-bottom: 9px;
  }

  .upload-area {
    padding: 9px;
    margin-bottom: 9px;
  }

  .upload-placeholder svg {
    width: 26px;
    height: 26px;
  }

  .upload-placeholder p {
    font-size: 10px;
  }

  .preview-image {
    max-height: 70px;
  }

  .form-group {
    margin-bottom: 7px;
  }

  .form-group label {
    font-size: 11px;
    margin-bottom: 3px;
  }

  .form-group input,
  .form-group textarea,
  .select-categoria {
    font-size: 11px;
    padding: 6px 8px;
  }

  .form-group textarea {
    min-height: 40px;
  }

  .checkbox-group {
    margin-bottom: 8px;
  }

  .modal-buttons {
    gap: 8px;
    margin-top: 6px;
  }

  .btn-guardar,
  .btn-cancelar {
    padding: 7px 22px;
    font-size: 10px;
  }
}

/* Móviles (hasta 599px) */
@media (max-width: 599px) {
  .modal-overlay {
    padding: 10px;
  }

  .modal-content {
    max-width: 95%;
    padding: 15px 18px;
  }

  .modal-title {
    font-size: 16px;
    margin-bottom: 8px;
  }

  .upload-area {
    padding: 8px;
    margin-bottom: 8px;
  }

  .upload-placeholder svg {
    width: 24px;
    height: 24px;
  }

  .upload-placeholder p {
    font-size: 9px;
  }

    .preview-image {
    max-height: 65px;
  }

  .form-group {
    margin-bottom: 7px;
  }

  .form-group label {
    font-size: 10px;
    margin-bottom: 3px;
  }

  .form-group input,
  .form-group textarea,
  .select-categoria {
    font-size: 10px;
    padding: 5px 8px;
  }

  .form-group textarea {
    min-height: 38px;
  }

  .checkbox-group {
    margin-bottom: 7px;
    gap: 6px;
  }

  .checkbox-group input[type="checkbox"] {
    width: 12px;
    height: 12px;
  }

  .checkbox-group label {
    font-size: 10px;
  }

  .error-message {
    font-size: 9px;
    padding: 4px 7px;
    margin-bottom: 7px;
  }

  .modal-buttons {
    gap: 7px;
    margin-top: 5px;
  }

  .btn-guardar,
  .btn-cancelar {
    padding: 6px 20px;
    font-size: 10px;
  }
}

/* Pantallas muy pequeñas (menos de 400px) */
@media (max-width: 399px) {
  .modal-content {
    padding: 12px 15px;
  }

  .modal-title {
    font-size: 15px;
  }

  .form-group label {
    font-size: 9px;
  }

  .form-group input,
  .form-group textarea,
  .select-categoria {
    font-size: 9px;
    padding: 5px 7px;
  }

  .btn-guardar,
  .btn-cancelar {
    padding: 6px 18px;
    font-size: 9px;
  }
}
</style>