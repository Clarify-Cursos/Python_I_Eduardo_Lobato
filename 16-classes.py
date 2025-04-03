class Carro:
    def __init__(self, marca, modelo, cor):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor

    def acelerar(self):
        print(f"O {self.marca} {self.modelo} está acelerando")

    def parar(self):
        print(f"O {self.marca} {self.modelo} está parando")

    def direita(self):
        print(f"O {self.marca} {self.modelo} está virando à direita")

    def esquerda(self):
        print(f"O {self.marca} {self.modelo} está virando à esquerda")

carro1 = Carro("Fuca", "1990", "Preto")
print(carro1.marca)
print(carro1.modelo)
print(carro1.cor)
carro1.acelerar()
carro1.parar()
carro1.direita()
carro1.esquerda()