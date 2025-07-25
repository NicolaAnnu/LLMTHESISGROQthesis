class FundTransfer:
    def __init__(self, transfer_id, from_account, to_account, amount, transfer_date):
        self.transfer_id = transfer_id
        self.from_account = from_account
        self.to_account = to_account
        self.amount = amount
        self.transfer_date = transfer_date
        self.confirmed = False

    def validate_transfer(self):
        # Add validation logic here
        # For example, check if the amount is positive, if accounts exist, etc.
        if self.amount > 0:
            return True
        else:
            return False

    def confirm_transfer(self):
        if self.validate_transfer():
            self.confirmed = True
            print(f"Transfer {self.transfer_id} confirmed.")
        else:
            print(f"Transfer {self.transfer_id} validation failed.")

# Example usage
transfer = FundTransfer("12345", "123456789", "987654321", 100.0, "2023-04-01")
transfer.confirm_transfer()