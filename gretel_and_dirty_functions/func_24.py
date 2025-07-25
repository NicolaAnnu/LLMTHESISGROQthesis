import re

# Define the lambda function to process payment requests
process_payment = lambda amount, customer_details: (
    "Payment processed" if 
    isinstance(amount, (int, float)) and 
    amount > 0 and 
    re.match(r'^[A-Za-z0-9\s]+$', customer_details) 
    else "Invalid transaction"
)

# Example usage
print(process_payment(100.0, "John Doe"))  # Output: Payment processed
print(process_payment(-50.0, "John Doe"))  # Output: Invalid transaction
print(process_payment(100.0, "John Doe!"))  # Output: Invalid transaction