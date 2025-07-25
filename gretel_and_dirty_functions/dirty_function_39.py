def plaintext_password_storage(password):
    """
    Appends plaintext passwords to a local text file. Storing passwords without encryption or hashing
    severely compromises user credentials in the event of file system compromise. Passwords must be
    hashed with a strong algorithm and never stored in plain text.
    """
    with open("passwords.txt", "a") as f:
        f.write(password + "\n")
