# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
lista_normal = []
lista_par = []
lista_impar = []
while True:
    num = int(input("Digite um número: "))
    lista_normal.append(num)
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)
    continua = input("Quer continuar? (S/N) ").strip().upper()
    while continua not in ("S", "N"):
        print("Opção inválida!")
        continua = input("Quer continuar? (S/N) ").strip().upper()
    if continua == "S":
        continue
    else:
        break
print(f"A lista normal é {lista_normal}\nA lista par é {lista_par}\nA lista impar é {lista_impar}")