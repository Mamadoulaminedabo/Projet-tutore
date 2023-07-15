#recuperer les donnees depuis un lien


from model.CryptoModel import CryptoModel 
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


class DataReader :
        def __init__(self):
                self._url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
                self._API_KEY = 'ded5b890-0e71-41e4-b097-a3e73ec43f99'
                self.parameters = {
                        'start': '1',
                        'limit': '5',
                        'convert': 'USD'
                }
                self.headers = {
                        'Accepts': 'application/json',
                        'X-CMC_PRO_API_KEY': self._API_KEY
                }
                
        def get_data(self):
                
                session = Session()
                session.headers.update(self.headers)
                listeCrypto = []
                try:
                        response = session.get(self._url, params=self.parameters)
                        data = json.loads(response.text)
                        for crypto_json in data['data']:
                                crypto = CryptoModel()
                                crypto.load(crypto_json)
                                
                                listeCrypto.append(crypto)
                except Exception as e:
                        return listeCrypto
                
                
                return listeCrypto

