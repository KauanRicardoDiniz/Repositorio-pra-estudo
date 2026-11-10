parada = 0
s = 0
count = 0
while parada != 999:
    parada = int(input("Digite qualquer numero: "))
    s += parada
    count += 1
s -= 999
count -= 1
print(f"Você digitou {count} valores, a soma deles é {s}")