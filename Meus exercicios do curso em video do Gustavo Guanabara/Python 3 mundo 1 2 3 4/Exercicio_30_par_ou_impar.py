numero = int(input("Digite um numero: "))
if numero % 2 == 0: #Resto da divisão vai definir se é par ou impar
    print("{:.0f} é par".format(numero))
else:
    print("{:.0f} é impar".format(numero))