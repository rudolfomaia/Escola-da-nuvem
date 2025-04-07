import csv

# Nome do arquivo CSV
arquivo_csv = r"D:\Filme, Cursos, etc\Python EDN\Pratica 5\ler_pessoas\dados_pessoas.csv"

try:
    # Abrindo o arquivo CSV para leitura
    with open(arquivo_csv, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        # Lendo e imprimindo os dados
        for linha in leitor:
            print(", ".join(linha))  # Exibe os dados separados por vírgula

except FileNotFoundError:
    print(f"Erro: O arquivo '{arquivo_csv}' não foi encontrado.")
except Exception as e:
    print(f"Erro inesperado: {e}")
