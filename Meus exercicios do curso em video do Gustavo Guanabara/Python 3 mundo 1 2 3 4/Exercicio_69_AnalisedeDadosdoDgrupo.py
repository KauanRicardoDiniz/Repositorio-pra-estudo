count18 = 0
countf = 0
countm = 0
while True:
    idade = int(input("Qual a sua idade ? "))
    sexo = input("Qual o seu sexo ? (M/F) ").strip().upper()
    while sexo not in ("M", "F"):
        print("Sexo inválido. Tente novamente.")
        sexo = input("Qual o seu sexo ? (M/F) ").strip().upper()
    if idade > 18:
        count18 += 1
    if sexo == "M":
        countm += 1
    if sexo == "F" and idade < 20:
        countf += 1
    continua = input("Você quer registrar mais alguem ? (S/N) ").strip().upper()
    while continua not in ("S", "N"):
        print("Caractere inválido. Tente novamente.")
        continua = input("Você quer registrar mais alguem ? (S/N) ").strip().upper()
    if continua == "S":
        continue
    else:
        break
print(f"{count18} Pessoa/s tem mais de 18 anos. {countm} Homem/s foi cadastrado/s. {countf} Mulher/es foi cadastrada/s")