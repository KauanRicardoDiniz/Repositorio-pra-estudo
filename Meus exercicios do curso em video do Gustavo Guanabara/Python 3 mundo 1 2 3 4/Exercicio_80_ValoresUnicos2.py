# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
lista = []
for i in range(0, 5):
    num = int(input("Digite um número: "))
    for e in range(len(lista)):
        if num < lista[e]:
            lista.insert(e, num)
            break
    else:
        lista.append(num)
print(f"Lista em ordem crescente: {lista}")