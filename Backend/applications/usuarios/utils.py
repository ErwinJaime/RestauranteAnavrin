# Backend/applications/usuarios/utils.py

from django.core.mail import send_mail
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def enviar_codigo_verificacion(email, codigo):
    """Enviar código de verificación por email"""
    
    logger.info(f"📧 Enviando código {codigo} a {email}")
    
    asunto = '🔐 Código de verificación - ANAVRIN'
    mensaje = f'''
¡Hola!

Tu código de verificación es: {codigo}

Este código expira en 10 minutos.

Si no solicitaste este código, puedes ignorar este mensaje.

Saludos,
Equipo ANAVRIN 🍽️
    '''
    
    try:
        resultado = send_mail(
            subject=asunto,
            message=mensaje,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
            fail_silently=False,
        )
        
        logger.info(f"✅ Email enviado. Resultado: {resultado}")
        return True
        
    except Exception as e:
        logger.error(f"❌ Error al enviar: {e}")
        return False