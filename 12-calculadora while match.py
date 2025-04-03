# ativa é uma variável booleana inicializada como True. Ele controla o loop principal da calculadora, mantendo-a funcionando enquanto permanecer True.
ativa = True
while ativa:

    # Uma string multilinha é atribuída às escolhas, contendo o menu de operações da calculadora.
    # print(escolhas) exibe este menu para o usuário.
    
    escolhas = '''
    Operações de cálculo permitidas
    [1] - Soma
    [2] - Subtração
    [3] - Multiplicação
    [4] - Divisão
    [5] - Potência
    [0] ou [Sair] - Sair
    '''
    print(escolhas)


    # input() solicita que o usuário selecione uma operação digitando um número ou “Sair”.
    # A entrada do usuário é armazenada na variável operador.
    operador = input("Selecione sua opção: ")


    if operador == "0" or operador == "Sair":
        # Se o usuário digitar "0" ou "Sair", o programa imprime uma mensagem de agradecimento e define ativa como False, fazendo com que o loop while termine.
        print("Obrigado por usar nossa Calculadora !")
        ativa = False

        # Se o usuário inserir um operador válido (1-5):
        # Ele solicita dois números (n1 e n2) usando input() e os converte em inteiros usando int().
        # Uma instrução match é usada para executar a operação selecionada com base no valor de operador.
        # O resultado da operação é impresso no console.
        
    elif operador >= "1" and operador < "6":
        n1 = int(input('Entre com o primeiro número: '))
        n2 = int(input('Entre com o segundo número: '))

        match operador:
            case "1":
                print(f'\nSomando os valores, temos: {n1+n2}')
            case "2":
                if n1 >= n2:
                    print(f'\nSubtraindo os valores, temos: {n1-n2}')
                else:
                    print(f'\nSubtraindo os valores, temos: {n2-n1}')
            case "3":
                print(f'\nMultiplicando os valores, temos: {n1*n2}')
            case "4":
                if n2 == 0:
                    print(f'\nNão é possível dividir por zero')
                else:
                    if n1 >= n2:
                        print(f'\nDividindo os valores, temos: {n1/n2}')
                    else:
                        print(f'\nDividindo os valores, temos: {n2/n1}')
            case "5":
                print(f'\nEfetuando a exponenciação entre os valores, temos: {n1**n2}')
            case _:
                print('Erro na operação')
    else:
        print('Erro na Operação')