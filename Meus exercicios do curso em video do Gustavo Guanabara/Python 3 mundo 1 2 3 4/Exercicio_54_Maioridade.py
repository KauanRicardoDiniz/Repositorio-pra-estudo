from datetime import date
ano = date.today().year
count = 0
count2 = 0
for i in range(1, 8):
    nasc = int(input(f"Ano de nascimento da {i}º pessoa: "))
    if ano - nasc >= 18:
        count += 1
    else:
        count2 += 1
print(f"{count} Já atingiram a maioridade, {count2} ainda não atingiu a maioriade.")