#code principale
import streamlit as st
import pandas as pd

from source.code.DataReader import DataReader
from source.code.CryptoModel import CryptoModel

###########################################
#recuperer les donnees depuis du lien

URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
API_KEY = 'ded5b890-0e71-41e4-b097-a3e73ec43f99'
data_reader = DataReader(URL, API_KEY)
#recuperer la liste des donnees (liste de CryptoModel) depuis le lien de l'API
liste_data = data_reader.get_data()
                                         
df = pd.DataFrame(CryptoModel.data_array_to_json(liste_data))
st.dataframe(df)
