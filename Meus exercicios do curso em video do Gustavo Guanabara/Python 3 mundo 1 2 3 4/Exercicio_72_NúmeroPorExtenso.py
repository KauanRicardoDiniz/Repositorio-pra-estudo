# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
nums = "Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Quatorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte"
while True:
    num = int(input("Digite um numero de 0 a 20: "))
    if num < 0 or num > 20:
        print("Numero inválido. Tente novamente")
        continue
    else:
        print(f"Você escolheu {nums[num]}.")
        break