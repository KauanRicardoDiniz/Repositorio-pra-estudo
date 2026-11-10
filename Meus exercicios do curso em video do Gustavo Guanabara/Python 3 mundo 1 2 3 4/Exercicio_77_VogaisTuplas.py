# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
palavras = (
    "casa",
    "computador",
    "python",
    "programacao",
    "teclado",
    "mouse",
    "janela",
    "livro",
    "escola",
    "faculdade"
)
for i in palavras:
    print(f"As vogais de {i} são: ", end="")
    for letra in i:
        if letra in "aeiou":
            print(letra, end=" ")
    print()