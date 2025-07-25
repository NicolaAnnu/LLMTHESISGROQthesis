class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def display_account_details(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ${self.balance:.2f}")

# Example usage:
# account = BankAccount("John Doe", "123456789", 1000.00)
# account.display_account_details()