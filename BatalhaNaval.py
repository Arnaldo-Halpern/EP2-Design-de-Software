from funcoes import define_posicoes, preenche_frota, faz_jogada, posiciona_frota, afundados, posicao_valida, monta_tabuleiros

# ---------- frota do jogador ----------
navios = {
    'porta-aviões': [1, 4],
    'navio-tanque': [2, 3],
    'contratorpedeiro': [3, 2],
    'submarino': [4, 1],
}

frota = {}
for nome, (quantidade, tamanho) in navios.items():
    for i in range(quantidade):
        print(f'Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}')
        valida = False
        while not valida:
            linha = int(input('Linha: '))
            coluna = int(input('Coluna: '))
            orientacao = 'horizontal'
            if nome != 'submarino':
                escolha = int(input('[1] Vertical [2] Horizontal >'))
                if escolha == 1:
                    orientacao = 'vertical'
            if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                valida = True
            else:
                print('Esta posição não está válida!')
        frota = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)

# ---------- frota do oponente (posicionamento padrão) ----------
frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

# ---------- tabuleiros ----------
tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota)

total_navios = sum(len(lista) for lista in frota_oponente.values())
jogadas = []

# ---------- loop principal do jogo ----------
jogando = True
while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    linha = int(input('Jogador, qual linha deseja atacar? '))
    while linha < 0 or linha > 9:
        print('Linha inválida!')
        linha = int(input('Jogador, qual linha deseja atacar? '))

    coluna = int(input('Jogador, qual coluna deseja atacar? '))
    while coluna < 0 or coluna > 9:
        print('Coluna inválida!')
        coluna = int(input('Jogador, qual coluna deseja atacar? '))

    if [linha, coluna] in jogadas:
        print(f'A posição linha {linha} e coluna {coluna} já foi informada anteriormente!')
    else:
        jogadas.append([linha, coluna])
        tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)

        if afundados(frota_oponente, tabuleiro_oponente) == total_navios:
            print('Parabéns! Você derrubou todos os navios do seu oponente!')
            jogando = False
