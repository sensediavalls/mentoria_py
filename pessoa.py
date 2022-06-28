class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura


pessoa = Pessoa("Isadora", "23", "1.58")

print("Nome: ", pessoa.nome)
print("Idade: ", pessoa.idade)
print("Tamaninho: ", pessoa.altura)
