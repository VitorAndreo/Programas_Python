import requests as rq
from pprint import pprint


nome = input("Digite o nome para pesquisa:\n")
url = f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}'
params = {
    "localidade": 33 #RJ
}

response = rq.get(url, params=params)

try:
    response.raise_for_status()

except rq.HTTPError as e:
    print(f"Erro no request: {e}")

else:
    resultado = response.json()
    pprint(resultado[0]["res"])