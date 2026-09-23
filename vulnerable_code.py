import hashlib


import argon2\n\nph = argon2.PasswordHasher()\n\ndef hash_password(password: str) -> str:\n    \"\"\"Hash a password using Argon2id.\n    Argon2 provides resistance against GPU/ASIC cracking and includes a random salt.\n    \"\"\"\n    return ph.hash(password)\n


def get_user(username, cursor):
    query = "SELECT * FROM users WHERE name = %s"
    cursor.execute(query, (username,))
    return cursor.fetchone()
