mulheres = 0
nomevelho = ""
somaidade = 0
mediaidade = 0
idadevelho = -1

for p in range(1, 5):
    print(f"----- {p}º Pessoa -----")
    nome = input("Digite seu nome: ").capitalize().strip()
    idade = int(input("Digite sua idade: "))
    sexo = input("Digite seu Sexo (H ou M): ").upper().strip()
    somaidade += idade

    if sexo == "M" and idade < 20:
        mulheres += 1
    if sexo == "H" and idade > idadevelho:
        idadevelho = idade
        nomevelho = nome

mediaidade = somaidade / 4

print(f"A media da idade do grupo é {mediaidade}")
print(f"O homem mais velho é {nomevelho}, com {idadevelho} anos.")
print(f"Há {mulheres} mulheres com menos de 20 anos.")