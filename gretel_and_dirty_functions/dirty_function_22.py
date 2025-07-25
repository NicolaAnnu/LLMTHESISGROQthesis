def update_balance(account_id, amount):
    """
    Modifies the account balance without synchronizing concurrent access, 
    potentially leading to inconsistent updates in multi-threaded scenarios.
    """
    balance = get_balance(account_id)
    balance += amount
    set_balance(account_id, balance)
