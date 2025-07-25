class FraudDetectionRule:
    def __init__(self, transaction_amount, is_high_risk_customer):
        self.transaction_amount = transaction_amount
        self.is_high_risk_customer = is_high_risk_customer
        self.is_fraudulent = self.detect_fraud()

    def detect_fraud(self):
        if self.transaction_amount > 10000 and self.is_high_risk_customer:
            return True
        return False

# Example usage
transaction = FraudDetectionRule(12000, True)
print(transaction.is_fraudulent)  # Output: True