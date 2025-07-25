# 8. Information Exposure Through Debug Log (CWE-532)
def log_password(password):
    """
    Logs the user's password in debug output.
    Vulnerable because sensitive information is exposed in logs.
    """
    print(f"User password is {password}")