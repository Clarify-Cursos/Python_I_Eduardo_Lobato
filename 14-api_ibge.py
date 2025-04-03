#Este programa indica quantas vezes seu nome foi registrado em uma região ( ou no Brasil inteiro ) durante um período específico

#importação dos pacotes. Instalar o requests ( pip install requests) e solicitar o mesmo os alunos
import json, requests

#pedimos o nome do usuário para fazer a busca pelo nome dele
nome = str(input('Insira seu nome : '))
localidade = 0

#Aqui, ao invés de utilizarmos um catch ou if else para evitar dados errados, utilizamos um while com os dados inválidos. Assim, é feito o bloqueio e não saimos do sistema
while localidade < 1 or localidade > 2:
    localidade = int(input("Você deseja selecionar uma localidade ? \n [1] - Sim \n [2] - Não \n"))

#Se for solicitada a inserção da localidade...
if localidade == 1:
    uf = int(input('''
                Qual UF deseja buscar ?
                [31] - MG
                [33] - RJ
                [35] - SP
                [43] - RS
                [53] - DF
            '''))
    
    #...coletamos os resultados aqui, indexando as varáveis no link. Utilizamos a propriedade get para reter os dados na variável.
    resultado = requests.get(f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}?localidade={uf}")

    # se não for solicitada uma localidade, faremos a busca somente com o nome
if localidade == 2:
    resultado = requests.get(f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}")

    #aqui, selecionamos o período que será solicitado
print('''
      Escolha o período de tempo:
      [1] - 1930
      [2] - 1930 - 1940
      [3] - 1940 - 1950
      [4] - 1950 - 1960
      [5] - 1960 - 1970
      [6] - 1970 - 1980
      [7] - 1980 - 1990
      [8] - 1990 - 2000
      [9] - 2000 - 2010
      ''')

#e aqui, devido aos valores referenciados em um site começarem em zero, como um array, coletaremos o valor escolhido na variável e subtrairemos o mesmo com menos 1 
tempo = int(input("Selecione um período: "))-1

#no final, com a variável resultado e as propriedades em json, colocamos os dados de texto da página do ibge em uma nova variável...
dados = json.loads(resultado.text)

#...e exibimos, com essa nova variável, os resultados no terminal.
print(dados[0]['res'][tempo])




