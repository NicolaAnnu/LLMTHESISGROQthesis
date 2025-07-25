import re

class UnderwritingValidator:
    def __init__(self, min_policy_amount, max_policy_amount):
        self.min_policy_amount = min_policy_amount
        self.max_policy_amount = max_policy_amount

    def validate_email(self, email):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email) is not None

    def validate_date(self, date_str):
        date_regex = r'^\d{4}-\d{2}-\d{2}$'
        return re.match(date_regex, date_str) is not None

    def validate_policy_amount(self, policy_amount):
        try:
            amount = float(policy_amount)
            return self.min_policy_amount <= amount <= self.max_policy_amount
        except ValueError:
            return False

    def validate_risk_assessment(self, risk_score, thresholds):
        if isinstance(thresholds, dict):
            for level, threshold in thresholds.items():
                if risk_score >= threshold:
                    return level
        return None