# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
produtos = (
    ("Arroz", 25.90),
    ("Feijão", 8.50),
    ("Macarrão", 4.99),
    ("Leite", 5.49),
    ("Açúcar", 4.50),
    ("Café", 18.90),
    ("Óleo", 7.99),
    ("Farinha", 6.50),
    ("Manteiga", 12.90),
    ("Pão", 9.00)
)
print("LISTAGEM DE PREÇOS\n------------------------------\nPRODUTO                 PREÇO")
for produto, preco in produtos:
    print(f"{produto:<23} R$ {preco:.2f}")