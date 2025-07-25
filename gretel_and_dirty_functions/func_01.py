# Import necessary libraries
import pandas as pd

# Sample data: List of banks with their respective risk weights and capital requirements
data = {
    'Bank Name': ['Bank A', 'Bank B', 'Bank C', 'Bank D'],
    'Risk Weight': [0.05, 0.10, 0.15, 0.20],
    'Capital Requirement': [100, 200, 300, 400]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Initialize total capital requirement
total_capital_requirement = 0

# Loop through each bank to calculate the total capital requirement
for index, row in df.iterrows():
    total_capital_requirement += row['Risk Weight'] * row['Capital Requirement']

# Print the total capital requirement
print(f"The total capital requirement is: {total_capital_requirement}")