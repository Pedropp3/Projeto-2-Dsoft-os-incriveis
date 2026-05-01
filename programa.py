from funcoes import *
def cartela_completa(cartela):
    for chave in cartela["regra_simples"]:
        if cartela["regra_simples"][chave] == -1:
            return False
    for chave in cartela["regra_avancada"]:
        if cartela["regra_avancada"][chave] == -1:
            return False
    return True
cartela = {
    "regra_simples": {
        1: -1,
        2: -1,
        3: -1,
        4: -1,
        5: -1,
        6: -1
    },
    "regra_avancada": {
        "sem_combinacao": -1,
        "quadra": -1,
        "full_house": -1,
        "sequencia_baixa": -1,
        "sequencia_alta": -1,
        "cinco_iguais": -1
    }
}
imprime_cartela(cartela)
while not cartela_completa(cartela):
    dados_rolados = rolar_dados(5)
    dados_guardados = []
    rerrolagens = 0
    rodada_finalizada = False
    print(f"Dados rolados: {dados_rolados}")
    print(f"Dados guardados: {dados_guardados}")
    print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
    opcao = input()
    while not rodada_finalizada:
        if opcao == "1":
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice = int(input())
            guardar_dado(dados_rolados, dados_guardados, indice)
        elif opcao == "2":
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice = int(input())
            remover_dado(dados_rolados, dados_guardados, indice)
        elif opcao == "3":
            if rerrolagens < 2:
                quantidade_dados = len(dados_rolados)
                dados_rolados = rolar_dados(quantidade_dados)
                rerrolagens = rerrolagens + 1
            else:
                print("Você já usou todas as rerrolagens.")
        elif opcao == "4":
            imprime_cartela(cartela)
        elif opcao == "0":
            print("Digite a combinação desejada:")
            combinacao = input()
            combinacao_marcada = False
            while not combinacao_marcada:
                dados_atuais = dados_rolados + dados_guardados
                if combinacao == "1" or combinacao == "2" or combinacao == "3" or combinacao == "4" or combinacao == "5" or combinacao == "6":
                    numero = int(combinacao)
                    if cartela["regra_simples"][numero] != -1:
                        print("Essa combinação já foi utilizada.")
                        combinacao = input()
                    else:
                        pontos_simples = calcula_pontos_regra_simples(dados_atuais)
                        cartela["regra_simples"][numero] = pontos_simples[numero]
                        combinacao_marcada = True
                        rodada_finalizada = True
                elif combinacao in cartela["regra_avancada"]:
                    if cartela["regra_avancada"][combinacao] != -1:
                        print("Essa combinação já foi utilizada.")
                        combinacao = input()
                    else:
                        pontos_avancados = calcula_pontos_regra_avancada(dados_atuais)
                        cartela["regra_avancada"][combinacao] = pontos_avancados[combinacao]
                        combinacao_marcada = True
                        rodada_finalizada = True
                else:
                    print("Combinação inválida. Tente novamente.")
                    combinacao = input()
        else:
            print("Opção inválida. Tente novamente.")
            opcao = input()
            continue
        if not rodada_finalizada:
            print(f"Dados rolados: {dados_rolados}")
            print(f"Dados guardados: {dados_guardados}")
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            opcao = input()
pontuacao = 0
for chave in cartela["regra_simples"]:
    valor = cartela["regra_simples"][chave]
    if valor != -1:
        pontuacao = pontuacao + valor
for chave in cartela["regra_avancada"]:
    valor = cartela["regra_avancada"][chave]
    if valor != -1:
        pontuacao = pontuacao + valor
soma_regra_simples = 0
for chave in cartela["regra_simples"]:
    valor = cartela["regra_simples"][chave]
    if valor != -1:
        soma_regra_simples = soma_regra_simples + valor
if soma_regra_simples >= 63:
    pontuacao = pontuacao + 35
imprime_cartela(cartela)
print(f"Pontuação total: {pontuacao}")