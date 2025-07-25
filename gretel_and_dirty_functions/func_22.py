import re

class LoanPreApprovalValidator:
    def validate_application_data(self, application_data):
        # Define the regex patterns for validation
        ssn_pattern = r'^\d{3}-\d{2}-\d{4}$'
        income_pattern = r'^\d+(\.\d{1,2})?$'
        employment_status_pattern = r'^(full-time|part-time|self-employed|unemployed)$'

        # Validate social_security_number
        if not re.match(ssn_pattern, application_data['social_security_number']):
            return False

        # Validate income
        if not re.match(income_pattern, application_data['income']):
            return False

        # Validate employment_status
        if not re.match(employment_status_pattern, application_data['employment_status']):
            return False

        return True