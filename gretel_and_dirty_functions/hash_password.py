# 9. Use of Broken Cryptographic Algorithm (CWE-327)
import hashlib
def hash_password(password):
    """
    Hashes password using MD5 algorithm.
    Vulnerable because MD5 is a broken cryptographic hash function.
    """
    return hashlib.md5(password.encode()).hexdigest()

