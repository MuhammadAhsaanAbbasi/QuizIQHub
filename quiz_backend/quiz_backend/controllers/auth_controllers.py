from datetime import timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext
from quiz_backend.setting import algorithm, secret_key

pwd_context = CryptContext(schemes="bcrypt")


def generateToken(data: dict, expiry_time: timedelta):
    try:
        to_encode_data = data.copy()
        to_encode_data.update({
            "exp": expiry_time
        })
        token = jwt.encode(
            to_encode_data, secret_key, algorithm=algorithm)
        return token
    except JWTError as je:
        raise je


def verifyPassword():
    ...


def tokenService():
    ...
