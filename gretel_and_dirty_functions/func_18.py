import numpy as np

class InvestmentPortfolio:
    def __init__(self, assets, weights):
        self.assets = assets
        self.weights = weights
        self.portfolio_value = 1.0

    def update_asset_values(self, new_values):
        self.assets = [a * v for a, v in zip(self.assets, new_values)]

    def rebalance_portfolio(self):
        current_weights = np.array(self.assets) / sum(self.assets)
        target_weights = np.array(self.weights)
        rebalance_factors = target_weights / current_weights
        self.update_asset_values(rebalance_factors)

# Example usage
portfolio = InvestmentPortfolio([100, 200, 300], [0.4, 0.3, 0.3])
portfolio.update_asset_values([102, 205, 295])
portfolio.rebalance_portfolio()
print(portfolio.assets)