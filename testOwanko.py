import requests
import pandas as pd

# ID stanowiska pomiarowego
sensor_id = 2
index = 52

# URL API do pobrania danych z konkretnego stanowiska pomiarowego
# url_dane = f'http://api.gios.gov.pl/pjp-api/rest/data/getData/{sensor_id}'
url_dane = f'https://api.gios.gov.pl/pjp-api/rest/aqindex/getIndex/{index}'

# url_dane = 'https://api.gios.gov.pl/pjp-api/v1/rest/archivalData/getDataBySensor/711?dateFrom=2022-02-23%2015%3A00&dateTo=2023-02-24%2015%3A00&page=0&size=20'

# Wykonanie zapytania do API
response_dane = requests.get(url_dane)

# Sprawdzenie, czy zapytanie się powiodło
if response_dane.status_code == 200:
    dane_pomiarowe = response_dane.json()
    mojDataFrame = pd.json_normalize(dane_pomiarowe)
    print(mojDataFrame.columns)
    print(mojDataFrame.head(3))
else:
    print("Błąd podczas pobierania danych pomiarowych")
