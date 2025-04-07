# Esse código tem como objetivo ler valores inteiros inputados pelo usuário e calcular a diferença entre eles.

# Lendo os quatro valores inteiros do usuário
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))
D = int(input("Digite o valor de D: "))

# Calculando a diferença conforme a fórmula
DIFERENCA = (A * B) - (C * D)

# Exibindo o resultado
print(f"A fórmula para a diferença é: (A * B) - (C * D)")
print(f"Substituindo os valores fornecidos: ({A} * {B}) - ({C} * {D})")
print(f"O resultado da diferença é: DIFERENCA = {DIFERENCA}")