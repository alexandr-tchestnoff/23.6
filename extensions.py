import requests
import json
from config import keys

# добавление классов для оптимизации и уменьшения кода
class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str ):
        # если конвертируют одинаковые валюты
        # quote, base, amount = values
        if quote == base:
            raise ConvertionException(f'Нельзя конвертировать одинаковые валюты {base}!')
        ############################################################################

        # если ввели не корректную валюту
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}!')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}!')
        ############################################################################

        #   если ввели не корректное количество валюты
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}!')
        ############################################################################
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]] * amount


        return total_base

############################################################################