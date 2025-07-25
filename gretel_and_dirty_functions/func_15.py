class TaxClient:
    def __init__(self, client_id, name):
        self.client_id = client_id
        self.name = name
        self.tax_data = {}

    def add_tax_info(self, tax_type, details):
        if tax_type in self.tax_data:
            self.tax_data[tax_type].append(details)
        else:
            self.tax_data[tax_type] = [details]

    def update_tax_info(self, tax_type, old_details, new_details):
        if tax_type in self.tax_data:
            for i, details in enumerate(self.tax_data[tax_type]):
                if details == old_details:
                    self.tax_data[tax_type][i] = new_details
                    break

    def delete_tax_info(self, tax_type, details):
        if tax_type in self.tax_data:
            self.tax_data[tax_type] = [d for d in self.tax_data[tax_type] if d != details]

    def generate_summary_report(self):
        report = f"Tax Report for Client: {self.name}\n"
        for tax_type, details in self.tax_data.items():
            report += f"{tax_type}:\n"
            for detail in details:
                report += f"  - {detail}\n"
        return report

# Example usage:
client = TaxClient(1, "John Doe")
client.add_tax_info("Income Tax", "2021 Income Tax")
client.add_tax_info("Sales Tax", "2021 Sales Tax")
client.update_tax_info("Income Tax", "2021 Income Tax", "2022 Income Tax")
client.delete_tax_info("Sales Tax", "2021 Sales Tax")
print(client.generate_summary_report())