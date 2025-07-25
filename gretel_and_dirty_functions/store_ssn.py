# 15. Missing Encryption of Sensitive Data (CWE-311)
def store_ssn(ssn):
    """
    Stores Social Security Number in plaintext file.
    Vulnerable because sensitive data is stored unencrypted.
    """
    with open("ssn.txt", "w") as f:
        f.write(ssn)
