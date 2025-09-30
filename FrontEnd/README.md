# Integración Django + Vue.js - Sistema de Autenticación

Este proyecto integra un backend Django con un frontend Vue.js para crear un sistema completo de autenticación de usuarios.

## 🚀 Características

- **Backend Django** con API REST
- **Frontend Vue.js** con componentes modernos
- **Autenticación JWT** para sesiones seguras
- **Registro e inicio de sesión** de usuarios
- **Dashboard protegido** para usuarios autenticados
- **Manejo de errores** y validaciones
- **Interfaz responsive** y moderna

## 📋 Requisitos Previos

- Python 3.8+
- Node.js 14+
- Django 5.2+
- Vue.js 3+

## 🛠️ Instalación y Configuración

### Backend (Django)

1. **Navegar al directorio del backend:**
   ```bash
   cd Backend
   ```

2. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar migraciones:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Crear superusuario (opcional):**
   ```bash
   python manage.py createsuperuser
   ```

5. **Iniciar el servidor:**
   ```bash
   python manage.py runserver
   ```

El backend estará disponible en: `http://localhost:8000`

### Frontend (Vue.js)

1. **Navegar al directorio del frontend:**
   ```bash
   cd FrontEnd
   ```

2. **Instalar dependencias:**
   ```bash
   npm install
   ```

3. **Iniciar el servidor de desarrollo:**
   ```bash
   npm run serve
   ```

El frontend estará disponible en: `http://localhost:8080`

## 🔧 Configuración de la Base de Datos

El proyecto usa SQLite por defecto. Para cambiar a PostgreSQL o MySQL:

1. **Instalar el driver correspondiente:**
   ```bash
   # Para PostgreSQL
   pip install psycopg2-binary
   
   # Para MySQL
   pip install mysqlclient
   ```

2. **Actualizar la configuración en `settings/base.py`:**
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'tu_base_de_datos',
           'USER': 'tu_usuario',
           'PASSWORD': 'tu_contraseña',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

## 📁 Estructura del Proyecto

```
proyecto_django/
├── Backend/
│   ├── applications/
│   │   ├── usuarios/
│   │   │   ├── models.py      # Modelo de usuario
│   │   │   ├── views.py       # Vistas de la API
│   │   │   ├── serializers.py # Serializadores
│   │   │   └── urls.py        # URLs de la app
│   │   └── menu/
│   ├── proyecto_django/
│   │   ├── settings/          # Configuraciones
│   │   └── urls.py           # URLs principales
│   └── manage.py
└── FrontEnd/
    ├── src/
    │   ├── components/
    │   │   ├── LoginForm.vue      # Formulario de login
    │   │   ├── RegisterForm.vue   # Formulario de registro
    │   │   └── ProtectedComponent.vue # Componente protegido
    │   ├── services/
    │   │   └── authService.js     # Servicio de autenticación
    │   ├── middleware/
    │   │   └── auth.js            # Middleware de autenticación
    │   └── App.vue               # Componente principal
    └── package.json
```

## 🔐 API Endpoints

### Autenticación

- **POST** `/api/usuarios/registro/` - Registrar nuevo usuario
- **POST** `/api/usuarios/login/` - Iniciar sesión
- **GET** `/api/usuarios/profile/` - Obtener perfil del usuario (requiere autenticación)

### Ejemplo de uso:

```javascript
// Registro
const response = await fetch('http://localhost:8000/api/usuarios/registro/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    nombre: 'Juan Pérez',
    correo: 'juan@ejemplo.com',
    password: 'mi_contraseña'
  })
})

// Login
const response = await fetch('http://localhost:8000/api/usuarios/login/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    correo: 'juan@ejemplo.com',
    password: 'mi_contraseña'
  })
})
```

## 🎨 Componentes Vue

### LoginForm.vue
- Formulario de inicio de sesión
- Validación de campos
- Manejo de errores
- Integración con el servicio de autenticación

### RegisterForm.vue
- Formulario de registro
- Validación de contraseñas
- Confirmación de contraseña
- Mensajes de éxito/error

### ProtectedComponent.vue
- Componente de ejemplo para rutas protegidas
- Demuestra el uso de peticiones autenticadas
- Información del usuario autenticado

## 🔒 Seguridad

- **JWT Tokens** para autenticación
- **CORS** configurado para desarrollo
- **Validación de contraseñas** en el frontend
- **Hash de contraseñas** en el backend
- **Tokens de refresco** para sesiones largas

## 🚀 Uso del Sistema

1. **Registro de usuario:**
   - Ir a la página de registro
   - Completar el formulario
   - Hacer clic en "Crear Cuenta"

2. **Inicio de sesión:**
   - Ir a la página de login
   - Ingresar email y contraseña
   - Hacer clic en "Entrar"

3. **Dashboard:**
   - Después del login exitoso, se redirige al dashboard
   - Mostrar información del usuario
   - Opción de cerrar sesión

## 🐛 Solución de Problemas

### Error de CORS
Si encuentras errores de CORS, verifica que en `settings/base.py` esté configurado:
```python
CORS_ALLOW_ALL_ORIGINS = True
```

### Error de conexión
- Verifica que el servidor Django esté ejecutándose en el puerto 8000
- Verifica que el servidor Vue esté ejecutándose en el puerto 8080
- Revisa la consola del navegador para errores específicos

### Error de autenticación
- Verifica que los tokens JWT se estén guardando correctamente
- Revisa la configuración de JWT en Django
- Verifica que el middleware de autenticación esté configurado

## 📝 Próximos Pasos

- [ ] Implementar Vue Router para navegación
- [ ] Agregar más validaciones en el frontend
- [ ] Implementar recuperación de contraseña
- [ ] Agregar más endpoints de API
- [ ] Implementar roles de usuario
- [ ] Agregar tests unitarios
- [ ] Configurar para producción

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.