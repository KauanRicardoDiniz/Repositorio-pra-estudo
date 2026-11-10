from datetime import date
ano = int(input("Ano de nascimento: "))
atual = date.today().year
idade = atual - ano
print("Você tem {} anos!".format(idade))
if idade <= 9:
    print("Está na Categoria Mirim.")
elif idade > 9 and idade <= 14:
    print("Está na Categoria Infantil.")
elif idade > 14 and idade <= 19:
    print("Está na Categoria Junior.")
elif idade > 19 and idade <= 25:
    print("Está na Categoria Senior.")
else:
    print("Está na Categoria Master.") 