usuario = input("Digite seu usuário:")
senha = input("Digite sua senha:")
if usuario == "admin":
    if senha == "12345":
         print("Login bem sucedido")
    else:
        print("Senha Incorreta")
else:
    print("Nome de usuário e senha incorretos")
