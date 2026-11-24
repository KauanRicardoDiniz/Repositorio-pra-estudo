# Aprimore o desafio anterior, mostrando no final:                                                    A) A soma de todos os valores pares digitados.                                                                                                  B) A soma dos valores da terceira coluna.                                                                                                                C) O maior valor da segunda linha.
# Declara a matriz 3x3 (inicialmente com zeros)
matriz = [[0 for _ in range(3)] for _ in range(3)]

# Preenche a matriz com valores lidos pelo teclado
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f"Digite o valor para [{i}][{j}]: "))

# Mostra a matriz formatada
print("\nMatriz 3x3:")
for i in range(3):
    for j in range(3):
        print(f"[{matriz[i][j]:^5}]", end=" ")
    print()

# A) Soma de todos os valores pares
soma_pares = 0
for i in range(3):
    for j in range(3):
        if matriz[i][j] % 2 == 0:
            soma_pares += matriz[i][j]

# B) Soma dos valores da terceira coluna (índice 2)
soma_coluna3 = 0
for i in range(3):
    soma_coluna3 += matriz[i][2]

# C) Maior valor da segunda linha (índice 1)
maior_linha2 = matriz[1][0]
for j in range(1, 3):
    if matriz[1][j] > maior_linha2:
        maior_linha2 = matriz[1][j]

# Resultados
print(f"\nA) Soma dos valores pares: {soma_pares}")
print(f"B) Soma da terceira coluna: {soma_coluna3}")
print(f"C) Maior valor da segunda linha: {maior_linha2}")