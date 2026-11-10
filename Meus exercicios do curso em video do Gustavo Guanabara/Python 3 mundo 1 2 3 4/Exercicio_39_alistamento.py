from datetime import date
ano = int(input("Digite o ano que você nasceu: "))
atual = date.today().year
print("Você tem {} anos em 2026.".format(atual - ano))
if atual - ano == 18:
    print("Deve se alistar esse ano!")
elif atual - ano < 18:
    saldo = 18 - (atual - ano)
    print("Ainda falta {} anos para se alistar.".format(saldo))
else:
    saldo = (atual - ano) - 18
    print("Já deveria ter se alistado a {} anos atrás.".format(saldo))