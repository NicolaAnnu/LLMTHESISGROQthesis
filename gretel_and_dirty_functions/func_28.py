class LoanApplicationValidator:
    def __init__(self, income_threshold, income_multiple):
        self.income_threshold = income_threshold
        self.income_multiple = income_multiple

    def validate(self, applicant_data):
        income = applicant_data['income']
        loan_amount = applicant_data['loan_amount']

        is_income_valid = (lambda x: x > self.income_threshold)(income)
        is_loan_amount_valid = (lambda x: x % income <= self.income_multiple)(loan_amount)

        return is_income_valid and is_loan_amount_valid