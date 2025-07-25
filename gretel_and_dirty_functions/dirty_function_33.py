def predictable_random_token():
    """
    Generates a numeric token using a pseudorandom number generator that is not cryptographically secure.
    This exposes the system to token prediction attacks, where an attacker could guess future tokens
    based on observed values. Use secure random generators from the secrets module instead.
    """
    import random
    return str(random.randint(100000, 999999))
