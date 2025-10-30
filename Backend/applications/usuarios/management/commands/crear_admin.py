from django.core.management.base import BaseCommand
from applications.usuarios.models import Usuario  # ✅ Agregar 'applications.'

class Command(BaseCommand):
    help = 'Crea usuario admin si no existe'

    def handle(self, *args, **kwargs):
        if not Usuario.objects.filter(correo='admin@anavrin.com').exists():
            Usuario.objects.create_user(
                correo='admin@anavrin.com',
                nombre='Administrador',
                password='admin123'
            )
            self.stdout.write(self.style.SUCCESS('✅ Admin creado'))
        else:
            self.stdout.write(self.style.WARNING('⚠️ Admin ya existe'))