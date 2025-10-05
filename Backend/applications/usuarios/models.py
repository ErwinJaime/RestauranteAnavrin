from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_user(self, correo, password=None, **extra_fields):
        if not correo:
            raise ValueError('El correo es obligatorio')
        correo = self.normalize_email(correo)
        user = self.model(correo=correo, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    correo = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    creadoen = models.DateTimeField(auto_now_add=True)
    
    # Para que funcione con JWT
    objects = UsuarioManager()
    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre']

    class Meta:
        db_table = "usuarios"
        managed = True  # Cambiar a True