class InvestmentOption:
    def __init__(self, investment_type, amount, expected_return_rate):
        self.investment_type = investment_type  # String
        self.amount = amount  # Float
        self.expected_return_rate = expected_return_rate  # Float

    def display_info(self):
        print(f"Investment Type: {self.investment_type}")
        print(f"Amount: ${self.amount}")
        print(f"Expected Return Rate: {self.expected_return_rate}%")

# Example usage
option1 = InvestmentOption("Stocks", 1500.00, 5.2)
option1.display_info()