class CryptoModel:
        def __init__(self) :
                #declarrer les attributs de l'objet dont on aura besoin  
                
                self.price = 0
                self.name = ''
                self.symbol = ''
                self.slug = ''
                self.cmc_rank = 0
                self.num_market_pairs = 0
                
                             
                pass
        def load(self, data):
                #charger les donnees dans l'objet
                #data est un dictionnaire et les cles sont les noms des attributs
                # pour traduis ls donnees de cette objet en format json on utilise la fonction dumps de json sur l'objet en question
                
                #pour traduire les donne
                for key, value in data.items():
                        self.charge(key, value)
        
        #utiliser la recursivité pour charger les donnees de l'objet
        def charge(self,key , value):
                #verifier si c est un dict
                if isinstance(value, dict):
                        self.load(value)
                else:
                        #verifier si l'attribut existe
                        if hasattr(self, key):
                                setattr(self,key,value)
        
        
        
        
        
                """
                 {
            "id": 1,
            "name": "Bitcoin",
            "symbol": "BTC",
            "slug": "bitcoin",
            "cmc_rank": 5,
            "num_market_pairs": 500,
            "circulating_supply": 16950100,
            "total_supply": 16950100,
            "max_supply": 21000000,
            "infinite_supply": false,
            "last_updated": "2018-06-02T22:51:28.209Z",
            "date_added": "2013-04-28T00:00:00.000Z",
            "tags": [
                "mineable"
            ],
            "platform": null,
            "self_reported_circulating_supply": null,
            "self_reported_market_cap": null,
            "quote": {
                "USD": {
                    "price": 9283.92,
                    "volume_24h": 7155680000,
                    "volume_change_24h": -0.152774,
                    "percent_change_1h": -0.152774,
                    "percent_change_24h": 0.518894,
                    "percent_change_7d": 0.986573,
                    "market_cap": 852164659250.2758,
                    "market_cap_dominance": 51,
                    "fully_diluted_market_cap": 952835089431.14,
                    "last_updated": "2018-08-09T22:53:32.000Z"
                },
                "BTC": {
                    "price": 1,
                    "volume_24h": 772012,
                    "volume_change_24h": 0,
                    "percent_change_1h": 0,
                    "percent_change_24h": 0,
                    "percent_change_7d": 0,
                    "market_cap": 17024600,
                    "market_cap_dominance": 12,
                    "fully_diluted_market_cap": 952835089431.14,
                    "last_updated": "2018-08-09T22:53:32.000Z"
                }
            }
        },
                """
        