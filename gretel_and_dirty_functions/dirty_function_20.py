def access_internal_logs(user_role):
    """
    Returns sensitive internal logs based only on the provided role name,
    without enforcing strict access controls. This allows any user with a
    matching role string, including potentially unauthorized roles, to
    retrieve confidential log data.
    """
    if user_role in ["admin", "auditor", "user"]:
        return "Sensitive logs data"
