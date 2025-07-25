# Define a list of loan applications with their credit scores
loan_applications = [
    {"name": "Alice", "credit_score": 750},
    {"name": "Bob", "credit_score": 650},
    {"name": "Charlie", "credit_score": 800},
    {"name": "David", "credit_score": 500}
]

# Define the minimum credit score required for approval
min_credit_score = 700

# Iterate through each loan application
for application in loan_applications:
    name = application["name"]
    credit_score = application["credit_score"]
    
    # Check if the credit score meets the minimum requirement
    if credit_score >= min_credit_score:
        decision = "Approved"
    else:
        decision = "Declined"
    
    # Print the decision for each application
    print(f"Loan application for {name}: {decision}")