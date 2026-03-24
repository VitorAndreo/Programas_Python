import requests as rq

url = "https://www.google.com.br"
response = rq.get(url)
print(response)
print(response.text)

with open("F:/Python/n8n/API/01-request/page.html", 'w') as page:
    page.write(response.text)