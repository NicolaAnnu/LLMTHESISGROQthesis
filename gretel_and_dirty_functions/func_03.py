# Import necessary library
import pandas as pd

# Create an empty DataFrame to store client information
crm_system = pd.DataFrame(columns=['Client Name', 'Tax ID'])

# Loop to add at least 5 clients to the system
for i in range(5):
    client_name = input(f"Enter client {i+1} name: ")
    tax_id = input(f"Enter client {i+1} tax ID: ")
    crm_system = crm_system.append({'Client Name': client_name, 'Tax ID': tax_id}, ignore_index=True)

# Print each client's information
print(crm_system)