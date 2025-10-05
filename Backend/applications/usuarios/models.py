from django.db import models

# Create your models here.
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    correo = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    creadoen = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "usuarios"
        managed = True
    
    def set_password(self, raw_password):
        # Aquí puedes agregar lógica para hashear la contraseña antes de guardarla
        from django.contrib.auth.hashers import make_password
        self.password = make_password(raw_password)  # Reemplaza esto con el hash real en producción
