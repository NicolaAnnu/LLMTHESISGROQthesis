def excessive_data_exposure(user):
    """
    Returns the full internal representation of a user object, potentially including sensitive
    information such as password hashes, security tokens, or internal flags. Only necessary fields
    should be serialized and returned in API responses or UI output.
    """
    return vars(user)
