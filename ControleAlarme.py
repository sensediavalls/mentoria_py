class ControleAlarmePositron:
    def __init__(self, cor, formato, peso, material, ativar):
        self.cor = cor
        self.formato = formato
        self.peso = peso
        self.material = material

    def ativar(self, botao):

        if botao == "y":
            print("Blip blip!! Ativado.")
        else:
            print("Blip!! Desativado.")

controleAlarmePositron = ControleAlarmePositron("preto", "retangular", "12g", "plastico", "n")
y = input ('Enter your name:')
print('Bem vindo sr(a), ' + y)

x = input ("Ativar o alarme? y/n \n")

print("Cor do controle: ", controleAlarmePositron.cor)
print("Formato do controle: ", controleAlarmePositron.formato)
print("Peso do controle: ", controleAlarmePositron.peso)
print("Material do controle: ", controleAlarmePositron.material)

controleAlarmePositron.ativar(x)
