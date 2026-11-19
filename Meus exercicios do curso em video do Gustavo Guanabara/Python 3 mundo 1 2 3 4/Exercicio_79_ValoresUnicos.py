# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
lista = []
while True:
    num = int(input("Digite um número: "))
    if num not in lista:
        lista.append(num)
    continua = input("Quer continuar? (S/N) ").strip().upper()
    while continua not in ("S", "N"):
        print("Opção inválida!")
        continua = input("Quer continuar? (S/N) ").strip().upper()
    if continua == "S":
        continue
    else:
        break
print(sorted(lista))