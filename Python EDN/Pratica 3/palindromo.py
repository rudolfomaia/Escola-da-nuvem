def palindromo(texto):
    texto_limpo = ''.join(char.lower() 
                          for char in texto 
                          if char.isalnum())
    return texto_limpo == texto_limpo[::-1]

frase = input("Digite sua palavra ou frase aqui: ")
resultado = palindromo(frase)

if resultado == True:
    resposta = "Sim"
else:
    resposta = "Não"

print(f"'{frase}' é considerado um palíndromo? {resposta}")
