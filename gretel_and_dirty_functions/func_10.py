class Loan:
    def __init__(self, loan_amount, annual_interest_rate, loan_duration_years):
        self.loan_amount = loan_amount
        self.annual_interest_rate = annual_interest_rate
        self.loan_duration_years = loan_duration_years

    def calculate_monthly_repayment(self):
        monthly_interest_rate = self.annual_interest_rate / 12 / 100
        number_of_payments = self.loan_duration_years * 12
        monthly_repayment = (self.loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -number_of_payments)
        return monthly_repayment

# Example usage:
# loan = Loan(200000, 4.5, 30)
# print(loan.calculate_monthly_repayment())