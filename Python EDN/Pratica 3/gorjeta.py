# Objetivo de calcular a porcentagem do valor de gorjeta
def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return round(gorjeta, 2)

total_conta = 126.00
porcentagem = 10

gorjeta = calcular_gorjeta(total_conta, porcentagem)
print(f"Para uma conta de R${total_conta:.2f}, a gorjeta de {porcentagem}% resulta em R${gorjeta:.2f}")