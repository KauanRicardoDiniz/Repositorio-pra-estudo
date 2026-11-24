# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
aluno = dict()
nome = input("Digite seu nome: ")
media = float(input("Digite sua média: "))
aluno["nome"] = nome
aluno["media"] = media
if media >= 7:
    aluno["situacao"] = "Aprovado"
elif media >= 5:
    aluno["situacao"] = "Recuperação"
else:
    aluno["situacao"] = "Reprovado"
print(aluno)