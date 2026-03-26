import requests as rq
from pprint import pprint



url = 'https://servicodados.ibge.gov.br/api/v1/localidades/municipios'
params = {
    "view": "nivelado"
}

response = rq.get(url, params=params)

try:
    response.raise_for_status()

except rq.HTTPError as e:
    print(f"Erro no request: {e}")

else:
    resultado = response.json()
    pprint(resultado)