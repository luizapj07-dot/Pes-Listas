Jogada1 = input("O que irás jogar?")
Jogada2 = input("O que irás jogar?")

if Jogada1 == "pedra" and Jogada2 == "papel":
    print("Jogador 2 ganhou")
elif Jogada1 == "pedra" and Jogada2 == "tesoura":
    print("Jogador 1 ganhou")
elif Jogada1 == "pedra" and Jogada2 == "pedra":
    print("Empate!")
elif Jogada1 == "papel" and Jogada2 == "tesoura":
    print("Jogador 2 ganhou")
elif Jogada1 == "papel" and Jogada2 == "papel":
    print("Empate!")
elif Jogada1 == "tesoura" and Jogada2 == "tesoura":
    print("Empate!")
elif Jogada2 == "pedra" and Jogada1 == "papel":
    print("Jogador 1 ganhou")
elif Jogada2 == "pedra" and Jogada1 == "tesoura":
    print("Jogador 2 ganhou")
elif Jogada2 == "pedra" and Jogada1 == "pedra":
    print("Empate!")
elif Jogada2 == "papel" and Jogada1 == "tesoura":
    print("Jogador 1 ganhou")
elif Jogada2 == "papel" and Jogada1 == "papel":
    print("Empate!")
else:
    print("Empate!")