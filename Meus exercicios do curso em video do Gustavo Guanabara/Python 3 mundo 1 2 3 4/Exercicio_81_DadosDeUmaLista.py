# Crie um programa que vai ler vários números e colocar em uma lista.                  Depois disso, mostre:                                                                                                                                                A) Quantos números foram digitados.                                                                                                                    B) A lista de valores, ordenada de forma decrescente.                                                                                          C) Se o valor 5 foi digitado e está ou não na lista.
lista = []
c = 0
while True:
    num = int(input("Digite um número: "))
    c += 1
    lista.append(num)
    continua = input("Quer continuar? (S/N) ").strip().upper()
    while continua not in ("S", "N"):
        print("Opção inválida!")
        continua = input("Quer continuar? (S/N) ").strip().upper()
    if continua == "S":
        continue
    else:
        break
if 5 not in lista:
    print("O número 5 não foi digitado.")
else:
    print("O número 5 foi digitado.")
print(f"{c} números foram digitados.")
print(sorted(lista, reverse=True))