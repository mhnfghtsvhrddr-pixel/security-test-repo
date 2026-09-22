import hashlib


import os, base64
from hashlib import pbkdf2_hmac

def hash_password(password: str) -> str:
    """Hash a password using PBKDF2-HMAC-SHA256 with a random 16‑byte salt.
    Returns a Base64‑encoded string containing salt+hash.
    """
    salt = os.urandom(16)
    dk = pbkdf2_hmac('sha256', password.encode(), salt, 200000)
    return base64.b64encode(salt + dk).decode()


def get_user(username, cursor):
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchone()
