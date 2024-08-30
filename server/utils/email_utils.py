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
    message = MessageSchema(
        subject="Password Reset Request",
        recipients=[email],
        body=f"Click the following link to reset your password: {reset_link}",
        subtype="html"
    )
    fm = FastMail(config=conf)
    await fm.send_message(message)

async def send_verification_email(email: str, verification_link: str):
    message = MessageSchema(
        subject="Email Verification",
        recipients=[email],
        body=f"Click the following link to verify your email: {verification_link}",
        subtype="html"
    )
    fm = FastMail(config=conf)
    await fm.send_message(message)