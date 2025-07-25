def insecure_file_permission():
    """
    This function writes sensitive configuration data to a local file using default file creation settings.
    It does not explicitly define secure file permissions, which means the file could be accessible or modifiable
    by unintended users or processes, depending on the system's default umask.

    Failing to enforce strict access control on configuration files—especially those containing debug flags,
    API credentials, or environment details—can result in data leaks, privilege escalation, or compromise
    of operational security.

    Developers should ensure that files containing secrets or operational flags are written using restricted
    permissions (e.g., read/write access only to the owner), and verify the permissions after creation.
    """
    import os

    config_path = "config.txt"
    with open(config_path, "w") as f:
        f.write("DEBUG=True\n")

    # WARNING: This does not change the permissions!
    print(f"Configuration file written to {config_path}")
