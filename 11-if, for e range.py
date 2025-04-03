# numeros: Esta linha declara uma variável chamada numeros e atribui a ela uma lista vazia ([]). Esta lista armazenará os números fornecidos pelo usuário.
numeros = []

# numero: Esta linha solicita ao usuário que insira o número desejado de elementos para o array. A função input() lê a entrada do usuário como uma string.# int(): A função int() converte a entrada do usuário (que inicialmente é uma string) em um número inteiro e a armazena na variável numero. Isso ocorre porque precisamos de um valor numérico para determinar o tamanho do array.
numero = int(input("Digite, de 1 a 3, quantos números seu array terá : "))

# Instrução if: Esta linha verifica se o valor de numero está dentro do intervalo aceitável (1 a 3). O operador and garante que ambas as condições sejam verdadeiras.

# Se a condição for True: O código dentro do bloco if é executado.
# Se a condição for Falsa: O código dentro do bloco else é executado.
# for Loop: Se a condição na instrução if for True, este loop itera inúmeras vezes.
if numero >= 1 and numero < 4:
    # range(numero): Esta função gera uma sequência de números de 0 a numero - 1. A variável de loop i assume cada valor nesta sequência.
    # Dentro do circuito:
    for i in range(numero):
        # componente = int(input(f"Digite o numero {i+1} : ")): Esta linha solicita que o usuário insira um número e o converte em um número inteiro usando int(). A formatação da string f insere o número da iteração atual (i+1) na mensagem de prompt.
        componente = int(input(f"Digite o numero {i+1} : "))

        # numeros.append(componente): Esta linha adiciona o número inserido (componente) ao final da lista de números.
        numeros.append(componente)

    # Função print() (dentro do bloco if): Após a conclusão do loop, esta linha imprime a lista de números final, mostrando ao usuário o array que ele criou.
    print("Os numeros do seu array são :", numeros)
else:
    # Bloco else: Se a condição inicial (número entre 1 e 3) for False, este bloco é executado e imprime uma mensagem de erro indicando uma entrada inválida.
    print("Erro na operação")



    '''sites para estatística
    https://www.brasil.io
    https://servicodados.ibge.gov.br/api/docs/
    sites para programas
    https://www.kaggle.com - ótima comunidade python
    https://color.adobe.com - paleta de cores RGB
    https://ollama.com - sistemas para carregar modelos de dados em C
    https://colab.research.google.com - Google Colab, ótimo para treinamento de Python, com muitos ambientes e exemplos prontos
    https://plotly.com/python - IA de gráficos em Python
    https://plotly.com
    #https://egua.dev/ - linguagem de programação em português
    #https://appinventor.mit.edu - inventor de aplicativos MIT
    
    '''

