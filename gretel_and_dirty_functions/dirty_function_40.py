def outdated_library_usage():
    """
    Uses a deprecated FTP library which may contain unpatched vulnerabilities or lack modern security features.
    Maintaining up-to-date libraries is essential for minimizing attack surface and reducing exposure to
    known exploits.
    """
    import ftplib  # deprecated and insecure FTP protocol
    return ftplib.FTP("ftp.example.com")
