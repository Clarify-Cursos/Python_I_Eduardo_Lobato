#tabela de alíquotas e faixas do imposto de renda

# def calculadora_ir(salario_bruto):: Esta linha define uma função chamada calculadora_ir que recebe um argumento: salario_bruto (salário bruto).

def calculadora_ir(salario_bruto):

# "faixa": Tupla representando os limites inferior e superior da faixa salarial da faixa.
# "aliquota": A alíquota de imposto (em percentual) da faixa.
# "deducao": O valor da dedução da faixa.

    tabela_ir = [
        {
            "faixa":(0,1903.98),
            "aliquota":0,
            "deducao":0
        },
        {
            "faixa":(1903.99,2826.65),
            "aliquota":7.5,
            "deducao":142
        },
        {
            "faixa":(2826.66,3751.05),
            "aliquota":15,
            "deducao":354
        },
        {
            "faixa":(3751.06,4664.68),
            "aliquota":22.5,
            "deducao":636
        },
        {
            "faixa":(4664.69,float("inf")),
            "aliquota":27.5,
            "deducao":869
        }
    ]

# calculando o imposto de renda

# for faixa in tabela_ir:: Esta linha inicia um loop que itera por cada colchete de imposto na lista tabela_ir.
    imposto = 0
    for faixa in tabela_ir:
        # if salario_bruto > faixa['faixa'][0] e salario_bruto <= faixa['faixa'][1]:: Esta linha verifica se o salario_bruto está dentro da faixa de imposto atual.

        # resultado = (salario_bruto * faixa['aliquota']) / 100 - faixa['deducao']: Se o salario_bruto estiver dentro da faixa de imposto vigente, esta linha calcula o imposto de renda devido através da fórmula: (salário bruto * alíquota / 100) - dedução.

        # break: Esta linha sai do loop após o cálculo do imposto de renda.

        # return resultado: Esta linha retorna o imposto de renda calculado (resultado).
        if salario_bruto > faixa['faixa'][0] and salario_bruto <= faixa['faixa'][1]:
            resultado = (salario_bruto * faixa['aliquota']) / 100 - faixa['deducao']
            break
    return resultado
#testando nossa função de cálculo de imposto de renda

salario_bruto = float(input("Informe o seu salário Bruto: "))
seuImposto = calculadora_ir(salario_bruto)
print(f'o Imposto devido é de R$ {seuImposto:.2f}')

