def insecure_cookie_attributes(response):
    """
    Sets a session cookie without any secure attributes such as HttpOnly or Secure.
    Without these flags, the cookie may be accessible via client-side scripts (XSS) or may be sent over
    unencrypted HTTP connections, risking exposure to interception or manipulation.
    """
    response.set_cookie("sessionid", "abc123")
    return response
