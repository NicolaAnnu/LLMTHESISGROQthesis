class Investment:
    def __init__(self, name, purchase_price, quantity):
        self.name = name
        self.purchase_price = purchase_price
        self.quantity = quantity

class Portfolio:
    def __init__(self, name, total_investment):
        self.name = name
        self.total_investment = total_investment
        self.investments = []

    def add_investment(self, investment):
        self.investments.append(investment)
        self.total_investment += investment.purchase_price * investment.quantity

    def get_total_investment(self):
        return self.total_investment

    def get_investment_list(self):
        return self.investments