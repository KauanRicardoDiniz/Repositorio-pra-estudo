# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import sample
jogos = []
quantidade = int(input("Quantos jogos serão gerados ?"))
for j in range(quantidade):
    jogo = sample(range(1, 61),6)
    jogos.append(jogo)
for i, jogo in enumerate(jogos, 1):
    print(f"Jogo {i}: {jogo}")