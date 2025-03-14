import requests
from dotenv import load_dotenv
import os
import zipfile
import pandas as pd

load_dotenv()
class FetchData:
    def __init__(self):
        self.url_user = os.getenv('API_URL_USUARIOS')
        self.url = os.getenv('API_URL')


    def fetch(self):
        response = requests.get(self.url_user)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    
    # Nos parecio interesante agregar un metodo para descargar un archivo zip directamente desde www.kaggle.com y así poder descargar un archivo zip con un dataset de prueba y funcionaria como una API
    def fetch_zip(self):
        r = requests.get(self.url)
        r.raise_for_status()
        with open('./src/static/ventas.zip', 'wb') as f:
            f.write(r.content)
        with zipfile.ZipFile('./src/static/ventas.zip', 'r') as zip_ref:
            zip_ref.extractall('./src/static/ventas')
        return pd.read_csv('./src/static/ventas/Base de datos de Ventas.csv')