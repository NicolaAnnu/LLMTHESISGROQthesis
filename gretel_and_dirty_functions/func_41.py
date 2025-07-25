import re

class PaymentGatewayValidator:
    def validate_transaction_id(self, transaction_id):
        pattern = r'^PG[a-zA-Z0-9]{10}-\d{3}$'
        if re.match(pattern, transaction_id):
            return True
        else:
            return False