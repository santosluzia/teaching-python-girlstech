# Exercício 4 — Listas e dicionários
# Crie um dicionário representando um produto (nome, preço, quantidade em estoque). 
# Escreva um programa que calcula o valor total em estoque (preço * quantidade)
# e exibe o resultado formatado.

produto = {"nome": "Macbook", "preco": 7100, "quantidade": 70}

print(f'Valor total em estoque {produto["preco"] *  produto["quantidade"]} de {produto["nome"]}')

