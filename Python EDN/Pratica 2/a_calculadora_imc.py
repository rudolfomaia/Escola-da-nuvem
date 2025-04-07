# O objetivo desse código é uma calculadora de Índice de Massa Corporal (IMC)

# Input de peso e altura do usuário
peso = float(input("Digite seu peso (KG): "))
altura = float(input("Digite sua altura (M): "))

# Fórmula de cáculo do IMC
imc = peso / (altura ** 2)

# Retorno de acordo com o cálculo dos dados fornecidos
if imc < 18.5:
    print("Você está abaixo do peso! ⚠️🥗")
elif imc < 25:
    print("Você está no peso ideal! ✅💪")
elif imc < 30:
    print("Você está com sobrepeso! ⚠️🍔")
else:
    print("Você está obeso! ❗")
    print("Confira algumas boas práticas para combater a obesidade: https://ge.globo.com/eu-atleta/nutricao/noticia/nutricionista-destaca-10-habitos-que-ajudam-na-luta-contra-o-sobrepeso.ghtml")