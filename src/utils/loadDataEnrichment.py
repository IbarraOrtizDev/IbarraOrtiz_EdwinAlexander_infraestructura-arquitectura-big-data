import pandas as pd
import glob
from dotenv import load_dotenv
import os

load_dotenv()

def loadProductInformation():
    # Load the product information
    product_info = pd.read_json('src/fuentesAdicionales/product.json')
    return product_info

def loadCustomerInformation():
    # Load the customer information
    customer_info = pd.read_excel('src/fuentesAdicionales/customer_information.xlsx')
    return customer_info

# Load data cleaning
def loadDataCleaning():
    files = glob.glob('src/static/xlsx/ingestion*.csv')
    guid = os.getenv('UUID')
    print(f"Files found: {files}")
    print(f"Files Guid: {guid}")
    # Leer y concatenar todos los archivos encontrados
    df_list = [pd.read_csv(file) for file in files]
    
    # Unir todos los DataFrames en uno solo
    df = pd.concat(df_list, ignore_index=True)
    
    return df