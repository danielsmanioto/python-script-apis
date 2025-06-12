import requests

url = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL"
response = requests.get(url)
data = response.json()

for moeda, info in data.items():
    print(f"Moeda: {info['name']}")
    print(f"  Código: {info['code']}/{info['codein']}")
    print(f"  Valor de compra (bid): {info['bid']}")
    print(f"  Valor de venda (ask): {info['ask']}")
    print(f"  Data: {info['create_date']}")
    print("-" * 40)