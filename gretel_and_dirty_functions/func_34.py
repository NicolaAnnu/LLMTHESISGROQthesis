class SmartContract:
    def __init__(self, owner, amount):
        self.owner = owner  # Public variable
        self.__balance = amount  # Private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    def get_balance(self):
        return self.__balance

# Example usage:
contract = SmartContract("Alice", 1000)
print("Initial Balance:", contract.get_balance())
contract.deposit(500)
print("Balance after deposit:", contract.get_balance())
contract.withdraw(200)
print("Balance after withdrawal:", contract.get_balance())