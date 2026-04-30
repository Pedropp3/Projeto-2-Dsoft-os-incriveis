import random
def rolar_dados (Ndados):
    resultado = []
    a = 0
    i=0
    while i < Ndados:
        a = random.randint(1,6)
        resultado.append(a)
        i = i+1
    return resultado

def guardar_dado (dados_rolados, dados_no_estoque, dado_para_guardar):
    dados_no_estoque.append(dados_rolados[dado_para_guardar])
    dados_rolados.pop(dado_para_guardar)
    return [dados_rolados,dados_no_estoque]

def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    dados_rolados.append(dados_no_estoque[dado_para_remover])
    dados_no_estoque.pop(dado_para_remover)
    return [dados_rolados, dados_no_estoque]

def calcula_pontos_regra_simples (faces):
    valores = {}
    contagem = 1
    while contagem < 7:
        soma = 0
        for face in faces:
            if face == contagem:
                soma = soma + face
        valores[contagem] = soma
        contagem = contagem + 1
    return valores

def calcula_pontos_soma (faces):
    soma = 0
    for face in faces:
        soma = soma + face
    return soma


def calcula_pontos_sequencia_baixa (faces):
    sim = 0
    for f in faces:
        if f + 1 in faces:
            if f+2 in faces:
                if f+3 in faces:
                    sim = 1
    if sim == 1:
        return 15
    else:
        return 0
    
def calcula_pontos_sequencia_alta (faces):
    sim = 0
    for f in faces:
        if f + 1 in faces:
            if f+2 in faces:
                if f+3 in faces:
                    if f+4 in faces:
                        sim = 1
    if sim == 1:
        return 30
    else:
        return 0
    
def calcula_pontos_full_house (dados):
    
    quantidades = []

    for dado in dados:
        quantidade = 0

        for dadoo in dados:
            if dado == dadoo:
                quantidade = quantidade + 1

        quantidades.append(quantidade)

    if 3 in quantidades and 2 in quantidades:
        return dados[0] + dados[1] + dados[2] + dados[3] + dados[4]
    else:
        return 0
    
def calcula_pontos_quadra(dados):
    quantidades = []

    for dado in dados:
        quantidade = 0

        for dadoo in dados:
            if dado == dadoo:
                quantidade = quantidade + 1

        quantidades.append(quantidade)

    for quantidade in quantidades:
        if quantidade >= 4:
            soma = 0

            for dado in dados:
                soma = soma + dado

            return soma

    return 0

def calcula_pontos_quina(dados):
    quantidades = []

    for dado in dados:
        quantidade = 0

        for dadoo in dados:
            if dado == dadoo:
                quantidade = quantidade + 1

        quantidades.append(quantidade)

    for quantidade in quantidades:
        if quantidade >= 5:
            return 50

    return 0

def calcula_pontos_regra_avancada(dados):
    pontos = {}

    pontos["cinco_iguais"] = calcula_pontos_quina(dados)
    pontos["full_house"] = calcula_pontos_full_house(dados)
    pontos["quadra"] = calcula_pontos_quadra(dados)
    pontos["sem_combinacao"] = calcula_pontos_soma(dados)
    pontos["sequencia_alta"] = calcula_pontos_sequencia_alta(dados)
    pontos["sequencia_baixa"] = calcula_pontos_sequencia_baixa(dados)

    return pontos