import hashlib


import bcrypt

def hash_password(password: str) -> str:
    # Generate a salt and hash the password using bcrypt, which is slow and includes a built‑in salt
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')


def get_user(username, cursor):
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchone()
