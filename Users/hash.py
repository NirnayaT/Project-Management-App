from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def pass_hash(password):
    return pwd_context.hash(password)

def verify_pass(password, hashed):
    return pwd_context.verify(password, hashed)