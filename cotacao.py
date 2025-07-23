import requests

def listar_moedas():
    # retorna um dicionário com os códigos e nomes das moedas
    url = "https://api.frankfurter.app/currencies"
    try:
        resposta = requests.get(url) # faz uma requisição HTTP para pegar os dados
        dados = resposta.json()
        return dict(sorted(dados.items())) # extrai os códigos das moedas em ordem alfabética
    except Exception as e: # em caso de erro, vai ocorrer uma lista padrão de 3 moedas
        print(f"Erro ao listar moedas: {e}")
        return {
            "USD": "United States Dollar",
            "BRL": "Brazilian Real",
            "EUR": "Euro"
        }

def converter_moeda(valor, moeda_origem, moeda_destino):
    # Frankfurter não permite conversão para a mesma moeda
    if moeda_origem == moeda_destino:
        return round(valor, 2)

    # monta a URL com os parâmetros passados
    url = f"https://api.frankfurter.app/latest?amount={valor}&from={moeda_origem}&to={moeda_destino}"
    try:
        resposta = requests.get(url)
        dados = resposta.json()
        return round(dados["rates"][moeda_destino], 2)
    except Exception as e:
        print(f"Erro na conversão: {e}")
        return None
        