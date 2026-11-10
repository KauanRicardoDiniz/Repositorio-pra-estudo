distancia = float(input("Qual a distancia? "))
if distancia <= 200:
    preço = distancia * 0.5
else:
    preço = distancia * 0.45
print("Seu custo de viagem será R${}".format(preço))