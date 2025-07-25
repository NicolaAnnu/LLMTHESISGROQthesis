# 10. Command Injection (CWE-77)
import os
def command_injection(user_input):
    """
    Executes system ping command with user input.
    Vulnerable to command injection because user input is passed directly to shell without validation.
    """
    os.system(f"ping {user_input}")


