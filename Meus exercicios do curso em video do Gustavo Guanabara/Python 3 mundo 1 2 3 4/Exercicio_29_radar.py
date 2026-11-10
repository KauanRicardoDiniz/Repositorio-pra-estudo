vel = int(input("Qual foi a velocidade registrada? "))
if vel > 80:
    print("Você foi multado!")
    multa = (vel - 80) * 7
    print("A sua multa é de R${:.2f}".format(multa))
else:
    print("Está dentro da velocidade permitida!")
print("Tenha um bom dia, dirija com segurança!")