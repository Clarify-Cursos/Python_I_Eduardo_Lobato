# instale as bibliotecas Pandas e random, obrigatóriamente, e datetime e matplotlib, se ainda não estiverem instaladas

import pandas as pd # essa é uma das bibliotecas mais utilizadas do Python
import random
from datetime import datetime, timedelta

#funcao para gerar dados de vendas ficticios em formato de tabela
def gerar_dados(num_linhas, in_min, in_max):
    produtos = ['Tupperware', 'Bombril', 'Xerox', 'Kodak']
    cidades = ['Orlando', 'Anahein', 'Franco da Rocha', 'Poá']
    dados = []
    # in_min = 0
    # in_max = 365
    #com o range, eu consigo controlar o número de vezes que uma repetição será feita em um for, trazendo exatamente o que é pedido, como um procv
    for _ in range(num_linhas):
        produto = random.choice(produtos)
        cidade = random.choice(cidades)
        # round - eu crio um valor arredendado sobre o valor final, pra cima ou pra baixo / :.2f - pego o valor final e deixo com 2 casas decimais, apenas excluindo o que sobrar
        valor = round(random.uniform(50,500),2)
        #timedelta - propriedade que facilita o cálculo entre valores de data
        data = datetime.today() - timedelta(days=random.randint(in_min, in_max))
        #adiciono valores na tabela
        dados.append([produto, cidade, valor, data])
    # e retorno os dados
    return dados

#com esta instrução, serão construídos 100 registros, automáticamente, com intervalo de datas de 1 a 365 dias

dados_prontos = gerar_dados(100, 1, 365)

#criar o dataframe (efetivamente a tabela)

df_vendas = pd.DataFrame(dados_prontos, columns = ['Produto', 'Cidade', 'Valor', 'Data'])

#ENFIM, CRIAMOS O ARQUIVO CSV, SEM ÍNDICE, OU SEJA, SEM NÚMERO DE REGISTRO
df_vendas.to_csv('vendas.csv', index=False)
