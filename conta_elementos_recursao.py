def conta_elementos(lista):

    if not lista:
        return 0
    else:
        return 1 + conta_elementos(lista[1:])
    
lista = [2, 4, 74, 20, 1, 3]

print(conta_elementos(lista))
    
