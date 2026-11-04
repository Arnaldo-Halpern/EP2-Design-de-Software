def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    for i in range(tamanho):
        if orientacao == "vertical":
            posicoes.append([linha + i, coluna])
        else:
            posicoes.append([linha, coluna + i])
    return posicoes


def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    navio = define_posicoes(linha, coluna, orientacao, tamanho)

    if nome_navio in frota:
        frota[nome_navio].append(navio)    
    else:
        frota[nome_navio] = [navio]        

    return frota


# marca X se acertou um navio e - se acertou a agua
def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro


# cria o tabuleiro 10x10 e coloca 1 onde tem navio
def posiciona_frota(frota):
    tabuleiro = [[0] * 10 for i in range(10)]
    for navios in frota.values():
        for navio in navios:
            for linha, coluna in navio:
                tabuleiro[linha][coluna] = 1
    return tabuleiro


# conta quantos navios tem todas as posicoes com X
def afundados(frota, tabuleiro):
    total = 0
    for navios in frota.values():
        for navio in navios:
            afundou = True
            for linha, coluna in navio:
                if tabuleiro[linha][coluna] != 'X':
                    afundou = False
            if afundou:
                total += 1
    return total

def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes == define_posicoes(linha, coluna, orientacao, tamanho)

    for posicao in posicoes:
        if posicao[0] <= 0 or posicao[0] > 9 or posicao[1] < 0 or posicao[1] > 9:
            return False

        for nome_navio in frota:
            for navio in frota[nome_navio]:
                if posicao in navio:
                    return False

    return True