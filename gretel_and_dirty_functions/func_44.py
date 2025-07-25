class CryptocurrencyTransaction:
    def __init__(self, amount, sender_address, recipient_address):
        self.amount = amount
        self.sender_address = sender_address
        self.recipient_address = recipient_address

    def display_transaction(self):
        return f"Transaction Details: Amount = {self.amount}, Sender = {self.sender_address}, Recipient = {self.recipient_address}"