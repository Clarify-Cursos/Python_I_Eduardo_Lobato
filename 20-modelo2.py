#Vamos começar com uma classe chamada carro. Uma classe é um molde ou planta que define como os objetos dessa classe serão
#Ela define o que um objeto pode fazer (os métodos) e o que eles têm (atributos)

class Carro:
    #A classe carro tem dois atributos: "marca" e "modelo", além de um método, acelerar.
    #método especial __init__ - é o que chamamos quando criamos um objeto de classe.
    #ele inicializa os atributos do objeto (marca e modelo)
    def __init__(self, marca, modelo, cor):
        #os atributos do objeto serão definidos dentro do módulo init
        #o self refere-se ao próprio obejto que está sendo criado e é o valor padrão para qualquer tipo de classe
        self.modelo = modelo #atributo que armazena o modelo
        self.marca = marca #atributo que armazena a marca
        self.cor = cor
    #métodos que definem o comportamento do objeto, aqui estamos falando o que de fato o carro faz
    def acelerar(self):
        print(f"O {self.marca} {self.modelo} está acelerando !")

    def parar(self):
        print(f"O {self.marca} {self.modelo} parou !")

    def corinthians(self):
        print(f"O {self.marca} {self.modelo} é um carro {self.cor} cromado da Gaviões da Fiel !")

    def direita(self):
        print(f"O {self.marca} {self.modelo} {self.cor} virou à direita !")

    def esquerda(self):
        print(f"O {self.marca} {self.modelo} {self.cor} virou à esquerda !")

carro1 = Carro("Fusca", "1984", "Preto")
print(carro1.marca)
print(carro1.modelo)
print(carro1.cor)
carro1.acelerar()
carro1.parar()
carro1.corinthians()
carro1.direita()
carro1.esquerda()