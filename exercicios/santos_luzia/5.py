# Exercício 5 — Funções (integrador)
# Escreva uma função analisar_notas(notas) que recebe uma lista de números 
# e retorna um dicionário com as notas pares, as notas ímpares e a média. 
# Teste a função com uma lista de pelo menos 5 notas.

def analisar_notas(notas):
    pares = [i for i in notas if i%2==0 ]
    impares = [i for i in notas if i%2!=0]
    media = sum(notas) / len(notas)
    return {"pares": pares, "impares": impares, "media": media}
    
resultado = analisar_notas([8, 7, 9, 6, 10])
print(resultado)

# Por que usar funções?
# 🔄 Reutilizar código — não precisa repetir.
# 🧹 Organizar o código — cada função pode cuidar de uma tarefa.
# 🐛 Facilitar a correção — se algo estiver errado, você sabe onde procurar.
# 📖 Facilitar a leitura — fica mais fácil entender o que o programa está fazendo.

# Uma forma simples de lembrar:
# Função = criar uma tarefa que posso chamar sempre que precisar.