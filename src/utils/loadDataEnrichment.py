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
    # Unir todos los DataFrames en uno solo
    df = pd.read_csv(os.getenv('CLEANED_FILE_PATH'))
    
    return df