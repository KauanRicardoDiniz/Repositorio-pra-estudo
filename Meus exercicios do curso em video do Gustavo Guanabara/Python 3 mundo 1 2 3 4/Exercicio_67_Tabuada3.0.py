while True:
    num = int(input("Qual valor você quer ver a tabuada ? "))
    if num < 0:
        break
    for c in range(1, 11):
        print(f"{num} x {c} = {num * c}")
print("Programa encerrado! Tenha um ótimo dia!")