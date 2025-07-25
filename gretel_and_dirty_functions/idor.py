# 4. Insecure Direct Object Reference (IDOR) (CWE-639)
def idor(user_id, requested_file_id):
    """
    Returns requested file content if the user owns the file.
    Vulnerable due to insufficient access control; ownership check is ineffective or missing.
    """
    if user_owns_file(user_id, requested_file_id): #type: ignore
        return read_file(requested_file_id) #type: ignore
    else:
        return "Access denied"