#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:A) qual é o total gasto na compra.B) quantos produtos custam mais de R$1000.C) qual é o nome do produto mais barato
sp = 0
pm = 0
c = 0
menorp = 0
while True:
    produto = input("Qual o nome do produto ? ").strip().capitalize()
    preco = float(input("Digite o preço dele: R$ "))
    sp += preco
    c += 1
    if preco > 1000:
        pm += 1
    if c == 1:
        menorp = preco
        menor = produto
    elif preco < menorp:
        menorp = preco
        menor = produto
    continua = input("Quer continuar ? (S/N) ").strip().upper()
    while continua not in ("S", "N"):
        print("Opção inválida. Tente novamente.")
        continua = input("Quer continuar ? (S/N) ").strip().upper()
    if continua == "S":
        continue
    else:
        break
print(f"O total a ser pago é R$ {sp:.2f}. {pm} Produtos custam mais de R$ 1000.00. O produto mais barato é {menor}")