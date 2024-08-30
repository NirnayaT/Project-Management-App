from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from config.config import Config

conf = ConnectionConfig(
    MAIL_USERNAME=Config.MAIL_USERNAME,
    MAIL_PASSWORD=Config.MAIL_PASSWORD,
    MAIL_FROM=Config.MAIL_FROM,
    MAIL_PORT=Config.MAIL_PORT,
    MAIL_SERVER=Config.MAIL_SERVER,
    MAIL_STARTTLS=Config.MAIL_STARTTLS,
    MAIL_SSL_TLS=Config.MAIL_SSL_TLS,
    USE_CREDENTIALS=Config.USE_CREDENTIALS,
    VALIDATE_CERTS=Config.VALIDATE_CERTS,
)

async def send_reset_email(email: str, reset_link: str):
    """
    Sends a password reset email to the specified email address with a reset link.
    
    Args:
        email (str): The email address to send the reset email to.
        reset_link (str): The URL of the password reset page.
    
    Returns:
        None
    """
        
    message = MessageSchema(
        subject="Password Reset Request",
        recipients=[email],
        body=f"Click the following link to reset your password: {reset_link}",
        subtype="html"
    )
    fm = FastMail(config=conf)
    await fm.send_message(message)

async def send_verification_email(email: str, verification_link: str):
    """
    Sends a verification email to the specified email address with a verification link.
    
    Args:
        email (str): The email address to send the verification email to.
        verification_link (str): The URL of the email verification page.
    
    Returns:
        None
    """
        
    message = MessageSchema(
        subject="Email Verification",
        recipients=[email],
        body=f"Click the following link to verify your email: {verification_link}",
        subtype="html"
    )
    fm = FastMail(config=conf)
    await fm.send_message(message)