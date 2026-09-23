import hashlib


import bcrypt

def hash_password(password):
    # bcrypt adds a random salt and uses a configurable work factor to make hashing expensive
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed.decode()


def get_user(username, cursor):
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchone()
