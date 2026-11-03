def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    for i in range(tamanho):
        if orientacao == "vertical":
            posicoes.append([linha + i, coluna])
        else:
            posicoes.append([linha, coluna + i])
    return posicoes



def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    i = 0
    while i < tamanho:
        if orientacao == 'vertical':
            posicoes.append([linha + i, coluna])   # desce linha a linha
        else:
            posicoes.append([linha, coluna + i])   # anda coluna a coluna
        i = i + 1
    return posicoes


def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    navio = define_posicoes(linha, coluna, orientacao, tamanho)

    if nome_navio in frota:
        frota[nome_navio].append(navio)    
    else:
        frota[nome_navio] = [navio]        

    return frota


def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro


def posiciona_frota(frota):
    tabuleiro = [[0] * 10 for i in range(10)]
    for navios in frota.values():
        for navio in navios:
            for linha, coluna in navio:
                tabuleiro[linha][coluna] = 1
    return tabuleiro
