
palavra = "sucesso"

#todo o processo de looping precisa de um contador

contador = 0

#para cada letra na palavra

for letra in palavra:
    print(str(contador) + " - " + letra)
    contador = contador + 1

#esse código desmembrará o conteúdo da palavra sucesso como uma srting, e vai trazer letra por letra da palavra até o final dela.

cidades = [
    'São Paulo', 
    'Barueri', 
    'Poá', 
    'Atibaia', 
    'Manaus'
    ]

# print(cidades[3])

for cidade in cidades:
    print(cidade)

botaoExecutar = True
contador = 0

#while - enquanto

def minhafuncao():
    print("ACABOU !")
    return

while botaoExecutar:
    print(contador)
    contador = contador + 1
    if contador >= 10:
        minhafuncao()
        break

def minhafuncaomelhorada(informacao, x):
    print(f'{x} - {informacao}')

#for - para

contador = 0
for cidade in cidades :
    contador = contador + 1
    minhafuncaomelhorada(cidade, contador)
