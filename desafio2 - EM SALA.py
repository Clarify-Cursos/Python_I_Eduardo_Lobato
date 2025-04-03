estoque = {}
menu = 0

def adicionar_produtos():
    nome = str(input("Digite o nome do produto :"))
    quantidade = int(input("Digite a quantidade do produto: "))
    preco = float(input("Digite o preço do produto :"))
    estoque[nome] = {'nome':nome, 'quantidade':quantidade, 'preço':preco}
    print(f'Produto {nome} adicionado com sucesso !')

def atualizar_produto():
    nome = str(input("Digite o nome do produto :"))
    if nome in estoque:
        operacao = int(input("digite 1 para adicionar quantidade e 2 para remover quantidade"))
        quantidade = int(input("Digite a quantidade: "))
        if operacao == 1:
            estoque[nome]['quantidade'] += quantidade
            print(f"Quantidade do produto {nome} aumentada com sucesso !")
        elif operacao == 2:
            if quantidade <= estoque[nome]['quantidade']:
                estoque[nome]['quantidade'] -= quantidade
                print(f"Quantidade do produto {nome} subtraída com sucesso !")
            else:
                print("Operação inválida por erro de estoque")
        else:
            print("Operação inválida, insira 1 ou 2, apenas")
    else:
        print("Produto não encontrado no estoque")

def remover_produto():
    nome = str(input("Digite o nome do produto :"))
    if nome in estoque:
        del estoque[nome]
        print(f"Produto {nome} removido com sucesso")
    else:
        print("Produto não encontrado no estoque")

def listar_produtos():
    if not estoque:
        print("Estoque vazio")
    else:
        for nome, info in estoque.items():
            print(f"Produto:{info['nome']}, Quantidade:{info['quantidade']}, Preço; R${info['preço']:.2f}")

while menu < 5:
    menu = int(input('''
            Selecione a operação:
            [1] - ADICIONAR PRODUTO AO ESTOQUE
            [2] - ATUALIZAR A QUANTIDADE DE UM PRODUTO
            [3] - REMOVER UM PRODUTO
            [4] - LISTAR TODOS OS PRODUTOS
            [5] - SAIR
            Sua escolha: '''))
    
    match menu:
        case 1:
            adicionar_produtos()
        case 2:
            atualizar_produto()
        case 3:
            remover_produto()
        case 4:
            listar_produtos()
        case _:
            break
