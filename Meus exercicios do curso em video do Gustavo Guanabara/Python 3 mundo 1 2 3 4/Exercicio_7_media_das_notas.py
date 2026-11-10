Nota1 = float(input("Digite a primeira nota: "))
Nota2 = float(input("Digite a segunda nota: "))
media = (Nota1 + Nota2) / 2
print(f"A média entre {Nota1} e {Nota2} é igual a {media:.1f}")
if media >= 7.0:
    print("Você passou por media!")
else:
    print("Você reprovou!")