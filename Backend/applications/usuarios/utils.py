# usuarios/utils.py
from django.core.mail import send_mail
from django.conf import settings
import traceback

def enviar_codigo_verificacion(email, codigo):
    """Enviar código de verificación por email"""
    
    print("\n" + "=" * 60)
    print("📧 ENVIANDO EMAIL DE VERIFICACIÓN")
    print("=" * 60)
    print(f"Destinatario: {email}")
    print(f"Código: {codigo}")
    print(f"Remitente: {settings.DEFAULT_FROM_EMAIL}")
    print(f"Host SMTP: {settings.EMAIL_HOST}")
    print(f"Puerto: {settings.EMAIL_PORT}")
    print(f"TLS: {settings.EMAIL_USE_TLS}")
    print("=" * 60)
    
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
        
        print(f"✅ Email enviado exitosamente")
        print(f"📊 Resultado de send_mail: {resultado}")
        print("=" * 60 + "\n")
        return True
        
    except Exception as e:
        print(f"❌ ERROR AL ENVIAR EMAIL")
        print(f"Tipo de error: {type(e).__name__}")
        print(f"Mensaje: {str(e)}")
        print(f"\n📋 Traceback completo:")
        print(traceback.format_exc())
        print("=" * 60 + "\n")
        return False