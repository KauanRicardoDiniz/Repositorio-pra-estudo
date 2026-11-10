km = float(input("Quantos kms você rodou? "))
dias = int(input("Quantos dias voce ficou com carro? "))
print("Voce terá que pagar R${:.2f}".format(60 * dias + 0.15 * km))