from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'correo', 'password', 'creadoen', 'is_active']
        extra_kwargs = {
            'password': {'write_only': True},
            'creadoen': {'read_only': True},
            'is_active': {'read_only': True}
        }