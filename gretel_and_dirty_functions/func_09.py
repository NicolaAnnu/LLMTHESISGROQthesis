class BankAccount:
    def __init__(self, account_number: int, account_holder_name: str, balance: float = 0.0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount: float):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self) -> float:
        return self.balance

    def __str__(self):
        return f"Account Number: {self.account_number}, Account Holder: {self.account_holder_name}, Balance: {self.balance}"