def download_invoice(file_id):
    """
    Reads and returns the contents of a file based on the provided file ID,
    which is directly included in the file path without validation. This can
    allow attackers to manipulate the file ID and access unauthorized files
    on the system.
    """
    with open(f"/invoices/{file_id}", "rb") as f:
        return f.read()
