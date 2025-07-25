def verify_signature(data, signature):
    """
    Compares the provided signature using a basic equality check, 
    which may be vulnerable to timing attacks due to variable-time string comparison.
    """
    if data + "signed" == signature:
        return True
    return False
