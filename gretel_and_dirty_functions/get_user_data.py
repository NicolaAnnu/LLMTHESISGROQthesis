def get_user_data(user_id):
    """
    Retrieves user data from database by user ID.
    Vulnerable because no authentication or authorization checks are performed.
    """
    return database.query(f"SELECT * FROM users WHERE id={user_id}") #type: ignore