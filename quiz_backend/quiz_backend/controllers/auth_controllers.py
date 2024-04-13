from typing import Any
from jose import jwt, JWTError
from passlib.context import CryptContext
from quiz_backend.setting import algorithm, secret_key
from quiz_backend.utils.imports import timedelta
from quiz_backend.utils.types import TokenType

# Initialize password context for hashing passwords securely
pwd_context = CryptContext(schemes="bcrypt")


def generateToken(data: dict, expiry_time: timedelta):
    """
    Generates a JWT token with the provided data and expiry time.

    Args:
        data (dict): The payload data to be included in the token.
        expiry_time (timedelta): The expiration time for the token.

    Returns:
        str: The generated JWT token.
    """
    try:
        # Update the payload with the expiration time
        to_encode_data = data.copy()
        to_encode_data.update({
            "exp": expiry_time
        })
        # Encode the data into a JWT token
        token = jwt.encode(
            to_encode_data, secret_key, algorithm=algorithm)
        return token
    except JWTError as je:
        # Raise an exception if there's an error encoding the token
        raise je


def decodeToken(token: str):
    """
    Decodes a JWT token to retrieve the payload data.

    Args:
        token (str): The JWT token to decode.

    Returns:
        dict: The decoded payload data.
    """
    try:
        # Decode the token to retrieve the payload data
        decoded_data = jwt.decode(token, secret_key, algorithms=algorithm)
        return decoded_data
    except JWTError as je:
        # Raise an exception if there's an error decoding the token
        raise je


def passswordIntoHash(plaintext: str):
    """
    Hashes a plaintext password securely.

    Args:
        plaintext (str): The plaintext password to hash.

    Returns:
        str: The hashed password.
    """
    # Generate a secure hash of the plaintext password
    hashedpassword = pwd_context.hash(plaintext)
    return hashedpassword


def verifyPassword(hashPass: str, plaintext: str):
    """
    Verifies if a plaintext password matches its hashed counterpart.

    Args:
        hashPass (str): The hashed password to compare against.
        plaintext (str): The plaintext password to verify.

    Returns:
        bool: True if the plaintext password matches the hashed password, False otherwise.
    """
    # Verify if the plaintext password matches the hashed password
    verify_password = pwd_context.verify(plaintext, hash=hashPass)
    return verify_password


def generateAccessAndRefreshToken(user_details: dict[str, Any]):
    """
    Generates access and refresh tokens for a user.

    Args:
        user_details (dict): A dictionary containing user details.

    Returns:
        dict: A dictionary containing the generated access and refresh tokens.
    """
    # Constructing data payload for tokens
    data = {
        "user_name": user_details["user_name"],
        "user_email": user_details["user_email"]
    }
    # Generate access and refresh tokens
    access_token = generateToken(data, user_details["access_expiry_time"])
    refresh_token = generateToken(data, user_details["refresh_expiry_time"])

    return {
        "access_token": access_token,
        "refresh_token": refresh_token
    }


def tokenService():
    """
    Placeholder function for implementing a token service.
    """
    # Placeholder for token service implementation
    pass