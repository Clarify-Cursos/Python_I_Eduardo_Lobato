#Função para criar um carro com marca e modelo
def criar_carro(marca, modelo):
    return{"marca":marca, "modelo":modelo}

#Função acelerar
def acelerar(carro):
    print(f"O {carro['marca']} {carro['modelo']} está acelerando !")

#Função parar
def parar(carro):
    print(f"O {carro['marca']} {carro['modelo']} parou !")

#Funções para virar
def virar_direita(carro):
    print(f"O {carro['marca']} {carro['modelo']} está virando à direita !")

def virar_esquerda(carro):
    print(f"O {carro['marca']} {carro['modelo']} está virando à esquerda !")


#Função para criar um carro adicional
def criar_carro_com_cor(marca, modelo, cor):
    carro = criar_carro(marca, modelo) #cria um carro básico
    carro["cor"] = cor
    return carro

#exibir a cor do carro
def exibir_cor(carro):
    print(f"O carro é da cor {carro['cor']}")

carro1 = criar_carro("Fusca", "1984")
carro2 = criar_carro("Suzuki", "Jimmy")
carro3 = criar_carro_com_cor("Toyota", "Etios", "Branco")

#acelerando e parando os carros
print(carro1["marca"]) #acessando a marca
print(carro1["modelo"]) #acessando o modelo

print(carro3["marca"])
print(carro3["modelo"])
print(carro3["cor"])
exibir_cor(carro3)

print('-----------------------------------------------------')# Separador
acelerar(carro3)
virar_direita(carro3)
parar(carro3)

print(carro2["marca"])
print(carro2["modelo"])
acelerar(carro2)
virar_esquerda(carro2)
parar(carro2)