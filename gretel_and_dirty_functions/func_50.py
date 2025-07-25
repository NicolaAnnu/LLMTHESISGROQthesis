import pandas as pd
import os

class TaxClientManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_data()

    def load_data(self):
        if not os.path.exists(self.file_path):
            return pd.DataFrame(columns=['ClientID', 'Name', 'Address', 'Phone', 'Email'])
        return pd.read_csv(self.file_path)

    def update_client(self, client_id, name=None, address=None, phone=None, email=None):
        if client_id not in self.data['ClientID'].values:
            raise ValueError("Client ID not found")
        
        row_index = self.data[self.data['ClientID'] == client_id].index[0]
        
        if name is not None:
            self.data.at[row_index, 'Name'] = name
        if address is not None:
            self.data.at[row_index, 'Address'] = address
        if phone is not None:
            self.data.at[row_index, 'Phone'] = phone
        if email is not None:
            self.data.at[row_index, 'Email'] = email

    def export_data(self, output_path=None):
        if output_path is None:
            output_path = self.file_path
        self.data.to_csv(output_path, index=False)

# Example usage:
# manager = TaxClientManager('clients.csv')
# manager.update_client('C001', name='John Doe', email='john.doe@example.com')
# manager.export_data('updated_clients.csv')