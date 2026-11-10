s = 0
c = 0
for i in range(1, 7):
    num = int(input("Digite o {}º numero: ".format(i)))
    if num % 2 == 0:
        s += num
        c += 1
    else:
        print("Esse numero impar será desconsiderado.")
print("Você informou {} numeros pares, a soma é {}".format(c, s))