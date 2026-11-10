# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
nums = ()
for r in range(1, 6):
    num = randint(0, 99)
    nums += (num,)
print(nums)
print(f"O menor numero da lista é {min(nums)}, o maior é {max(nums)}")