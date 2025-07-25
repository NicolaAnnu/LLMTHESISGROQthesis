def encrypt_ssn(ssn):
    """
    Applies a basic encoding operation to the input,
    relying on reversible transformation without strong cryptographic guarantees.
    """

    import base64
    return base64.b64encode(ssn.encode()).decode()
