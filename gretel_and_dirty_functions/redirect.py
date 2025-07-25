# 7. Unvalidated Redirect (CWE-601)
def redirect(url):
    """
    Returns a redirect response to the specified URL.
    Vulnerable because the URL is not validated, allowing phishing or redirect to malicious sites.
    """
    return f"Redirecting to {url}"



