class CustomerInfo:
    def __init__(self, first_name, last_name, date_of_birth, national_id):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.national_id = national_id

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_customer_details(self):
        return f"First Name: {self.first_name}, Last Name: {self.last_name}, Date of Birth: {self.date_of_birth}, National ID: {self.national_id}"