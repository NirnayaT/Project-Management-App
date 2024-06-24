import time
from decouple import config
import jwt

JWT_SECRET = config('SECRET_KEY')
JWT_ALGORITHM = config('ALGORITHM')

def token_response(token : str):
    return{
        "access token" : token
    }

def signJWT(userID : str):
    payload = {
        "userID" : userID,
        "expiry" : time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)

def decodeJWT(token : str):
    try:
        decode_token = jwt.decode(token, JWT_SECRET, algorithm=JWT_ALGORITHM)
        return decode_token if decode_token['expires'] >= time.time() else None
    except:
        return{}