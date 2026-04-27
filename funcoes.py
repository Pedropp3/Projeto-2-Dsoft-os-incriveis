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