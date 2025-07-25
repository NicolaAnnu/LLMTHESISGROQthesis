# Define the income and tax rate
income = float(input("Enter your income: "))
tax_rate = 0.2  # Assuming a flat tax rate of 20%

# Calculate the tax
tax = income * tax_rate

# Print the calculated tax
print(f"The calculated tax is: ${tax:.2f}")