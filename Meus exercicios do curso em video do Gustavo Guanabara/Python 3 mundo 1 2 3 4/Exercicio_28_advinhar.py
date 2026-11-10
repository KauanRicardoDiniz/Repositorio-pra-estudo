from random import randint
from time import sleep
comp = randint(0, 5) # Faz o computador pensar
print("-=-" * 20)
print("Vou pensar em um numero entre 0 e 5. tente adivinhar...")
print("-=-" * 20)
num = int(input("Digite um numero de 0 a 5: ")) # Jogador tenta adivinhar
print("Processando...")
sleep(2)
if num == comp:
    print("Você advinhou o numero! era {}.".format(comp))
else:
    print("Erroooooou, era {}.".format(comp))