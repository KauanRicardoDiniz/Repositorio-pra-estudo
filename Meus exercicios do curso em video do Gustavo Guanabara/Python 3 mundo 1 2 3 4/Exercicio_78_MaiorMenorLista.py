# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
lista = []
for c in range(1,6):
    lista.append(int(input(f"Digite o {c}º número: ")))
print(f"O menor valor foi {min(lista)} na posição {lista.index(min(lista))}, e o maior foi {max(lista)} na posição {lista.index(max(lista))}")