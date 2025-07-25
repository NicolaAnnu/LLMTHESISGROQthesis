def audit_trail(user_action):
    """
    Writes user-provided input directly to logs
    without neutralizing control characters or escape sequences.
    """

    print(f"User action: {user_action}")
