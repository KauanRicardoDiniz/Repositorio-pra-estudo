# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

# a) Os 5 primeiros times.

# b) Os últimos 4 colocados.

# c) Times em ordem alfabética.

# d) Em que posição está o time da Chapecoense.
times = (
    "Flamengo",
    "Palmeiras",
    "Cruzeiro",
    "Fluminense",
    "Athletico-PR",
    "Bahia",
    "Atlético-MG",
    "Bragantino",
    "Santos",
    "São Paulo",
    "Botafogo",
    "Coritiba",
    "Vasco",
    "Mirassol",
    "Vitória",
    "Internacional",
    "Corinthians",
    "Grêmio",
    "Remo",
    "Chapecoense"
)
print(f"Os 5 primeiros times são {times[0 : 5]}")
print(f"Os ultimos quatros são {times[-4:]}")
print(f"Os times em ordem fica {sorted(times)}")
print(f"A Chapecoense está na posição {times.index('Chapecoense') + 1}")