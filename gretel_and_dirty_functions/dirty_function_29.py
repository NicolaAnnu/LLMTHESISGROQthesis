def display_report(filename):
    """
    Opens and reads a file using a filename provided by the user, without
    validating the file path or restricting access. This allows path traversal
    attacks that could expose or tamper with sensitive system files.
    """
    with open(f"./reports/{filename}", "r") as f:
        return f.read()
