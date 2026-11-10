Nota1 = float(input("Digite a primeira nota: "))
Nota2 = float(input("Digite a segunda nota: "))
media = (Nota1 + Nota2) / 2
print("A média entre {} e {} é igual a {:.1f}".format(Nota1, Nota2, media))
if media >= 7.0:
    print("Você passou por media!")
elif media <= 6.9 and media >= 5.0:
    print("Você ta na recuperação!")
else:
    print("Você reprovou!")