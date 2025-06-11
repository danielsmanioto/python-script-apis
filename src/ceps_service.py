import requests

ceps = [
    "01001000",  # Praça da Sé - SP
    "30140071",  # Praça Sete - BH
    "30130170",  # Savassi - BH
    "13470170"   # Rua Tunisia
]

def consultar_cep(cep: str):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        if "erro" in data:
            print(f"CEP {cep} não encontrado.")
        else:
            print(f"\nCEP {cep}:")
            print(f"  Logradouro: {data.get('logradouro')}")
            print(f"  Bairro: {data.get('bairro')}")
            print(f"  Cidade: {data.get('localidade')}")
            print(f"  UF: {data.get('uf')}")
    except requests.RequestException as e:
        print(f"Erro ao consultar o CEP {cep}: {e}")

for cep in ceps:
    consultar_cep(cep)
