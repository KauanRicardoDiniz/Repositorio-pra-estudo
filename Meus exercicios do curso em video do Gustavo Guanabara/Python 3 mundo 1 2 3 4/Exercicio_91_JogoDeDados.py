# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
jogadores = {}
for jogador in range(1, 5):
    resultado = randint(1, 6)
    jogadores[f"Jogador {jogador}"] = resultado
jogadores = dict(sorted(jogadores.items(), key=lambda item: item[1], reverse=True))
print(jogadores)