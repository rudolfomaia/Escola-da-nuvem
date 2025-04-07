import requests

def obter_cotacao(moeda):
    try:
        url = f'https://brapi.dev/api/v2/currency?currency={moeda}'
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()  # Levanta um erro se a resposta for inválida
        return resposta.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao obter a cotação: {e}")
        return None

def exibir_cotacao(cotacao):
    try:
        dados = cotacao["currency"][0]

        print(f"\nCotação {dados['name']} ({dados['currency']}/{dados['pair']}):")
        print(f"Valor atual: R$ {dados['bid']}")
        print(f"Máximo do dia: R$ {dados['high']}")
        print(f"Mínimo do dia: R$ {dados['low']}")
        print(f"Data e hora da última atualização: {dados['updatedAt']}\n")

    except (KeyError, IndexError):
        print("Moeda não encontrada ou erro na resposta da API.")

def main():
    while True:
        try:
            moeda = input("Digite o código da moeda desejada (ex: USD, EUR, FKP) ou 'sair' para encerrar: ").upper()
            if moeda == 'SAIR':
                print("Encerrando o programa...")
                break
            if not moeda.isalpha():
                raise ValueError("Código inválido. Digite apenas letras.")

            cotacao = obter_cotacao(moeda)
            if cotacao and "currency" in cotacao and cotacao["currency"]:
                exibir_cotacao(cotacao)
            else:
                print("Não foi possível obter a cotação. Verifique se o código da moeda está correto.")

        except ValueError as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    main()
