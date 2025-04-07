import pandas as pd

arquivo = r"D:\Filme, Cursos, etc\Python EDN\Pratica 5\treinamento\logs_treinamento.csv"

try:
    # Tentando ler o arquivo CSV
    frame = pd.read_csv(arquivo)

    # Verificando se a coluna 'tempo_execucao' existe
    if 'tempo_execucao' not in frame.columns:
        raise ValueError("A coluna 'tempo_execucao' não foi encontrada no arquivo.")
    
    # Calculando a média e o desvio padrão
    media = frame['tempo_execucao'].mean()
    desvio_padrao = frame['tempo_execucao'].std()
    
    # Exibindo os resultados
    print(f"Média do tempo de execução: {media:.2f} segundos")
    print(f"Desvio padrão do tempo de execução: {desvio_padrao:.2f} segundos")

except FileNotFoundError:
    print(f"Erro: O arquivo '{arquivo}' não foi encontrado.")
except ValueError as e:
    print(f"Erro: {e}")
except pd.errors.EmptyDataError:
    print(f"Erro: O arquivo '{arquivo}' está vazio.")
except pd.errors.ParserError:
    print(f"Erro: O arquivo '{arquivo}' não pode ser processado como CSV.")
except Exception as e:
    print(f"Erro inesperado: {e}")