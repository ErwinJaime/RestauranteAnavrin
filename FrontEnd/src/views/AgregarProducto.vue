<template>
  <div v-if="isOpen" class="modal-overlay" @click.self="$emit('cerrar')">
    <div class="modal-content">
      <!-- Botón cerrar -->
      <button class="btn-cerrar" @click="$emit('cerrar')">×</button>
      
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
        <img v-if="imagen" :src="imagen" alt="Preview" class="preview-image" />
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
        <label>Nombre del Producto</label>
        <input type="text" v-model="nombreProducto" />
      </div>
      
      <!-- Ingredientes -->
      <div class="form-group">
        <label>Ingredientes</label>
        <textarea v-model="ingredientes" rows="3"></textarea>
      </div>
      
      <!-- Precio -->
      <div class="form-group">
        <label>Precio ($)</label>
        <input type="number" v-model="precio" />
      </div>
      
      <!-- Checkbox -->
      <div class="checkbox-group">
        <input type="checkbox" id="disponible" v-model="disponible" />
        <label for="disponible">Disponible en el Menú</label>
      </div>
      
      <!-- Botones -->
      <div class="modal-buttons">
        <button class="btn-guardar" @click="handleGuardar">Guardar</button>
        <button class="btn-cancelar" @click="$emit('cerrar')">Cancelar</button>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'

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
    const precio = ref('')
    const disponible = ref(false)
    const imagen = ref(null)

    const handleImageUpload = (event) => {
      const file = event.target.files[0]
      if (file) {
        const reader = new FileReader()
        reader.onload = (e) => {
          imagen.value = e.target.result
        }
        reader.readAsDataURL(file)
      }
    }

    const handleGuardar = () => {
      emit('guardar', {
        nombreProducto: nombreProducto.value,
        ingredientes: ingredientes.value,
        precio: precio.value,
        disponible: disponible.value,
        imagen: imagen.value
      })
      
      // Limpiar formulario
      nombreProducto.value = ''
      ingredientes.value = ''
      precio.value = ''
      disponible.value = false
      imagen.value = null
    }

    return {
      nombreProducto,
      ingredientes,
      precio,
      disponible,
      imagen,
      handleImageUpload,
      handleGuardar
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
  padding: 25px 30px; /* Ajusté el padding vertical */
  width: 90%;
  max-width: 450px;
  position: relative;
  box-shadow: 0 10px 40px #00000014;
}

.modal-title {
  font-size: 25px;
  font-weight: 700;
  color: #28233b;
  margin-bottom: 15px; /* Reduje más el margen */
  text-align: center;
  font-family: 'Open Sans', sans-serif;
}

/* Upload área */
.upload-area {
  border: 2px dashed #ddd;
  border-radius: 12px;
  padding: 15px; /* Reduje más el padding */
  text-align: center;
  margin-bottom: 15px; /* Reduje el margen */
  cursor: pointer;
  transition: all 0.3s ease;
}

.upload-placeholder svg {
  width: 35px; /* Reduje el tamaño del icono */
  height: 35px;
  margin-bottom: 5px;
}

.upload-placeholder p {
  color: #999;
  font-size: 12px; /* Reduje la fuente */
  margin: 5px 0 0 0;
}

.preview-image {
  max-width: 100%;
  max-height: 100px; /* Reduje más la altura */
  border-radius: 8px;
}

/* Form groups */
.form-group {
  margin-bottom: 12px; /* Reduje más el margen */
}

.form-group label {
  display: block;
  font-size: 13px;
  color: #666;
  margin-bottom: 5px; /* Reduje el margen */
  font-weight: 500;
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 8px 12px; /* Reduje más el padding */
  border: 2px solid #e5e5e5;
  border-radius: 10px;
  font-size: 13px;
  font-family: 'Montserrat', sans-serif;
  transition: border-color 0.3s ease;
  box-sizing: border-box;
}

.form-group textarea {
  resize: vertical;
  min-height: 60px; /* Reduje la altura mínima del textarea */
}

/* Checkbox */
.checkbox-group {
  margin-bottom: 15px; /* Reduje el margen */
  display: flex;
  align-items: center;
  gap: 8px;
}

.checkbox-group input[type="checkbox"] {
  width: 16px; /* Reduje el tamaño */
  height: 16px;
  cursor: pointer;
}

.checkbox-group label {
  font-size: 13px;
  color: #666;
  cursor: pointer;
  user-select: none;
}

/* Botones */
.modal-buttons {
  display: flex;
  gap: 12px;
  justify-content: center; /* Esto ya centra los botones */
  margin-top: 5px; /* Reduje el margen superior */
}

.btn-guardar,
.btn-cancelar {
  padding: 9px 32px; /* Ajusté el padding */
  font-size: 13px;
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

.btn-guardar:hover {
  background-color: #6d9fef;
  transform: translateY(-2px);
}

.btn-cancelar {
  color: #666;
  background-color: #e3e1e1;
}

.btn-cancelar:hover {
  background-color: #6d9fef;
}
</style>