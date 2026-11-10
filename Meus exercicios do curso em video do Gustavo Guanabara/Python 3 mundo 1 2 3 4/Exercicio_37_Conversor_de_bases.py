num = int(input("Digite um numero que você quer converter: "))
base = str(input("Qual base de conversão você quer ?\n(1 Binário, 2 Octal, 3 Hexadecimal): "))
if base == "1":
    print("{} convertido para binário fica {}".format(num, bin(num)))
elif base == "2":
    print("{} convertido para octal fica {}".format(num, oct(num)))
elif base == "3":
    print("{} convertido para hexadecimal fica {}".format(num, hex(num)))
else:
    print("Base inválida. Apenas (1, 2 ,3).")