from random import randint
itens = ("PEDRA", "PAPEL", "TESOURA")
comp = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
pepate = int(input("Qual você escolhe ?: "))
print("-=-" * 11)
print("Computador jogou {}".format(itens[comp]))
print("Você jogou {}".format(itens[pepate]))
print("-=-" * 11)
if comp == 0: # Computador jogou PEDRA
    if pepate == 0:
        print("Empate!")
    elif pepate == 1:
        print("Você ganhou!")
    else:
        print("Você perdeu!")
if comp == 1: # Computador jogou PAPEL
    if pepate == 0:
        print("Você perdeu!")
    elif pepate == 1:
        print("Empate!")
    else:
        print("Você ganhou!")
if comp == 2: # Computador jogou TESOURA
    if pepate == 0:
        print("Você ganhou!")
    elif pepate == 1:
        print("Você perdeu!")
    else:
        print("Empatou!")