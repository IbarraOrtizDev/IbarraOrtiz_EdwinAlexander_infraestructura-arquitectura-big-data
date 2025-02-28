import requests
from dotenv import load_dotenv
import os

load_dotenv()
class FetchData:
    def __init__(self):
        self.url = os.getenv('API_URL')

    def fetch(self):
        response = requests.get(self.url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()