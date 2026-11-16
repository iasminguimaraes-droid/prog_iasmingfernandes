"""Aula 08: laboratorio de grafos (labirinto).

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.

O labirinto e uma lista de textos: 'S' largada, 'E' saida, '.' livre, '#' parede.
Posicao = tupla (linha, coluna). Nao altere o labirinto nem o grafo recebidos.
"""


def achar(labirinto, letra):
    """JA PRONTA. Posicao (linha, coluna) da primeira ocorrencia da letra,
    ou None se nao existir."""
    for linha in range(len(labirinto)):
        for coluna in range(len(labirinto[linha])):
            if labirinto[linha][coluna] == letra:
                return (linha, coluna)
    return None


def vizinhos(labirinto, linha, coluna):
    """Casas livres ao redor (cima, baixo, esquerda, direita), como lista de
    tuplas (linha, coluna). Parede e fora do labirinto nao contam; 'S' e 'E'
    contam como livres. A ordem nao importa."""
    linhas = len(labirinto)
    colunas = len(labirinto[0]) if linhas > 0 else 0

    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    livres = []

    for dl, dc in direcoes:
        nl = linha + dl
        nc = coluna + dc

        if 0 <= nl < linhas and 0 <= nc < colunas:
           
            if labirinto[nl][nc] != "#":
                livres.append((nl, nc))

    return livres


def passos_ate_saida(labirinto):
    """Menor numero de passos de 'S' ate 'E'. Sem caminho: -1."""
    inicio = fim = None
    for l, linha in enumerate(labirinto):
        for c, celula in enumerate(linha):
            if celula == "S":
                inicio = (l, c)
            elif celula == "E":
                fim = (l, c)

    if not inicio or not fim:
        return -1
    if inicio == fim:
        return 0

    visitados = set([inicio])
    fila = deque([(inicio, 0)])

    while fila:
        (l, c), passos = fila.popleft()
        for nl, nc in vizinhos(labirinto, l, c):
            if (nl, nc) == fim:
                return passos + 1
            if (nl, nc) not in visitados:
                visitados.add((nl, nc))
                fila.append(((nl, nc), passos + 1))

    return -1


def alcance(grafo, origem, k):
    """Nos a no maximo k setas da origem, SEM contar a propria origem, sem
    repetidos, em qualquer ordem. k = 0 devolve lista vazia."""
    if k <= 0:
        return []

    visitados = set([origem])
    fila = deque([(origem, 0)])
    alcancaveis = []

    while fila:
        atual, dist = fila.popleft()
        if dist == k:
            continue

        for vizinho in grafo.get(atual, []):
            if vizinho not in visitados:
                visitados.add(vizinho)
                alcancaveis.append(vizinho)
                fila.append((vizinho, dist + 1))

    return alcancaveis


def caminho_ate_saida(labirinto):
    """(Desafio) Lista de posicoes do caminho mais curto de 'S' ate 'E',
    incluindo as duas. Sem caminho: []."""
    inicio = fim = None
    for l, linha in enumerate(labirinto):
        for c, celula in enumerate(linha):
            if celula == "S":
                inicio = (l, c)
            elif celula == "E":
                fim = (l, c)

    if not inicio or not fim:
        return []
    if inicio == fim:
        return [inicio]

    visitados = set([inicio])
    fila = deque([[inicio]])

    while fila:
        caminho = fila.popleft()
        l, c = caminho[-1]

        for prox in vizinhos(labirinto, l, c):
            novo_caminho = caminho + [prox]
            if prox == fim:
                return novo_caminho
            if prox not in visitados:
                visitados.add(prox)
                fila.append(novo_caminho)

    return []
