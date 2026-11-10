from time import sleep
programa = False
while not programa:
    s = 0
    m = 1
    for i in range(1, 3):
        num = int(input(f"Digite o {i}º numero: "))
        s += num
        m *= num
        if i == 1:
            maior = num
        elif num > maior:
            maior = num
    op = 0
    while op != 4:
        sleep(1)
        opcao = int(input("Qual opção voce deseja ?\n[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa\n: "))   
        if opcao == 1:
            print(f"A soma dos números é {s}")
        elif opcao == 2:
            print(f"A multiplicação dos números é {m}")
        elif opcao == 3:
            print(f"O maior numero é {maior}")
        elif opcao == 4:
            print("Digites os valores novamente.")
            op = 4
        elif opcao == 5:
            print("Finalizando...")
            sleep(2)
            print("Fim do programa!")
            programa = True
            op = 4
        else:
            print("Opção inválida. Tente Novamente.")
