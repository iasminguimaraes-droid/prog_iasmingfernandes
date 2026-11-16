"""Aula 07: grafos e busca em largura.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.

O grafo e um dicionario: chave = no, valor = lista de vizinhos.
Todo no aparece como chave (lista vazia se nao tiver vizinhos).
Use uma FILA e uma lista de VISITADOS. Nao altere o grafo recebido.
"""


def grau(grafo, no):
    """Quantas setas saem do no (quantos vizinhos ele tem)."""
    return len(grafo.get(no, []))


def existe_caminho(grafo, origem, destino):
    """True se da para chegar da origem ao destino, False se nao da.
    Origem igual ao destino: True."""
    if origem == destino:
        return True

    visitados = set([origem])
    fila = deque([origem])

    while fila:
        atual = fila.popleft()
        for vizinho in grafo.get(atual, []):
            if vizinho == destino:
                return True
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)

    return False


def distancia(grafo, origem, destino):
    """Menor numero de setas da origem ao destino.
    Sem caminho: -1. Origem igual ao destino: 0."""
    if origem == destino:
        return 0

    visitados = set([origem])
    fila = deque([(origem, 0)])

    while fila:
        atual, dist = fila.popleft()
        for vizinho in grafo.get(atual, []):
            if vizinho == destino:
                return dist + 1
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append((vizinho, dist + 1))

    return -1

def menor_caminho(grafo, origem, destino):
    """(Desafio) Lista dos nos do caminho mais curto, com origem e destino.
    Sem caminho: []. Origem igual ao destino: [origem]."""
    if origem == destino:
        return [origem]

    visitados = set([origem])
    fila = deque([[origem]])

    while fila:
        caminho = fila.popleft()
        atual = caminho[-1]

        for vizinho in grafo.get(atual, []):
            novo_caminho = caminho + [vizinho]
            if vizinho == destino:
                return novo_caminho
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(novo_caminho)

    return []
