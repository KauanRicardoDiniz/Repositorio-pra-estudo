parada = 0
s = 0
count = 0
while True:
    parada = int(input("Digite qualquer numero: "))
    if parada == 999:
        break
    s += parada
    count += 1
print(f"Você digitou {count} valores, a soma deles é {s}")