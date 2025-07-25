class MobileBankingUser:
    def __init__(self, name, account_balance, account_number):
        self.name = name
        self.account_balance = account_balance
        self.account_number = account_number

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def get_balance(self):
        return self.account_balance

# Example usage:
user = MobileBankingUser("John Doe", 1000.0, 123456789)
print(user.get_balance())  # Output: 1000.0
user.deposit(500.0)
print(user.get_balance())  # Output: 1500.0
user.withdraw(200.0)
print(user.get_balance())  # Output: 1300.0