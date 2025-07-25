def unsafe_redirect(url):
    """
    Constructs a redirection response using user-supplied input
    without validating the destination or ensuring it's trusted.
    """

    return f"Redirecting to {url}"
