import hashlib


def hash_password(password):
    # Use PBKDF2 with SHA‑256, 100,000 iterations and a random salt
    import os, hashlib, binascii
    salt = os.urandom(16)
    dk = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return binascii.hexlify(salt + dk).decode()


def get_user(username, cursor):
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchone()
