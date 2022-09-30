import requests
from urllib import parse

def get_currency_exchange_rate(date: str,
                               base_currency: str,
                               currency: str,
                               bank: str):
    url = 'https://api.privatbank.ua/p24api/exchange_rates?json&'

    queryString = {'date': date}
    query = parse.urlencode(queryString)

    response = requests.get(url + query)
    json = response.json()

    if response.status_code == 200:
        date = json.get('date')
        exchange_rate = json.get('exchangeRate')
        for i in range(len(exchange_rate)):
            if exchange_rate[i].get('baseCurrency') == base_currency and exchange_rate[i].get('currency') == currency:
                if bank == 'NB':
                    rate_NB = exchange_rate[i]['saleRateNB']
                    return f'NBU currency {date} in convertation {base_currency} in {currency} - {rate_NB}'
                elif bank == 'PB':
                    try:
                        sales_rate = exchange_rate[i]['saleRate']
                        purchase_rate = exchange_rate[i]['purchaseRate']
                        return f'PrivatBank currency on {date} in convertation {base_currency} - {currency} for buying {purchase_rate} for sale {sales_rate}'
                    except:
                        return f'PrivatBank currency on {date} in convertation {base_currency} - {currency} not found!!!'
        return f'Not found: exchange rate {base_currency} to {currency}'
    else:
        return f"Api error {response.status_code}: {json.get('errorDescription')}"



