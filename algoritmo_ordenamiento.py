def ordenar_burbuja(lista):
    indice_lista_desordenada = 0

    while indice_lista_desordenada < len(lista) - 1:
        contador = len(lista) - 1
        while contador > indice_lista_desordenada:
            if lista[contador] < lista[contador - 1]:
                aux = lista[contador]
                lista[contador] = lista[contador-1]
                lista[contador-1] = aux

            contador = contador - 1
        indice_lista_desordenada = indice_lista_desordenada + 1
    return lista

lista_desordenada = [7, 5, 2, 4, 8, 1, 8, 5, 20, 14]
lista_ordenada = [1, 2, 4, 5, 5, 7, 8, 8, 14, 20]
assert ordenar_burbuja(lista_desordenada) == lista_ordenada