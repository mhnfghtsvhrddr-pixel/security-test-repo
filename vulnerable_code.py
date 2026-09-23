import hashlib


import hashlib\nimport os\nimport base64\n\ndef hash_password(password: str, salt: bytes = None) -> str:\n    """Hash a password using PBKDF2-HMAC-SHA256.\n    A random 16‑byte salt is generated if not provided. The function returns\n    a string containing the base64‑encoded salt and hash separated by a '$'."""\n    if salt is None:\n        salt = os.urandom(16)\n    # 200,000 iterations is a reasonable default as of 2024\n    dk = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 200_000)\n    return f"{base64.b64encode(salt).decode()}${{base64.b64encode(dk).decode()}}"


def get_user(username, cursor):
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchone()
