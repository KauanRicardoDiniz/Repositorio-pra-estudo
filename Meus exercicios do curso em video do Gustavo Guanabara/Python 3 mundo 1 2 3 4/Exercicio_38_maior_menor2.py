n1 = int(input("Digite um numero: \033[32m"))
print("\033[0m", end="")

n2 = int(input("Digite outro: \033[32m"))
print("\033[0m", end="")

if n1 > n2:
    print("{} é o maior numero.".format(n1))
elif n2 > n1:
    print("{} é o maior numero.".format(n2))
else:
    print("Não existe valor maior, os dois são iguais.")