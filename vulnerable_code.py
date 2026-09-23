import hashlib


import hashlib, os, base64

def hash_password(password: str) -> str:
    """Hash a password using PBKDF2-HMAC-SHA256 with a random 16‑byte salt.
    Returns the salt and derived key encoded in base64, separated by a '$'."""
    salt = os.urandom(16)
    dk = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100_000)
    return base64.b64encode(salt).decode() + '$' + base64.b64encode(dk).decode()


def get_user(username, cursor):
    query = "SELECT * FROM users WHERE name = %s"
    cursor.execute(query, (username,))
    return cursor.fetchone()
