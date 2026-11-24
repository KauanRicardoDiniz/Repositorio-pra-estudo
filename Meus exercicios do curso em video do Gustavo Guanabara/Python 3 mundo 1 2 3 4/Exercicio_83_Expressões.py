# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
expressao = input("Digite uma expressão: ")
count = 0
for caractere in expressao:
    if caractere == "(":
        count += 1
    elif caractere == ")":
        count -= 1
    if count < 0:
        break
if count == 0:
    print("Expressão válida!")
else:
    print("Expressão inválida!")