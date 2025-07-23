import requests

def listar_moedas():
    url = "https://api.frankfurter.app/currencies"
    try:
        response = requests.get(url)
        dados = response.json()
        return sorted(list(dados.keys()))
    except Exception as e:
        print("❌ Erro ao listar moedas:", e)
        return ["USD", "BRL", "EUR"]

def converter_moeda(valor, moeda_origem, moeda_destino):
    # Frankfurter não permite conversão para a mesma moeda
    if moeda_origem == moeda_destino:
        return round(valor, 2)

    url = f"https://api.frankfurter.app/latest?amount={valor}&from={moeda_origem}&to={moeda_destino}"
    try:
        response = requests.get(url)
        dados = response.json()
        return round(dados["rates"][moeda_destino], 2)
    except Exception as e:
        print("❌ Erro na conversão:", e)
        return None
        