import requests
from typing import Dict, Any

class BankAPIHandler:
    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    def authenticate(self) -> bool:
        try:
            response = requests.get(f"{self.base_url}/auth", headers=self.headers)
            response.raise_for_status()
            return True
        except requests.RequestException as e:
            print(f"Authentication failed: {e}")
            return False

    def get_account_balance(self, account_id: str) -> Dict[str, Any]:
        if not self.authenticate():
            return None

        try:
            response = requests.get(f"{self.base_url}/accounts/{account_id}", headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Failed to retrieve account balance: {e}")
            return None

    def format_balance_data(self, account_data: Dict[str, Any]) -> Dict[str, Any]:
        if not account_data:
            return None

        formatted_data = {
            'account_id': account_data.get('id'),
            'balance': account_data.get('balance', {}).get('amount'),
            'currency': account_data.get('balance', {}).get('currency')
        }
        return formatted_data

# Example usage:
# api_handler = BankAPIHandler(api_key='your_api_key', base_url='https://api.examplebank.com')
# balance_data = api_handler.get_account_balance('123456789')
# formatted_balance = api_handler.format_balance_data(balance_data)
# print(formatted_balance)