# Identifica e classifica o usuário com base em sua idade inputada.

# Input de idade
idade = int(input("Digite sua idade: "))

# Condições que definem a resposta com base em if, elif e else
if idade  <= 12:
    print("Você é criança!👶")
elif idade <=17:
    print("Você é adolescente!🧒")
elif idade <= 59:
    print("Você é adulto!🧑")
elif idade >= 60:
    print("Você é idoso!👴")