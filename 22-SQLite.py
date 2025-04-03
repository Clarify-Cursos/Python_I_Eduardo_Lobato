#se precisar, instale a bivblioteca sqlite, mas ela já vem entre as bibliotecas default do python
#instale o pandas (pip install pandas)
#PROCURE SOBRE AS LIMITAÇÕES DO SQLite : alguns comandos TSQL como ALTER TABLE não funcionam nesse programa

import sqlite3
import pandas as pd

# Abre a conexão com banco de dados
conn = sqlite3.connect('meubanco.db')
print('conexão aberta')

# A biblioteca sqlite permite programar em SQL dentro do Python
#No comando abaixo, estou utilizando sintaxe SQLite

conn.execute(''' 
    CREATE TABLE IF NOT EXISTS Alunos(
        matricula integer,
        nome string,
        curso string
    );             
''')

#Comando que executa o TSQL
conn.commit()
print('Tabela criada com sucesso')

#Inserindo dados na tabela

conn.execute('''INSERT INTO Alunos VALUES(1, "Caio", "Python");''')
conn.execute('''INSERT INTO Alunos VALUES(2, "Eduardo", "SQL");''')
conn.execute('''INSERT INTO Alunos VALUES(3, "Amanda", "Oracle");''')
conn.execute('''INSERT INTO Alunos VALUES(4, "Henrique", "NASA");''')


conn.commit()
print('Dados inseridos com sucesso')

alunos_encontrados = conn.execute('''
    SELECT matricula, nome FROM Alunos
''')

for linha in alunos_encontrados:
    print("Matrícula: " + str(linha[0]))
    print("Aluno: " + str(linha[1]))

pedido = """
    SELECT * FROM Alunos
"""

estruturadedados = pd.read_sql_query(pedido, conn)
print(estruturadedados)

conn.close()