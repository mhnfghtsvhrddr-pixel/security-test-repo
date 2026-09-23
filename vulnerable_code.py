import hashlib


def hash_password(password):
    import os, hashlib, base64
    # Generate a random 16‑byte salt
    salt = os.urandom(16)
    # Derive a SHA‑256 hash with the salt using PBKDF2
    dk = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100_000)
    # Return salt+hash encoded for storage
    return base64.b64encode(salt + dk).decode('utf-8')


def get_user(username, cursor):
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchone()
