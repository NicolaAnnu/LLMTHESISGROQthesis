def export_transactions(user_id):
    """
    Exports user transaction data to a file based solely on user ID, 
    without verifying whether the requesting party has permission to access the data.
    """
    with open(f"{user_id}_transactions.csv", "w") as f:
        f.write("Exported data")
