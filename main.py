# Witajcie w moim pierwszym projekcie w Pythonie!

import requests

# URL API do pobrania listy stacji pomiarowych
url_stacje = 'http://api.gios.gov.pl/pjp-api/rest/station/findAll'

# Wykonanie zapytania do API i przypisanie odpowiedzi do zmiennej
response_stacje = requests.get(url_stacje)

# Sprawdzenie, czy zapytanie się powiodło
if response_stacje.status_code == 200:
    lista_stacji = response_stacje.json()
    print(lista_stacji)
else:
    print("Błąd podczas pobierania danych stacji")
