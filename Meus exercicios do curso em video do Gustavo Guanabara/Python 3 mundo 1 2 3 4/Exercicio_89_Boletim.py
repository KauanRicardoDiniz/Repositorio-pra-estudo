# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
boletim = []
while True:
    nome = input("Digite seu nome: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media = (nota1 + nota2) / 2
    boletim.append([nome, nota1, nota2, media])
    continua = input("Quer continuar? (S/N) ").strip().upper()
    while continua not in ("S", "N"):
        print("Opção inválida!")
        continua = input("Quer continuar? (S/N) ").strip().upper()
    if continua == "S":
        continue
    else:
        break
for i, aluno in enumerate(boletim, 1):
    print(f"{i} - {aluno[0]} | Média: {aluno[3]:.1f}")
while True:
    escolha = int(input("Mostrar notas de qual aluno? (0 para sair): "))
    if escolha == 0:
        break
    if 1 <= escolha <= len(boletim):
        aluno = boletim[escolha - 1]
        print(f"Notas de {aluno[0]}: {aluno[1]} e {aluno[2]}")
    else:
        print("Número de aluno inválido!")