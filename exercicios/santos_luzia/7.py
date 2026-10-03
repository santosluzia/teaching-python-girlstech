class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos"
    
ana = Pessoa("Ana", 25) 
print(ana.apresentar())

# Programação Orientada a Objetos (POO) é um modelo de desenvolvimento que usa objetos para representar coisas e ideias do mundo real no código

# Conceitos Básicos
# Classe: É o molde ou a planta que define como um objeto será. Exemplo: a classe Carro define que todo carro tem cor e velocidade.
# Objeto: É a criação real baseada na classe (chamada de instância). Exemplo: o carro vermelho do seu vizinho é um objeto da classe Carro.
# Atributos: São as características ou propriedades do objeto (cor, marca, preço).
# Métodos: São as ações que o objeto pode fazer (ligar, acelerar, frear)