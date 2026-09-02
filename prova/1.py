nome = str(input("Digite o nome do usuário: "))
senha = int(input("Digite a senha do usuário: "))

if nome == "admin" and senha == 12345:
    print("Login bem sucedido!!")
else:
    print("Nome de usuário ou senha incorretos!!")
