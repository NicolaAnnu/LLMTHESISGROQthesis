import pandas as pd

class TaxReportingProcessor:
    def __init__(self, data):
        self.data = data

    def clean_data(self):
        # Remove any rows with missing values
        self.data = self.data.dropna()
        # Convert all column names to lowercase
        self.data.columns = self.data.columns.str.lower()
        # Ensure all numeric columns are of the correct type
        for column in self.data.select_dtypes(include=['number']).columns:
            self.data[column] = pd.to_numeric(self.data[column], errors='coerce')

    def transform_data(self):
        # Standardize column names
        self.data.columns = self.data.columns.str.replace(' ', '_').str.replace('-', '_')
        # Convert dates to a uniform format
        if 'date' in self.data.columns:
            self.data['date'] = pd.to_datetime(self.data['date'], errors='coerce')

    def generate_summary_report(self, category):
        if category not in self.data.columns:
            raise ValueError(f"Category '{category}' not found in the data.")
        summary_report = self.data.groupby(category).sum().reset_index()
        return summary_report

# Example usage:
# data = pd.read_csv('tax_data.csv')
# processor = TaxReportingProcessor(data)
# processor.clean_data()
# processor.transform_data()
# summary = processor.generate_summary_report('tax_type')
# print(summary)