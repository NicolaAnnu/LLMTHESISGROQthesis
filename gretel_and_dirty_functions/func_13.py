from django.http import JsonResponse
from django.views import View
import requests

class MortgageOffersView(View):
    def get(self, request):
        credit_score = request.GET.get('credit_score')
        desired_interest_rate = request.GET.get('desired_interest_rate')

        if not credit_score or not desired_interest_rate:
            return JsonResponse({'error': 'Credit score and desired interest rate are required'}, status=400)

        # Fetch real-time interest rate data from a financial API
        api_url = "https://api.financeprovider.com/interest_rates"
        response = requests.get(api_url)
        if response.status_code != 200:
            return JsonResponse({'error': 'Failed to fetch interest rate data'}, status=500)

        interest_rate_data = response.json()

        # Filter offers based on credit score and desired interest rate
        offers = []
        for offer in interest_rate_data['offers']:
            if offer['credit_score'] <= int(credit_score) and offer['interest_rate'] <= float(desired_interest_rate):
                offers.append(offer)

        return JsonResponse({'offers': offers})