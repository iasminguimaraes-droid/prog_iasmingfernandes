"""Lista B - ordenacao, dois indices e janela, contagem por chave.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.

Nos exercicios de ordenacao, NAO use sorted() nem list.sort().
Onde o enunciado pede lista nova, preserve a lista recebida.
bubble_sort e selection_sort devolvem (lista_ordenada, comparacoes, trocas),
o mesmo contrato da aula05.
"""

# ---------- Bloco 1: ordenacao ----------

def passagem_bubble(lista):
    """Uma unica passagem completa da esquerda para a direita, trocando
    vizinhos fora de ordem. Devolve uma copia; nao altera a entrada."""
    copia = list(lista)
    for i in range(len(copia) - 1):
        if copia[i] > copia[i + 1]:
            copia[i], copia[i + 1] = copia[i + 1], copia[i]
    return copia


def bubble_sort(lista):
    """Bubble sort crescente, parando quando uma passagem nao faz troca.
    Devolve (lista_ordenada, comparacoes, trocas): conte toda comparacao
    entre vizinhos e somente as trocas que acontecerem."""
    copia = list(lista)
    n = len(copia)
    comparacoes = 0
    trocas = 0

    for i in range(n):
        trocou = False
    
        for j in range(n - 1 - i):
            comparacoes += 1
            if copia[j] > copia[j + 1]:
                copia[j], copia[j + 1] = copia[j + 1], copia[j]
                trocas += 1
                trocou = True
        if not trocou:
            break

    return (copia, comparacoes, trocas)

def selection_sort(lista):
    """Selection sort crescente. Devolve (lista_ordenada, comparacoes,
    trocas): conte cada comparacao entre candidatos e as trocas reais
    (nao conte a troca de um valor consigo mesmo)."""
    copia = list(lista)
    n = len(copia)
    comparacoes = 0
    trocas = 0

    for i in range(n - 1):
        idx_menor = i
        for j in range(i + 1, n):
            comparacoes += 1
            if copia[j] < copia[idx_menor]:
                idx_menor = j
        if idx_menor != i:
            copia[i], copia[idx_menor] = copia[idx_menor], copia[i]
            trocas += 1

    return (copia, comparacoes, trocas)


def insertion_sort(lista):
    """Insira cada proximo valor na posicao certa do trecho ja ordenado.
    Devolve uma copia; nao altera a entrada."""
    copia = list(lista)
    for i in range(1, len(copia)):
        chave = copia[i]
        j = i - 1
        while j >= 0 and copia[j] > chave:
            copia[j + 1] = copia[j]
            j -= 1
        copia[j + 1] = chave
    return copia


def quicksort(lista):
    """(Desafio) Quicksort recursivo, separando menores, iguais e maiores
    que o pivo. Devolve uma copia."""
    if len(lista) <= 1:
        return list(lista)

    pivo = lista[len(lista) // 2]
    menores = [x for x in lista if x < pivo]
    iguais = [x for x in lista if x == pivo]
    maiores = [x for x in lista if x > pivo]

    return quicksort(menores) + iguais + quicksort(maiores)


# ---------- Bloco 2: dois indices e janela ----------

def eh_palindromo(texto):
    """True se a sequencia for igual de tras para frente. Maiusculas e
    espacos contam."""
    sq = 0
    dir = len(texto) - 1

    while esq < dir:
        if texto[esq] != texto[dir]:
            return False
        esq += 1
        dir -= 1

    return True


def par_que_soma(lista, alvo):
    """Lista JA ORDENADA. Dois indices distintos cuja soma e alvo, ou
    (-1, -1). Use dois indices, sem laco dentro de laco."""
    esq = 0
    dir = len(lista) - 1

    while esq < dir:
        soma = lista[esq] + lista[dir]
        if soma == alvo:
            return (esq, dir)
        elif soma < alvo:
            esq += 1
        else:
            dir -= 1

    return (-1, -1)


def remove_repetidos_ordenada(lista):
    """Lista JA ORDENADA. Copia com uma ocorrencia de cada valor."""
    if not lista:
        return []

    resultado = [lista[0]]
    for i in range(1, len(lista)):
        if lista[i] != lista[i - 1]:
            resultado.append(lista[i])

    return resultado


def soma_maxima_janela(lista, k):
    """Maior soma de um trecho consecutivo de tamanho k (1 <= k <= n).
    Atualize a janela sem somar tudo de novo."""
    soma_atual = sum(lista[:k])
    maior_soma = soma_atual

    for i in range(k, len(lista)):
       
        soma_atual += lista[i] - lista[i - k]
        if soma_atual > maior_soma:
            maior_soma = soma_atual

    return maior_soma


def conta_janelas_acima(lista, k, limite):
    """(Desafio) Quantas janelas consecutivas de tamanho k tem soma
    ESTRITAMENTE maior que limite. Atualize a soma em tempo constante."""
    soma_atual = sum(lista[:k])
    contador = 1 if soma_atual > limite else 0

    for i in range(k, len(lista)):
        soma_atual += lista[i] - lista[i - k]
        if soma_atual > limite:
            contador += 1

    return contador

# ---------- Bloco 3: contagem por chave ----------

def conta_frequencias(lista):
    """Dicionario com a frequencia de cada valor."""
    freqs = {}
    for item in lista:
        freqs[item] = freqs.get(item, 0) + 1
    return freqs


def mais_frequente(lista):
    """Valor mais frequente; em empate, o que apareceu primeiro.
    Lista nao vazia."""
    freqs = conta_frequencias(lista)
    melhor_item = lista[0]
    maior_contagem = freqs[melhor_item]

    for item in lista:
        
        if freqs[item] > maior_contagem:
            maior_contagem = freqs[item]
            melhor_item = item

    return melhor_item


def primeiro_unico(lista):
    """Primeiro valor que aparece uma unica vez, ou None. Use dicionario."""
    freqs = conta_frequencias(lista)
    for item in lista:
        if freqs[item] == 1:
            return item
    return None
