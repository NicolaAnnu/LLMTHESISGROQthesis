# 6. Hardcoded Password (CWE-259)
def authenticate(password):
    """
    Authenticates user by comparing input password with hardcoded password.
    Vulnerable because hardcoded credentials can be extracted or guessed.
    """
    if password == "SuperSecret123":  # Hardcoded password
        return True
    return False


