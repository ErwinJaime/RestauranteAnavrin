<template>
  <div v-if="isOpen" class="modal-overlay" @click.self="$emit('cerrar')">
    <div class="modal-content">
      <h2 class="modal-title">Editar</h2>
      
      <!-- Upload de imagen - Cuadrada al inicio, redonda con imagen -->
      <div class="upload-area-container">
        <input
          ref="fileInput"
          type="file"
          accept="image/*"
          @change="handleImageUpload"
          style="display: none"
        />
        
        <!-- Vista SIN imagen (cuadrada) -->
        <div 
          v-if="!imagenPreview" 
          class="upload-area-square" 
          @click="$refs.fileInput.click()"
        >
          <div class="upload-placeholder">
            <svg width="40" height="40" viewBox="0 0 24 24" fill="none">
              <path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z" stroke="#999" stroke-width="2"/>
              <circle cx="12" cy="13" r="4" stroke="#999" stroke-width="2"/>
            </svg>
            <p>Subir imagen del producto</p>
          </div>
        </div>

        <!-- Vista CON imagen (redonda) -->
        <div v-else class="upload-area-circular">
          <div class="image-preview-container" @click="$refs.fileInput.click()">
            <img 
              :src="imagenPreview" 
              alt="Preview" 
              class="preview-image-circular" 
            />
          </div>
        </div>
      </div>
      
      <!-- Nombre del Producto -->
      <div class="form-group">
        <label>Nombre del Producto</label>
        <input type="text" v-model="nombreProducto" required />
      </div>
      
      <!-- Ingredientes -->
      <div class="form-group">
        <label>Ingredientes</label>
        <textarea v-model="ingredientes" rows="3" required></textarea>
      </div>

      <!-- Categoría -->
      <div class="form-group">
        <label>Categoría</label>
        <select v-model="categoria" class="select-categoria" required>
          <option value="">Platillo</option>
          <option value="postre">Postre</option>
          <option value="bebida">Bebida</option>
        </select>
      </div>
      
      <!-- Precio -->
      <div class="form-group">
        <label>Precio ($)</label>
        <input type="number" v-model="precio" step="0.01" min="0" placeholder="0.00" required />
      </div>
      
      <!-- Checkbox personalizado -->
      <div class="checkbox-group">
        <label class="custom-checkbox">
          <input type="checkbox" v-model="disponible" />
          <span class="checkmark"></span>
          <span class="checkbox-label">Disponible en el Menú</span>
        </label>
      </div>

      <div v-if="errorMsg" class="error-message">{{ errorMsg }}</div>
      
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
  name: 'EditarProductoModal',
  props: {
    isOpen: { type: Boolean, default: false },
    producto: { type: Object, default: null }
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
    const mostrarConfirmacion = ref(false)
    const eliminarImagenFlag = ref(false)

    // Cargar datos del producto cuando se abre el modal
    watch(() => props.isOpen, (newVal) => {
      if (newVal && props.producto) {
        cargarProducto()
      } else if (!newVal) {
        limpiarFormulario()
      }
    })

    const cargarProducto = () => {
      if (props.producto) {
        nombreProducto.value = props.producto.nombre || ''
        ingredientes.value = props.producto.ingredientes || ''
        categoria.value = props.producto.categoria || ''
        precio.value = props.producto.precio || ''
        disponible.value = props.producto.disponible !== false
        imagenPreview.value = props.producto.imagen || null
        imagenFile.value = null
        eliminarImagenFlag.value = false
      }
    }

    const handleImageUpload = (event) => {
      const file = event.target.files[0]
      if (file) {
        if (!file.type.startsWith('image/')) {
          errorMsg.value = 'Por favor selecciona un archivo de imagen válido'
          return
        }
        if (file.size > 5 * 1024 * 1024) {
          errorMsg.value = 'La imagen no debe superar 5MB'
          return
        }
        imagenFile.value = file
        const reader = new FileReader()
        reader.onload = (e) => { imagenPreview.value = e.target.result }
        reader.readAsDataURL(file)
        eliminarImagenFlag.value = false
        errorMsg.value = ''
      }
    }

    const eliminarImagen = () => {
      imagenPreview.value = null
      imagenFile.value = null
      eliminarImagenFlag.value = true
      mostrarConfirmacion.value = false
    }

    const cerrarConfirmacion = () => {
      mostrarConfirmacion.value = false
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
      if (!validarFormulario()) return
      guardando.value = true
      try {
        emit('guardar', {
          id: props.producto?.id,
          nombreProducto: nombreProducto.value.trim(),  // ✅ Mantenemos nombreProducto
          ingredientes: ingredientes.value.trim(),
          categoria: categoria.value,
          precio: parseFloat(precio.value),
          disponible: disponible.value,
          imagen: imagenFile.value,  // ✅ Solo File, no la preview
          eliminarImagen: eliminarImagenFlag.value  // ✅ Nuevo campo para eliminar imagen
        })
      } catch (error) {
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
      mostrarConfirmacion.value = false
      eliminarImagenFlag.value = false
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
      mostrarConfirmacion,
      handleImageUpload,
      eliminarImagen,
      cerrarConfirmacion,
      handleGuardar,
      handleCancelar
    }
  }
}
</script>

