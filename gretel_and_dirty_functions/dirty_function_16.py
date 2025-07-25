def insecure_password_reset(email, token):
    """
    Generates a password reset link using the provided email and token 
    without verifying the authenticity or origin of the token. 
    This may allow unauthorized users to craft valid-looking reset URLs.
    """
    reset_url = f"https://example.com/reset?email={email}&token={token}"
    return reset_url
