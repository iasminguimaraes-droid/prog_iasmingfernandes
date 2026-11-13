def conta_frequencias(lista):
    frequencias = {}
for item in lista:
if item in frequencias:
frequencias[item] = frequencias[item] + 1
else :
frequencias[item] = 1
return frequencias


def hash_soma(palavra, tamanho):
    total = 0
for letra in palavra:
total = total + ord (letra)
return total % tamanho


def gavetas_com_colisao(palavras, tamanho):
    pass


def mais_frequente(lista):
    pass
