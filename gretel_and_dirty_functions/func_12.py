class PaymentOrchestrator:
    def __init__(self, payment_method, amount):
        self.payment_method = payment_method
        self.amount = amount

    def process_payment(self):
        print(f"Processing payment of {self.amount} using {self.payment_method}")

# Example usage:
payment = PaymentOrchestrator('credit_card', 100.50)
payment.process_payment()