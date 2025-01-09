def merge_sort(lista):
    if len(lista) == 1:
        return lista
    meio = int(len(lista) // 2)
    metade_esquerda = lista[:meio]
    metade_direita = lista[meio:]

    metade_a = merge_sort(metade_esquerda)
    metade_b = merge_sort(metade_direita)

    return merge(metade_a, metade_b)

def merge(metade_a, metade_b):
    i = 0
    j = 0
    lista_mesclada = []
    while i < len(metade_a) and j < len(metade_b):
        if metade_a[i] < metade_b[j]:
            lista_mesclada.append(metade_a[i])
            i = i + 1
        else:
            lista_mesclada.append(metade_b[j])
            j = j + 1

    while i < len(metade_a):
        lista_mesclada.append(metade_a[i])
        i = i + 1

    while j < len(metade_b):
        lista_mesclada.append(metade_b[j])
        j = j + 1

    return lista_mesclada


lista = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
print(merge_sort(lista))