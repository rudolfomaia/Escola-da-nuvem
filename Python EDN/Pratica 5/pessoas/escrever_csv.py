import csv
import os

# Obtém o diretório do script
diretorio_atual = os.path.dirname(__file__)
arquivo_csv = os.path.join(diretorio_atual, "dados_pessoas.csv")

# Dados a serem acrescentados
novos_dados = [
    ["Maria", "35", "Curitiba"],
    ["Carlos", "40", "Salvador"],
    ["Joao", "29", "Rio de Janeiro"],
    ["Marcela", "23", "Belo Horizonte"],
    ["Kleber", "19", "São Paulo"]
]

# Verificando se o arquivo já existe
arquivo_existe = os.path.exists(arquivo_csv)

# Abrir o arquivo em modo de acréscimo ('a') ou escrita ('w') dependendo da existência
with open(arquivo_csv, mode="a", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    
    # Se o arquivo estiver vazio (não tiver cabeçalho), adiciona o cabeçalho
    if not arquivo_existe:
        escritor.writerow(["Nome", "Idade", "Cidade"])

    escritor.writerows(novos_dados)

print(f"Novos dados foram adicionados ao arquivo '{arquivo_csv}' com sucesso!")
