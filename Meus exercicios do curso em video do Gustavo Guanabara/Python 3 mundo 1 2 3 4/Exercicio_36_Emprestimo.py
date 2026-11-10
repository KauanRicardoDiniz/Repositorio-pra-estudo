casa = float(input("Qual o valor da casa ? R$"))
salario = float(input("Qual o seu salário? R$"))
anos = int(input("Em quantos anos você quer pagar? "))
prestação = casa / (anos * 12)
if salario * 1.30 < prestação:
    print("Emprestimo negado!")
else:
    print("Emprestimo aprovado! Cada prestação fica R${:.2f} de {} vezes.".format(prestação, anos * 12))