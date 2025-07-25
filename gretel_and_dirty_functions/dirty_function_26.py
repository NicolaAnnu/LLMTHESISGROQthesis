def auto_approve_loan(user_score):
    """
    Automatically approves a loan request based solely on the user's credit
    score, without evaluating additional eligibility criteria. This can result
    in unauthorized approvals and bypass of business rules or fraud checks.
    """
    if user_score > 600:
        return "Approved"
    return "Rejected"
