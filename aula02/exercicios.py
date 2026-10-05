"""Aula 02 - Listas em Python.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.
"""


def remove_negativos(lista):
    return [numero for numero in lista if numero >= 0]


def inverte(lista):
    nova_lista = []
    for i in range(len(lista) - 1, -1, -1):
        nova_lista.append(lista[i])
    return nova_lista



def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1  


def intercala(lista_a, lista_b):
    lista_intercalada = []
    
    for i in range(len(lista_a)):
        lista_intercalada.append(lista_a[i])
        lista_intercalada.append(lista_b[i])
        
    return lista_intercalada


def remove_repetidos(lista):
 
