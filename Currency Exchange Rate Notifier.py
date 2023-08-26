import requests
import time

def get_exchange_rate(base, target):
    url = f"https://api.exchangeratesapi.io/latest?base={base}&symbols={target}"
    response = requests.get(url)
    data = response.json()
    return data["rates"][target]

base_currency = input("Enter base currency code (e.g., USD): ").upper()
target_currency = input("Enter target currency code (e.g., EUR): ").upper()
target_rate = float(input("Enter target exchange rate: "))

while True:
    exchange_rate = get_exchange_rate(base_currency, target_currency)
    print(f"Current {base_currency} to {target_currency} exchange rate: {exchange_rate:.2f}")
    
    if exchange_rate >= target_rate:
        print(f"Exchange rate reached {target_rate}! Sending notification.")
        break
    
    time.sleep(3600)  # Check every hour
