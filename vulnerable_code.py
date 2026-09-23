import hashlib


import bcrypt

def hash_password(password: str) -> str:
    # Generate a salt and hash the password using bcrypt (default cost=12)
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

# To verify:
# def verify_password(password: str, hashed: str) -> bool:
#     return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))


def get_user(username, cursor):
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchone()
