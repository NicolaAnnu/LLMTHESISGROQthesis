import pandas as pd
from datetime import datetime

class ATMTransactionProcessor:
    def __init__(self):
        self.transactions = pd.DataFrame(columns=['TransactionID', 'AccountNumber', 'TransactionType', 'Amount', 'Timestamp'])
    
    def deposit(self, account_number, amount):
        transaction_id = self._generate_transaction_id()
        timestamp = datetime.now()
        self.transactions = self.transactions.append({
            'TransactionID': transaction_id,
            'AccountNumber': account_number,
            'TransactionType': 'Deposit',
            'Amount': amount,
            'Timestamp': timestamp
        }, ignore_index=True)
        return transaction_id
    
    def withdraw(self, account_number, amount):
        if self._check_balance(account_number, amount):
            transaction_id = self._generate_transaction_id()
            timestamp = datetime.now()
            self.transactions = self.transactions.append({
                'TransactionID': transaction_id,
                'AccountNumber': account_number,
                'TransactionType': 'Withdrawal',
                'Amount': amount,
                'Timestamp': timestamp
            }, ignore_index=True)
            return transaction_id
        else:
            return None
    
    def check_balance(self, account_number):
        balance = self.transactions[self.transactions['AccountNumber'] == account_number]['Amount'].sum()
        return balance
    
    def _generate_transaction_id(self):
        return str(datetime.now()).replace(':', '').replace(' ', '_')
    
    def _check_balance(self, account_number, amount):
        balance = self.transactions[self.transactions['AccountNumber'] == account_number]['Amount'].sum()
        return balance >= amount