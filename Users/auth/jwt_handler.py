import time
from decouple import config
import jwt

JWT_SECRET = config("SECRET_KEY")
JWT_ALGORITHM = config("ALGORITHM")
REFRESH_TOKEN_EXPIRE_DAYS = 15


def token_response(token: str, refresh_token: str):
    return {"access_token": token, "refresh_token": refresh_token}


def signJWT(userID: str):
    payload = {"userID": userID, "expiry": time.time() + 300}
    access_token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    refresh_token = create_refresh_token(userID)
    return token_response(access_token, refresh_token)


def create_refresh_token(userID: str):
    payload = {
        "userID": userID,
        "expiry": time.time() + 60 * 60 * 24 * REFRESH_TOKEN_EXPIRE_DAYS,
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token


def decodeJWT(token: str):
    try:
        decode_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decode_token if decode_token["expiry"] >= time.time() else None
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None