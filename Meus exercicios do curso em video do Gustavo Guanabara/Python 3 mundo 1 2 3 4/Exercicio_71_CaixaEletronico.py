#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
valor = int(input("Qual o valor será sacado ? R$ "))
print(f"será entregue {valor // 50} cedulas de R$ 50")
valor %= 50
print(f"{valor // 20} Cedulas de R$ 20")
valor %= 20
print(f"{valor // 10} Cédulas de R$ 10")
valor %= 10
print(f"{valor // 1} Cédulas de R$ 1")