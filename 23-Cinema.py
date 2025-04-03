#webscraping da página tmdb.com

from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
from colorama import init, Fore, Back, Style

#url da página alvo
url = 'https://www.themoviedb.org/movie'

#cabeçalho com user-agent para simular um navegador específico. Com essas linhas de comando, burlamos sistemas de segurança nos servidores                                                                                                                              
headers0 = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36' }

#fazendo a requisição
response = requests.get(url, headers=headers0)

#verificar se a resposta foi positiva
if response.status_code == 403: #se o acesso não for autorizado
    print(f'Erro {response.status_code}: Não autorizado')
elif response.status_code != 200: #se o acesso for negado por motivo desconhecido
    print(f'Erro {response.status_code}: Acesso Negado')
else:
    #se passou daqui, tudo deu certo ao capturar a página, então vamos realizar o scrapping
    soup = BeautifulSoup(response.text, 'html.parser')

    #verifica a estrutura HTML, nas primeiras 1000 linhas ( Conta as linhas de css, por isso, visualmente, dará muito menos )
    #print(soup.prettify()[:1000])

    #selecionando os filmes da página
    movies = soup.find_all('div', class_='card style_1')

    #verifica quantos filmes foram encontrados
    print(f'Total de filmes: {len(movies)}')

    #lista e armazena as informações dos filmes
    movies_list = []

    #iterando sobre os filmes para extrair as informações
    for movie in movies:
        try:
            #extrair o título
            title_tag=movie.find('a', class_='image') 
            nome_filme=title_tag['title'] if title_tag else 'Título não encontrado'#estrutura de decisão pequena, caso não tenha um título
            date_tag = movie.find('p')
            release_date = date_tag.get_text(strip=True) if date_tag else 'Data não encontrada'
            tabela = {"título":nome_filme, 
                      "Data":release_date}
            movies_list.append(tabela)

        #A mensagem será exibida caso exista um erro na listagem   
        except Exception as erro:
            print(f'Erro ao processar o filme: {erro}')

    

    #por fim, colocamos a lista no dataframe e exibimos o dataframe
    df = pd.DataFrame(movies_list)

    if not df.empty:
        print(df)

        #salvar em csv
        df.to_csv('movies.csv', index=False)
        print('Tabela salva com sucesso')

        print("Dados das datas extraídas", df['Data'].head())

        #garantir que as datas sejam corretamente interpretadas
        df['Data'] = pd.to_datetime(df['Data'], format='%d de %b de %Y', errors='coerce')

        print('Dados das datas extraídas', df['Data'].head())

        #extraindo o mês e ano da data
        df['Mês/Ano'] = df['Data'].dt.to_period('M')

        #Contando os valores encontrados para montar o gráfico
        filmes_por_mes = df['Mês/Ano'].value_counts().sort_index()

        #plotar o gráfico de barras
        plt.figure(figsize=(10,6))
        filmes_por_mes.plot(kind='bar', color='skyblue')
        plt.title('Quantidade de filmes por mês')
        plt.xlabel('Mês/Ano')
        plt.ylabel('Quantidade de Filmes')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        #extraindo o mês e ano da data
        df['Mês/Ano'] = df['Data'].dt.to_period('y')

        #Contando os valores encontrados para montar o gráfico
        filmes_por_mes = df['Mês/Ano'].value_counts().sort_index()

        #plotar o gráfico de barras
        plt.figure(figsize=(10,6))
        filmes_por_mes.plot(kind='bar', color='gold')
        plt.title('Quantidade de filmes por Ano')
        plt.xlabel('Ano')
        plt.ylabel('Quantidade de Filmes')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    else:
        print('Nenhum dado encontrado')