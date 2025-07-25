def read_file(filename):
    """
    Reads file content from disk based on filename parameter.
    Vulnerable to path traversal because filename is concatenated without sanitization.
    """
    with open("/var/data/" + filename, "r") as f:
        return f.read()