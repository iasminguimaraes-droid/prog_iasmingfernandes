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
  tabela = [[] for _ in range(tamanho)]

  for palavra in palavras:
    indice = sum(ord(letra) for letra in palavra) % tamanho
    if palavra not in tabela[indice]:
      tabela[indice].append(palavra)

  return tabela


lista_palavras = ["casa", "saca", "bola", "gato", "toga", "sol"]
resultado = gavetas_com_colisao(lista_palavras, 5)

for i, gaveta in enumerate(resultado):
  print(f"Gaveta {i}: {gaveta}")


def mais_frequente(lista):
  if not lista:
    return None

  contagem = {}
  for item in lista:
    contagem[item] = contagem.get(item, 0) + 1

  return max(contagem, key=contagem.get)
