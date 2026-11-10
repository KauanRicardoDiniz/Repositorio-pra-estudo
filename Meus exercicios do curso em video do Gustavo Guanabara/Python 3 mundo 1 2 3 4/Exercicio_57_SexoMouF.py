sexo = input("Qual o seu sexo? (M/F) ").strip().upper()

while sexo != "M" and sexo != "F":
    print("Sexo inválido! Digite novamente.")
    sexo = input("Qual o seu sexo? (M/F) ").strip().upper()
if sexo == "M" or sexo == "F":
    print("Sexo registrado com sucesso.")
