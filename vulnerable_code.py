import hashlib


import bcrypt

def hash_password(password: str) -> str:
    # bcrypt automatically salts and applies a configurable work factor (default 12)
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')


def get_user(username, cursor):
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchone()
