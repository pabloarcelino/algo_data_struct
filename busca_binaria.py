def busca_binaria(lista, alvo, inicio, fim):
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1


lista = [1, 3, 5, 7, 9]
alvo = 5
inicio = 0
fim = len(lista) - 1
print(busca_binaria(lista, alvo, inicio, fim))