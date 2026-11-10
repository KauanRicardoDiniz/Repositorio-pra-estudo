pesos = []

for i in range(1, 6):
    peso = float(input("Digite o seu peso em Kg: "))
    pesos.append(peso)

maior = max(pesos)
menor = min(pesos)

print(f"O maior peso foi {maior}Kg e o menor foi {menor}Kg")