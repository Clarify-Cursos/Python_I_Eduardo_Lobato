# esta linha importa a função randint do módulo aleatório. Esta função é usada para gerar um número inteiro aleatório dentro de um intervalo especificado.
from random import randint

# O código imprime uma mensagem de boas-vindas.
# Ele define os valores mínimo (mín.) e máximo (máx.) do número aleatório como 0 e 100, respectivamente.
# Inicializa uma variável gameOver como False, indicando que o jogo ainda não acabou.
print("####---------- VAMOS JOGAR ? ----------####")
min = 0
max = 100
gameOver = False


# Este loop while mantém o jogo rodando enquanto gameOver for False.
while gameOver != True:


    # - Dentro do loop principal, diversas variáveis ​​são inicializadas:
    # - `chute`: Armazena o palpite do jogador.
    # - `chances`: Armazena o número de palpites restantes.
    # - `dificuldade`: Armazena o nível de dificuldade escolhido pelo jogador.
    chute = 0
    chances = 0
    dificuldade = 0

    # O código solicita ao jogador que selecione um nível de dificuldade (1 para Fácil, 2 para Normal, 3 para Difícil).
    # Com base na dificuldade escolhida, é definido o número de chances.
    # Um número aleatório é gerado usando randint dentro do intervalo mínimo e máximo especificado.
    while dificuldade < 1 or dificuldade > 3:
        dificuldade = int(input("Selecione:\n [1] - Fácil \n [2] - Normal \n [3] - Dificil \n AGORA : "))
        if dificuldade == 1:
            chances = 15
        elif dificuldade == 2:
            chances = 10
        elif dificuldade == 3:
            chances = 5
        random = randint(min, max)


        # Este loop while continua até que o jogador adivinhe o número correto (aleatório).
            # O jogador é solicitado a inserir seu palpite.
            # Se a estimativa for numérica:
                # Ele converte a estimativa em um número inteiro.
                # Diminui o número de chances em 1.
                # Se as chances chegarem a 0, o jogo termina com a mensagem “Você perdeu”.
            # Se o palpite estiver correto:
                # Ele imprime uma mensagem “Você ganhou” e revela o número aleatório.
                # Ele sai do loop interno.
            # Se a estimativa estiver incorreta:
                # Imprime uma mensagem "Incorreto" e as chances restantes.
                # Dá uma dica ao jogador (maior ou menor).
        while chute != random:
            chute = input(f'chute um número entre {min} e {max} : ')
            
            if chute.isnumeric():
                chute = int(chute)
                chances = chances - 1
                if chances == 0:
                    print("SUAS CHANCES ACABARAM E VOCÊ PERDEU ! HAHAHAHAHAHAHAHAHAHAH !")
                    break
                else:
                    if chute == random:
                        print('WE ARE THE CHAMPIONS !')
                        print('Você venceu, parabéns !')
                        print(f'O numero era {random} e você ainda tinha {chances} chance(s)')
                        print('CLAP, CLAP, CLAP, CLAP, CLAP !')
                        break
                    else:
                        print(f'Errado ! Você só tem mais {chances} chances!')
                        if chute > random:
                            print('Uma dica, meu número é menor')
                        else:
                            print('Uma dica, meu número é maior')

    # - Após cada rodada, o jogador é questionado se deseja jogar novamente.
    # - Se o jogador digitar 2, `gameOver` será definido como `True`, encerrando o loop principal do jogo e o programa.                          
    print("####---------- VAMOS JOGAR DE NOVO ? ----------####")
    replay = 0
    while replay < 1 or replay > 2:
        replay = int(input("Digite 1 para continuar, 2 para sair: "))
        if replay == 2:
            print('Nos vemos em breve !')
            gameOver = True



