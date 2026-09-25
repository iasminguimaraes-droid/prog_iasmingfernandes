"""Aula 01 - De C para Python.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.
"""


def soma_lista(lista):
 soma = 0
    for numero in lista:
        soma += numero
        return soma


def conta_pares(lista):
  contador = 0
  for num in lista:
    if num % 2 == 0:
      contador += 1
  return contador



def maior_valor(lista):
    maior = lista[0]
    for numero in lista:
        if numero > maior:
            maior = numero  
    return maior

  

def existe(lista, alvo):
    for elemento in lista:
        if elemento == alvo:
            return True  
    return False  


def busca_linear(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i  
    return -1 



def segundo_maior(lista):
  if len(lista) < 2:
    return None
  maior = float('-inf')
  segundo = float('-inf')
  for num in lista:
    if num > maior:
      segundo = maior
      maior = num
    elif num > segundo and num != maior:
      segundo = num
  if segundo == float('-inf'):
    return None
  return segundo
