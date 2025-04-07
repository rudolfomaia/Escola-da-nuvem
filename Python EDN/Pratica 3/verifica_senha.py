def verifica_senha():
    while True:
        senha = input("Digite uma senha com pelo menos 8 caracteres e ao menos um número! (ou 'sair' para encerrar): ")
        
        # Da a opção ao usuário que quer sair
        if senha.lower() == 'sair':
            print("Programa encerrado.")
            break
        
        # Verifica o tamanho da senha
        if len(senha) < 8:
            print("Senha fraca: deve ter pelo menos 8 caracteres.")
            continue
        
        # Verifica se a senha contém pelo menos um número
        if not any(caractere.isdigit() for caractere in senha):
            print("Senha fraca: deve conter pelo menos um número.")
            continue
        
        # Senha valida
        print("Senha forte e válida!")
        break

verifica_senha()