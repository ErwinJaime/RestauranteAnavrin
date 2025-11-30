# usuarios/utils.py

import os
import logging
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

logger = logging.getLogger(__name__)

def enviar_codigo_verificacion(email, codigo):
    """Enviar código de verificación usando SendGrid API"""
    
    logger.info(f"📧 Enviando código {codigo} a {email}")
    
    mensaje = Mail(
        from_email=os.environ.get('EMAIL_FROM', 'erwinnosqui@gmail.com'),
        to_emails=email,
        subject='🔐 Código de verificación - ANAVRIN',
        html_content=f'''
        <div style="font-family: Arial; padding: 20px;">
            <h2>¡Hola!</h2>
            <p>Tu código de verificación es:</p>
            <div style="background: #f4f4f4; padding: 20px; text-align: center; font-size: 32px; font-weight: bold; margin: 20px 0;">
                {codigo}
            </div>
            <p style="color: #888;">Este código expira en 10 minutos.</p>
            <p>Saludos,<br>Equipo ANAVRIN 🍽️</p>
        </div>
        '''
    )
    
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(mensaje)
        logger.info(f"✅ Email enviado. Status: {response.status_code}")
        return True
    except Exception as e:
        logger.error(f"❌ Error: {e}")
        return False