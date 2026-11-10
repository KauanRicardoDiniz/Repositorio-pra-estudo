valor = float(input("Digite o preço: "))
condicao = str(input("Meio de pagamento.(1 à vista, 2 à vista no cartão, 3 duas vezes no cartão, 4 três vezes ou mais no cartão): "))
if condicao == "1":
    print("À Vista tem desconto de 10%, fica por R${:.2f}".format(valor * 0.90))
elif condicao == "2":
    print("À vista no cartão tem desconto de 5%, fica por R${:.2f}".format(valor * 0.95))
elif condicao == "3":
    print("Divido duas vezes no cartão fica em duas de R${:.2f}".format(valor / 2))
elif condicao == "4":
    print("Divido três vezes no cartão tem juros de 20%, fica em três de R${}".format((valor * 1.20) / 3))
else:
    print("Condição invalida, tente novamente. (Obs: De 1 a 4)")