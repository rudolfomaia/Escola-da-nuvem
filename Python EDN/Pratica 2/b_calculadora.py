num1 = input("Digite o primeiro Número: ")
num2 = input("Digite o segundo Número: ")

# Verifica se a entrada dos números é válida
if not num1.replace('.', '', 1).isdigit() or not num2.replace('.', '', 1).isdigit():
    print("Erro: Entrada Invalida. Por favor, insira Números válidos.")
    exit()

# Converte os valores de string para float
num1 = float(num1)
num2 = float(num2)

# Solicita a operação
operacao = input("Digite a operação (+, -, *, /): ")

# Realiza a operação escolhida
if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    # Verifica se há tentativa de divisão por zero
    if num2 == 0:
        print("Erro: Divisão por Zero não é permitida")
        exit()
    resultado = num1 / num2
else:
    print("Erro: Operação invalida. Tente Novamente.")
    exit()

# Exibe o resultado
print(f"O resultado de {num1} {operacao} {num2} é: {resultado}")