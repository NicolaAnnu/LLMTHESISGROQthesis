import pandas as pd

class PaymentFraudAnalyzer:
    def __init__(self, transactions_df):
        self.transactions_df = transactions_df
    
    def analyze_fraud(self):
        # Convert transaction time to datetime
        self.transactions_df['transaction_time'] = pd.to_datetime(self.transactions_df['transaction_time'])
        
        # Sort transactions by time
        self.transactions_df.sort_values(by='transaction_time', inplace=True)
        
        # Calculate time difference between consecutive transactions
        self.transactions_df['time_diff'] = self.transactions_df['transaction_time'].diff().dt.total_seconds()
        
        # Calculate average transaction amount per location
        avg_amount_per_location = self.transactions_df.groupby('location')['amount'].mean()
        
        # Add average transaction amount per location as a new column
        self.transactions_df['avg_amount_per_location'] = self.transactions_df['location'].map(avg_amount_per_location)
        
        # Identify transactions with time difference greater than 600 seconds and amount greater than average amount per location
        fraudulent_transactions = self.transactions_df[(self.transactions_df['time_diff'] > 600) & (self.transactions_df['amount'] > self.transactions_df['avg_amount_per_location'])]
        
        return fraudulent_transactions

# Example usage:
# transactions = pd.DataFrame({
#     'transaction_id': [1, 2, 3, 4, 5],
#     'amount': [100, 50, 200, 300, 150],
#     'location': ['A', 'B', 'A', 'C', 'B'],
#     'transaction_time': ['2023-01-01 10:00:00', '2023-01-01 10:01:00', '2023-01-01 10:05:00', '2023-01-01 11:00:00', '2023-01-01 11:01:00']
# })
# analyzer = PaymentFraudAnalyzer(transactions)
# fraudulent_transactions = analyzer.analyze_fraud()
# print(fraudulent_transactions)