import requests as rq

# url = "https://httpbin.org/get"
url = "https://httpbin.org/post"

data = {
    "pessoa":{
        "nome": "Rodrigo",
        "profissao": "professor"
    }
}

params = {
    "dataIni": "2025-01-01",
    "dataFim": "2025-12-31"
}

# response = rq.get(url)
response = rq.post(url, json=data, params=params)
print(response.request.url)
print(response.text)