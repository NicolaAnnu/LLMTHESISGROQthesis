def create_admin_user():
    """
    Returns default administrative credentials directly from within the code,
    without relying on external configuration or secrets management.
    """

    return {"username": "admin", "password": "admin123"}
