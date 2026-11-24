# Faça um programa que leia nome e peso de várias pessoas,                                      guardando tudo em uma lista. No final, mostre:                                                                                                    A) Quantas pessoas foram cadastradas.                                                                                                                B) Uma listagem com as pessoas mais pesadas.                                                                                                    C) Uma listagem com as pessoas mais leves.
galera = []
dado = []
pesados = []
leves = []
c = 0
while True:
    dado.append(input("Nome: "))
    dado.append(float(input("Peso: ")))
    galera.append(dado[:])
    dado.clear()
    c += 1
    continua = input("Quer continuar? (S/N) ").strip().upper()
    while continua not in ("S", "N"):
        print("Opção inválida!")
        continua = input("Quer continuar? (S/N) ").strip().upper()
    if continua == "S":
        continue
    else:
        break
maior = max(pessoa[1] for pessoa in galera)
menor = min(pessoa[1] for pessoa in galera)
for p in galera:
    if p[1] == maior:
        pesados.append(p)
    if p[1] == menor:
        leves.append(p)
print(f"{c} pessoas foram cadastradas\nAs pessoas mais pesadas são {pesados}\nAs mais leves são {leves}")