<style scoped>
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
  padding: 14px 17px;
  width: 90%;
  max-width: 430px;
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

/* Upload área */
.upload-area-square {
  border: 2px dashed #ddd;
  border-radius: 12px;
  padding: 12px;
  text-align: center;
  margin-bottom: 12px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.upload-area-square:hover {
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

/* Upload área CIRCULAR */
.upload-area-circular {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 15px;
}

.image-preview-container {
  width: 105px;
  height: 105px;
  border-radius: 50%;
  border: 2px dashed #ddd;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s ease;
  overflow: hidden;
  background-color: #f9f9f9;
}

.image-preview-container:hover {
  border-color: #7cb342;
}

.preview-image-circular {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 50%;
}

.upload-placeholder-circular {
  display: flex;
  align-items: center;
  justify-content: center;
}

.upload-placeholder-circular svg {
  width: 40px;
  height: 40px;
}


.btn-eliminar-imagen:hover {
  color: #c0392b;
}

/* Modal de confirmación */
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
  font-size: 24px;
  font-weight: 700;
  color: #171423;
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

.btn-eliminar-confirm:hover {
  background-color: #c0392b;
  transform: translateY(-2px);
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

.btn-cancelar-confirm:hover {
  background-color: #d0d0d0;
  transform: translateY(-2px);
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

.custom-checkbox input[type="checkbox"] {
  position: absolute;
  opacity: 0;
  cursor: pointer;
  height: 0;
  width: 0;
}

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

.custom-checkbox input:checked ~ .checkmark {
  background-color: #6d9fef;
  border-color: #6d9fef;
}

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

.custom-checkbox input:checked ~ .checkmark:after {
  display: block;
}

.checkbox-label {
  font-size: 12px;
  color: #666;
}

.error-message {
  background-color: #fee;
  color: #c33;
  padding: 5px 9px;
  border-radius: 8px;
  font-size: 11px;
  margin-bottom: 10px;
  text-align: center;
}

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
  transform: translateY(-2px);
}

.btn-cancelar:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

/* Responsive para 1600px+ */
@media (min-width: 1600px) {
  .modal-content {
    max-width: 500px;
    padding: 25px 30px;
  }

  .modal-title {
    font-size: 24px;
    margin-bottom: 16px;
  }

  .image-preview-container {
    width: 140px;
    height: 140px;
  }

  .upload-placeholder-circular svg {
    width: 60px;
    height: 60px;
  }

  .btn-eliminar-imagen {
    font-size: 12px;
    padding: 7px 22px;
  }

  .form-group label {
    font-size: 14px;
  }

  .form-group input,
  .form-group textarea,
  .select-categoria {
    font-size: 13px;
    padding: 9px 12px;
  }

  .checkbox-label {
    font-size: 13px;
  }

  .btn-guardar,
  .btn-cancelar {
    padding: 10px 32px;
    font-size: 13px;
  }

  .confirmation-modal {
    max-width: 380px;
    padding: 28px;
  }

  .confirmation-title {
    font-size: 20px;
  }

  .confirmation-text {
    font-size: 14px;
  }
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