class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.plano = plano

cliente = Cliente ("fulano", "email@email.com", "Plus master NET")

print("Nome: ", cliente.nome)
print("Email: ", cliente.email)
print("Plano: ", cliente.plano)

