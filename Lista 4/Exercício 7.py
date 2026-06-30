notas = []
opcao = 5
indices = []
cont = 0
while opcao != 0:
    print("""Notas
            -----
            1 - Cadastrar
            2 - Excluir
            3 - Listar
            4 - Calcular média
            5 – Mostrar maior nota
            6 – Mostrar menor nota
            0 - Sair
            Opção:""")
    
    opcao = int(input("Digite uma opcao: "))
    
    if opcao == 1:
        nota = int(input("Digite a nota: "))
        notas.append(nota)
        indices.append(cont)
        cont += 1

    if opcao == 2:
        i = 0
        while i < len(notas):
            print(f"Nota -> {notas[i]} indice -> {indices[i]}")
            i+=1 

        excluir = int(input("Digite o indice a ser excluido: "))
        notas.pop(excluir)
        indices.pop(excluir)
        print("Nota excluída com sucesso!!")
        
    if opcao == 3:
        if len(notas) == 0:
            print("A lista está vazia!!")
        else:
            for nota in notas:
                print(nota)
    
    if opcao == 4:
        soma = 0
        for nota in notas:
            soma = soma + nota
        media = soma/(len(notas))
        print(media)
        if media < 6:
            print("Reprovado")
        else:
            print("Aprovado")
    
    if opcao == 5:
        maior = 0
        if len(notas) == 0:
            print("Sem notas cadastradas!!")
        else:
            for nota in notas:
                if nota > maior:
                    maior = nota
            print(maior)

    if opcao == 6:
        menor = 11
        if len(notas) == 0:
            print("Sem notas cadastradas!!")
        else:
            for nota in notas:
                if nota < menor:
                    menor = nota
            print(menor)
   
    if opcao == 0:
        break
     


            
