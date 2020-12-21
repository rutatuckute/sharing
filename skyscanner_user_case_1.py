import requests, json
import pandas as pd
import time
import datetime
from pandas.io.json import json_normalize

current_time = time.time()
daily_time = datetime.datetime.fromtimestamp(current_time).strftime('%Y%m%d_%H%M%S')

url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/FR/EUR/en-US/PARI-sky/VILN-sky/2020-12-20/2020-12-27"

headers = {
    'x-rapidapi-key': "your_API_key",
    'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)
take_me_home = response.json()
quotes = json_normalize(take_me_home['Quotes'])

file_path = "C:\\Users\\ruttuc\\Desktop\\take_me_home\\"
file_save = "/generated_quotes_" + daily_time + ".xlsx"

quotes.to_excel(file_path+file_save)



