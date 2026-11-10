from math import hypot
catoposto = float(input("Digite o comprimento do cateto oposto: "))
catadjacente = float(input("Digite o comprimento do cateto adjacente: "))
print("O comprimento da hipotenusa é: {:.2f} ".format(hypot(catoposto, catadjacente)))