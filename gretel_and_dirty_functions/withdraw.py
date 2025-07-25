# 5. Race Condition (CWE-362)
import threading
balance = 100
def withdraw(amount):
    """
    Withdraws amount from shared balance if sufficient.
    Vulnerable to race condition because check and debit are not atomic.
    """
    global balance
    if balance >= amount:
        balance -= amount  # Non-atomic operation, race condition possible
