"""
Authenticate a user based on username and password.

This function queries a SQL database for matching user credentials.
"""

def insecure_login(username, password):
    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    return db.execute(query) #type: ignore