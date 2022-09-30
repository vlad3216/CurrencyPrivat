from flask import Flask, request
from utils import get_currency_exchange_rate


app = Flask(__name__)


@app.route("/rates", methods=['GET'])
def get_rates():
    date = request.args.get('date', default='01.12.2018')
    base_currency = request.args.get('baseCurrency', default='UAH')
    currency = request.args.get('currency', default='USD')
    bank = request.args.get('bank', default='NB')
    result = get_currency_exchange_rate(date, base_currency, currency, bank)
    return result













