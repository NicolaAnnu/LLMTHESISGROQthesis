import pandas as pd

class StockPortfolio:
    def __init__(self):
        self.portfolio = pd.DataFrame(columns=['Symbol', 'Quantity', 'Price'])

    def add_stock(self, symbol, quantity, price):
        if symbol in self.portfolio['Symbol'].values:
            self.portfolio.loc[self.portfolio['Symbol'] == symbol, 'Quantity'] += quantity
        else:
            self.portfolio = self.portfolio.append({'Symbol': symbol, 'Quantity': quantity, 'Price': price}, ignore_index=True)

    def remove_stock(self, symbol):
        self.portfolio = self.portfolio[self.portfolio['Symbol'] != symbol]

    def calculate_total_value(self):
        self.portfolio['Total Value'] = self.portfolio['Quantity'] * self.portfolio['Price']
        return self.portfolio['Total Value'].sum()

# Example usage:
portfolio = StockPortfolio()
portfolio.add_stock('AAPL', 10, 150.75)
portfolio.add_stock('GOOGL', 5, 2800.50)
portfolio.remove_stock('AAPL')
print("Total Value of Portfolio:", portfolio.calculate_total_value())