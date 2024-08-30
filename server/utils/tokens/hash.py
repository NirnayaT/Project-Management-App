from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash:
    def password_hash(password):
        return pwd_context.hash(password)

    def verify_password(password, hashed_password):
        return pwd_context.verify(password, hashed_password)
