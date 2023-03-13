import requests

api_key = 'zMU0tKVgzUwzmsU1KbU1JZr6JdRwucJc'
base_currency = 'USD'
target_currency = 'EUR'

url = f'https://api.exchangeratesapi.io/latest?base={base_currency}&symbols={target_currency}&access_key={api_key}'

response = requests.get(url)
print(response.json())
# if response.ok:
#     data = response.json()
#     rate = data['rates'][target_currency]
#     print(f'The {target_currency} rate is {rate} {base_currency}')
# else:
#     print('Could not get rate from API using default rate...')
#     rate = 0.85
#     print(f'The {target_currency} rate is {rate} {base_currency} (default)')