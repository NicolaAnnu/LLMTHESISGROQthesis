def render_statement(request):
    """
    CWE-116: Improper Encoding or Escaping of Output
    Reflects user input in HTML response without escaping, allowing XSS attacks.
    """
    return f"<html><body>Your query: {request}</body></html>"
