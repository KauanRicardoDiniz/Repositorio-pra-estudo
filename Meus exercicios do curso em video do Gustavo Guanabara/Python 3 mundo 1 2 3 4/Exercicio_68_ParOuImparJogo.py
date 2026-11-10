from random import randint
print("Vamos jogar par ou impar")
c = 0
while True:
    nj = int(input("Digite um numero: "))
    pouij = input("Par ou impar ? (P/I) ").strip().upper()
    if pouij not in ("P", "I"):
        print("Caractere inválido! tente novamente.")
        continue
    comp = randint(0, 999)
    s = nj + comp
    if s % 2 == 0:
        poui = "Par"
    else:
        poui = "Impar"
    print(f"Voce jogou {nj} e o computador jogou {comp}, o total de {s} é {poui}")
    if pouij == "P" and poui == "Par":
        print("Você ganhou essa rodada")
        c += 1
    elif pouij == "I" and poui == "Impar":
        print("Você ganhou essa rodada")
        c += 1
    else:
        break
print(f"Game over! você venceu {c} vezes")