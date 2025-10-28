produto = input("nome do produto: ")
nome_mercado1 = input("nome do mercado: ")
preco1 = float(input("valor do produto: "))

produto = input("nome do produto: ")
nome_mercado2 = input("nome do mercado: ")
preco2 = float(input("valor do produto: "))

produto = input("nome do produto: ")
nome_mercado3 = input("nome do mercado: ")
preco3 = float(input("valor do produto: "))

print("=== Resultado ===")

print("produto", produto)

if preco1<preco2 and preco1<preco3:
    print("nome_mercado", nome_mercado1)
    print("preco", preco1)
elif preco2<preco1 and preco2<preco3:
    print("nome_mercado", nome_mercado2)
    print("preco", preco2)
elif preco3<preco1 and preco3<preco2:
    print("nome_mercado", nome_mercado3)
    print("preco", preco3)
