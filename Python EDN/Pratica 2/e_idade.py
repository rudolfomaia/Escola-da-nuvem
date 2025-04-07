# Identifica e classifica o usuário com base em sua idade inputada.

# Input de idade
idade = int(input("Digite sua idade: "))

# Condições que definem a resposta com base em if o elif
if idade >= 18:
    print("Você é adulto!🧑")
elif idade >= 12:
    print("Você é adolescente!🧒")
else:
    print("Você é criança!👶")