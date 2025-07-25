class SimplePricingEngine:
    def __init__(self, stock_price, strike_price):
        self.stock_price = stock_price
        self.strike_price = strike_price
    
    def calculate_intrinsic_value(self):
        intrinsic_value = max(0, self.stock_price - self.strike_price)
        return intrinsic_value