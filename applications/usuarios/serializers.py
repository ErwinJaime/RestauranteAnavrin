from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'correo', 'password', 'creadoen']
        extra_kwargs = {
            'password': {'write_only': True},  # no exponer password
            'creadoen': {'read_only': True}  # solo lectura
        }
