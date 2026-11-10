salario = float(input("Digite seu salario: R$"))
if salario > 1250:
    aumento = salario * 1.10
else:
    aumento = salario * 1.15
print("Com aumento seu salario fica R${:.2f}".format(aumento))