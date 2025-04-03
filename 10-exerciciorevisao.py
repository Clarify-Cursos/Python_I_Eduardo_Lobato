#Até aqui, exercício
# O código primeiro pede o nome do aluno e o armazena na variável nomeAluno.
# Em seguida, ele solicita as notas do aluno nos quatro bimestres (períodos letivos) e as armazena como números de ponto flutuante (números com decimais) nas variáveis: nota01, nota02, nota03 e nota04.


nomeAluno = str(input("Digite o nome do aluno :"))
nota01 = float(input("Qual a nota do primeiro bimestre : "))
nota02 = float(input("Qual a nota do segundo bimestre : "))
nota03 = float(input("Qual a nota do terceiro bimestre : "))
nota04 = float(input("Qual a nota do quarto bimestre : "))
mediaAluno = (nota01 + nota02 + nota03 + nota04) / 4
print(f"A média do aluno foi : ", round(mediaAluno,2))


#Aqui, explicação
# Em seguida, solicita a frequência de frequência do aluno (em porcentagem) e armazena-a como um número inteiro (um número inteiro) na variável freqAluno.

freqAluno = int(input("Digite a frequência, em porcentagem, do aluno, de 0 a 100 :"))

# Por fim, solicita o tipo de escola (pública ou privada) e armazena-o como um número inteiro (1 para pública, 2 para privada) na variável tipoEscola e verifica a situação final

tipoEscola = int(input("Tipo do Colegio: \n [1]Publico \n [2]Particular \n"))
print(f"O Aluno {nomeAluno} obteve média {round(mediaAluno,2)}")
if tipoEscola == 1:
    if mediaAluno >=5 or freqAluno >=70:
        print("O aluno está aprovado")
    else:
        print("O aluno está reprovado")
elif tipoEscola == 2:
    if mediaAluno >=6 and freqAluno >=75:
        print("O aluno está aprovado")
    else:
        print("O aluno está reprovado")
else:
    print("Tipo de escola inválido, não é possível atribuir a situação final")


