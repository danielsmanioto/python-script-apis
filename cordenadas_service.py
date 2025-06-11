import requests

def buscar_coordenadas(endereco):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": endereco,
        "format": "json",
        "limit": 1
    }
    headers = {"User-Agent": "clima-python-app"}
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    dados = response.json()
    if not dados:
        raise ValueError("Endereço não encontrado.")
    return float(dados[0]["lat"]), float(dados[0]["lon"])

def buscar_previsao(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,wind_speed_10m",
        "timezone": "auto"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    dados = response.json()
    current = dados.get("current", {})
    return current.get("temperature_2m"), current.get("wind_speed_10m")

# --- Uso ---
endereco = input("Digite o endereço (ex: Rua das Rosas, Americana, SP): ")

try:
    lat, lon = buscar_coordenadas(endereco)
    temperatura, vento = buscar_previsao(lat, lon)
    print(f"\n📍 Local: {endereco}")
    print(f"📌 Coordenadas: {lat:.4f}, {lon:.4f}")
    print(f"🌡️ Temperatura: {temperatura} °C")
    print(f"🌬️ Vento: {vento} km/h")
except Exception as e:
    print("Erro:", e)
