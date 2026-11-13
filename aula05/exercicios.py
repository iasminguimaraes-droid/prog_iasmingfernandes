def bubble_sort(lista):
    for fim in range (len(lista) - 1, 0, -1): 
for j in range (fim): 
if lista[j] > lista[j + 1]: 
lista[j], lista[j + 1] = lista[j + 1], lista[j]


def selection_sort(lista):
    a = copiar(lista)
for i in range (len (a) - 1):
menor = i
for j in range (i + 1, len(a)):
if a[j] < a[menor]:
menor = j
a[i], a[menor] = a[menor], a[i]
return a


def insertion_sort(lista):
    a = copiar(lista)
for i in range (1, len(a)):
valor = a[i]
j=i-1
while j >= 0 and a[j] > valor:
a[j + 1] = a[j]
j=j-1
a[j + 1] = valor
return a


def quicksort(lista):
    if len(lista) <= 1:
return copiar(lista)
pivo = lista[len(lista) // 2]
menores = []
iguais = []
maiores = []
for valor in lista:
if valor < pivo:
menores.append(valor)
elif valor > pivo:
maiores.append(valor)
else :
iguais.append(valor)
return quicksort(menores) + iguais + quicksort(maiores)
