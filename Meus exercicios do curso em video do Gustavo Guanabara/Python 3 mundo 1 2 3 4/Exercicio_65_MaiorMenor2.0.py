programa = False
s = 0
c = 0
while not programa:
    num = int(input("Digite um número: "))
    s += num
    c += 1
    if c == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    sequencia = input("Quer continuar ? (S/N) ").strip().upper()
    while sequencia not in ("S", "N"):
        print("Resposta inválida! Digite S ou N.")
        sequencia = input("Quer continuar? (S/N) ").strip().upper()
    if sequencia == "N":
        programa = True
media = s / c
print(f"A média dos valores é {media}, o menor valor foi {menor} o maior foi {maior}")