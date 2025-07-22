import requests
import json
from dotenv import load_dotenv
import os

def basic_format(language,country):
    load_dotenv() 

    API = os.getenv("API_KEY")

    language_code = language
    country_code = country   

    url = f"https://gnews.io/api/v4/top-headlines?category=general&lang={language_code}&country={country_code}&max=10&apikey={API}"

    req = requests.get(url).json()

    with open("txt_files/NEWS.txt","w") as f:
        json.dump(req,f)