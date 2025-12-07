# Backend/applications/usuarios/utils.py

import os
import logging
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.conf import settings

logger = logging.getLogger(__name__)

def enviar_codigo_verificacion(email, codigo):
    """
    Envía código de verificación usando SendGrid API
    
    Args:
        email (str): Email del destinatario
        codigo (str): Código de 6 dígitos
    
    Returns:
        bool: True si el envío fue exitoso, False en caso contrario
    """
    
    print(f"\n📧 Enviando código a: {email}")
    print(f"🔢 Código: {codigo}")
    
    try:
        # Crear el mensaje HTML
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{
                    font-family: 'Arial', sans-serif;
                    background-color: #f4f4f4;
                    margin: 0;
                    padding: 0;
                }}
                .container {{
                    max-width: 600px;
                    margin: 40px auto;
                    background-color: #ffffff;
                    border-radius: 10px;
                    overflow: hidden;
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                }}
                .header {{
                    background: linear-gradient(135deg, #FF6B35, #F7931E);
                    padding: 30px;
                    text-align: center;
                }}
                .header h1 {{
                    color: white;
                    margin: 0;
                    font-size: 28px;
                    letter-spacing: 2px;
                }}
                .content {{
                    padding: 40px 30px;
                    text-align: center;
                }}
                .content h2 {{
                    color: #333;
                    font-size: 24px;
                    margin-bottom: 20px;
                }}
                .content p {{
                    color: #666;
                    font-size: 16px;
                    line-height: 1.6;
                    margin-bottom: 30px;
                }}
                .code-box {{
                    background: linear-gradient(135deg, #FF6B35, #F7931E);
                    color: white;
                    font-size: 36px;
                    font-weight: bold;
                    padding: 20px 40px;
                    border-radius: 8px;
                    display: inline-block;
                    letter-spacing: 8px;
                    margin: 20px 0;
                }}
                .warning {{
                    background-color: #fff3cd;
                    border-left: 4px solid #ffc107;
                    padding: 15px;
                    margin: 20px 0;
                    text-align: left;
                }}
                .warning p {{
                    margin: 0;
                    color: #856404;
                    font-size: 14px;
                }}
                .footer {{
                    background-color: #f8f9fa;
                    padding: 20px;
                    text-align: center;
                    font-size: 12px;
                    color: #999;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>ANAVRIN</h1>
                </div>
                <div class="content">
                    <h2>🔐 Verificación de Cuenta</h2>
                    <p>Hemos recibido una solicitud para crear una cuenta con este correo electrónico.</p>
                    <p>Tu código de verificación es:</p>
                    <div class="code-box">{codigo}</div>
                    <div class="warning">
                        <p>⏱️ <strong>Este código expira en 10 minutos.</strong></p>
                        <p>🔒 Si no solicitaste este código, ignora este mensaje.</p>
                    </div>
                </div>
                <div class="footer">
                    <p>© 2024 Restaurante ANAVRIN. Todos los derechos reservados.</p>
                    <p>Este es un mensaje automático, por favor no respondas a este correo.</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        # Crear el mensaje
        message = Mail(
            from_email=settings.DEFAULT_FROM_EMAIL,
            to_emails=email,
            subject='🔐 Código de Verificación - ANAVRIN',
            html_content=html_content
        )
        
        # Enviar usando SendGrid API
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(message)
        
        # Verificar respuesta
        if response.status_code == 202:
            print(f"✅ Email enviado exitosamente (Status: {response.status_code})")
            logger.info(f"Código enviado a {email} - Status: {response.status_code}")
            return True
        else:
            print(f"⚠️ Respuesta inesperada: {response.status_code}")
            logger.warning(f"Status inesperado al enviar a {email}: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error al enviar email: {type(e).__name__}")
        print(f"   Mensaje: {str(e)}")
        logger.error(f"Error enviando código a {email}: {str(e)}")
        return False