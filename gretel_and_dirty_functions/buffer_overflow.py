# 3. Buffer Overflow (CWE-120) - simulated in Python
def buffer_overflow():
    """
    Demonstrates a buffer overflow vulnerability.

    Vulnerability Details:
    The function allocates a buffer of fixed size (5 bytes) 
    but attempts to write data beyond its allocated boundaries (10 bytes).
    This unsafe memory operation can lead to memory corruption, unexpected crashes,
    or potentially allow arbitrary code execution by an attacker.
    """
    buf = bytearray(5)
    for i in range(10):
        buf[i] = 0x41
