import datetime

class Transaction:
    def __init__(self, transaction_id, amount, timestamp, merchant_info):
        self.transaction_id = transaction_id
        self.amount = amount
        self.timestamp = timestamp
        self.merchant_info = merchant_info
        self.status = 'Pending'

    def update_status(self, new_status):
        self.status = new_status

class MerchantTransactionManager:
    def __init__(self):
        self.transactions = {}

    def add_transaction(self, transaction):
        self.transactions[transaction.transaction_id] = transaction

    def get_transactions_by_date_range(self, start_date, end_date):
        return [transaction for transaction in self.transactions.values() if start_date <= transaction.timestamp <= end_date]

    def get_transactions_by_merchant(self, merchant_id):
        return [transaction for transaction in self.transactions.values() if transaction.merchant_info['merchant_id'] == merchant_id]

# Example usage
mt_manager = MerchantTransactionManager()

# Adding transactions
mt_manager.add_transaction(Transaction('12345', 100.0, datetime.datetime(2023, 10, 1, 12, 0, 0), {'merchant_id': 'M123', 'name': 'Merchant A'}))
mt_manager.add_transaction(Transaction('67890', 200.0, datetime.datetime(2023, 10, 2, 13, 0, 0), {'merchant_id': 'M456', 'name': 'Merchant B'}))

# Updating transaction status
mt_manager.transactions['12345'].update_status('Completed')

# Retrieving transactions
print([t.transaction_id for t in mt_manager.get_transactions_by_date_range(datetime.datetime(2023, 10, 1, 0, 0, 0), datetime.datetime(2023, 10, 2, 23, 59, 59))])
print([t.transaction_id for t in mt_manager.get_transactions_by_merchant('M123')])