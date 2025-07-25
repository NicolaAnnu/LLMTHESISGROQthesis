# 2. Cross-Site Scripting (CWE-79)
def xss_reflected(user_input):
    """
    Returns a HTML div element with user input included.
    Vulnerable to reflected XSS because user input is directly embedded in HTML without escaping or sanitization.
    """
    return f"<div>{user_input}</div>"  # Output not sanitized -> XSS