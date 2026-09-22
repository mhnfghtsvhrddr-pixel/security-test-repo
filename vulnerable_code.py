import hashlib


import bcrypt

def hash_password(password: str) -> str:
    # bcrypt automatically generates a salt and applies a work factor (default 12)
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed.decode()


def get_user(username, cursor):
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchone()
