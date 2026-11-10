# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.

# B) Em que posição foi digitado o primeiro valor 3.

# C) Quais foram os números pares.
nums = ()
count = 0
pares = ()
for i in range(1, 5):
    num = int(input(f"Digite o {i}º Numero: "))
    nums += (num,)
    if num == 9:
        count += 1
print(f"O 9 apareceu {count} vezes.")
if 3 in nums:
    print(f"O Numero 3 foi digitado primeiro na posição {nums.index(3) + 1}")
else:
    print("Nenhum numero 3 foi digitado.")
for numero in nums:
    if numero % 2 == 0:
        pares += (numero,)
print(f"Os numeros pares foram {pares}")