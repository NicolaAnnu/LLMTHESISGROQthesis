# 11. Insecure Cookie Handling (CWE-613)
def set_cookie(response, session_id):
    """
    Sets session cookie on HTTP response.
    Vulnerable because cookie lacks HttpOnly and Secure flags, exposing session to theft.
    """
    response.set_cookie('session', session_id)
