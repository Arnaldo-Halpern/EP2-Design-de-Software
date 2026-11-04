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

# confere se o navio cabe no tabuleiro e nao bate em outro navio
def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    for l, c in posicoes:
        if l < 0 or l > 9 or c < 0 or c > 9:
            return False
        for navios in frota.values():
            for navio in navios:
                if [l, c] in navio:
                    return False
    return True


# monta o texto com os dois tabuleiros lado a lado
def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '___________      ___________\n'
    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto
