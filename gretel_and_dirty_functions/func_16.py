class FraudDetector:
    def __init__(self, high_amount_threshold=1000, max_daily_transactions=100):
        self.high_amount_threshold = high_amount_threshold
        self.max_daily_transactions = max_daily_transactions

    def identify_fraudulent_transactions(self, transactions):
        fraudulent_transactions = []
        daily_transaction_count = {}

        for transaction in transactions:
            transaction_id = transaction['id']
            amount = transaction['amount']
            date = transaction['date']

            # Check for high amount transactions
            if amount > self.high_amount_threshold:
                fraudulent_transactions.append(transaction_id)
                continue

            # Check for unusual daily transaction volume
            if date not in daily_transaction_count:
                daily_transaction_count[date] = 1
            else:
                daily_transaction_count[date] += 1

            if daily_transaction_count[date] > self.max_daily_transactions:
                fraudulent_transactions.append(transaction_id)

        return fraudulent_transactions