import json
import os

# Obtém o diretório do script
diretorio_atual = os.path.dirname(__file__)
arquivo_json = os.path.join(diretorio_atual, "dados_pessoais.json")

# Dados a serem armazenados
dados = [
    {"Nome": "Maria", "Idade": 35, "Cidade": "Curitiba"},
    {"Nome": "Carlos", "Idade": 40, "Cidade": "Salvador"},
    {"Nome": "João", "Idade": 29, "Cidade": "Rio de Janeiro"},
    {"Nome": "Marcela", "Idade": 23, "Cidade": "Belo Horizonte"},
    {"Nome": "Kleber", "Idade": 19, "Cidade": "São Paulo"}
]

# Verifica se o arquivo já existe
arquivo_existe = os.path.exists(arquivo_json)

# Escrita no arquivo JSON
with open(arquivo_json, "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, indent=4, ensure_ascii=False)

print(f"Novos dados foram adicionados ao arquivo '{arquivo_json}' com sucesso!")

# Leitura do arquivo JSON
try:
    with open(arquivo_json, "r", encoding="utf-8") as arquivo:
        dados_lidos = json.load(arquivo)  # Carrega os dados do JSON

        for pessoa in dados_lidos:
            print(f"""
                  Nome: {pessoa['Nome']}, Idade: {pessoa['Idade']}, Cidade: {pessoa['Cidade']}
""")

except FileNotFoundError:
    print(f"Erro: O arquivo '{arquivo_json}' não foi encontrado.")
except json.JSONDecodeError:
    print(f"Erro: O arquivo '{arquivo_json}' está corrompido ou não é um JSON válido.")
except Exception as e:
    print(f"Erro inesperado: {e}")
