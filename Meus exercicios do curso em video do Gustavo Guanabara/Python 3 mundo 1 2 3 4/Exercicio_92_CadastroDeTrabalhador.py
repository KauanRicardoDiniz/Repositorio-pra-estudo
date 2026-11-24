# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date
trabalhador = dict()
nome = input("Digite seu nome: ")
nasc = int(input("Digite seu ano de nascimento: "))
ctps = int(input("Digite sua carteira de trabalho: "))
idade = date.today().year - nasc
trabalhador["nome"] = nome
trabalhador["idade"] = idade
trabalhador["ctps"] = ctps
if ctps != 0:
    contratacao = int(input("Ano de contratação: "))
    salario = float(input("Salário: "))
    tempo_contribuicao = date.today().year - contratacao
    aposentar = idade + (35 - tempo_contribuicao)
    trabalhador["contratacao"] = contratacao
    trabalhador["salario"] = salario
    trabalhador["aposentadoria"] = aposentar
print(trabalhador)