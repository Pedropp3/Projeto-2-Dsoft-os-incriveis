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