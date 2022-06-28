class ControleRemoto:
    def __init__(self, cor, altura, profundidade, largura):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura

    def passar_canal(self, botao):

        if botao == "+":
            print("Aumentando o canal em +1")

        elif botao == "-":
            print("Diminuindo o canal em -1")


controle_remoto_net = ControleRemoto("preto", "10cm", "3cm", "2cm")
print("A cor do controle remoto NET é:", controle_remoto_net.cor)
print("A largura do controle remoto NET é:", controle_remoto_net.largura)
print("A altura do controle remoto NET é:", controle_remoto_net.altura)
print("A profundidade do controle remoto NET é:", controle_remoto_net.profundidade)
controle_remoto_net.passar_canal("+")

controle_remoto_aws = ControleRemoto("chumbo", "07cm", "2.5cm", "1cm")
print(controle_remoto_aws.largura)
