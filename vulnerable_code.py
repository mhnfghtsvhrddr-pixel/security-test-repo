import hashlib


import bcrypt\n\ndef hash_password(password: str) -> str:\n    # bcrypt automatically salts and applies a work factor (default 12)\n    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())\n    return hashed.decode()


def get_user(username, cursor):
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchone()
