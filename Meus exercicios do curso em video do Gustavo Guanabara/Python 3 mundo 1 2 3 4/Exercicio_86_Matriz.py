# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
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