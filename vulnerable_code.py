import hashlib


def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


def get_user(username, cursor):
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchone()
