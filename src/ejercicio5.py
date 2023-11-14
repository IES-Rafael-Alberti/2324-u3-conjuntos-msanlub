'''
Dado el conjunto de números enteros:

numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

Crea un conjunto pares que contenga los números pares del conjunto numeros.
Crea un conjunto multiplos_de_tres que contenga los números que son múltiplos de tres del conjunto numeros.
Encuentra la intersección entre los conjuntos pares y multiplos_de_tres y guárdala en un conjunto llamado pares_y_multiplos_de_tres.
'''

def pares(numeros:set) -> set:
    '''
    crea un conjunto con los numeros par

    parameters
    ----------
    numeros(set): conjunto de numeros

    returns
    -------
    devuelve el conjunto de números par.
    '''

    numerosPar = set()
    for numero in numeros:
        if numero % 2 == 0:
            numerosPar.add(numero)
    return numerosPar

def multiploTres(numeros:set) -> set:
    '''
    crea un conjunto con los numeros multiplos de tres

    parameters
    ----------
    numeros(set): conjunto de numeros

    returns
    -------
    devuelve el conjunto de números multiplos de tres.
    '''

    numerosMultiplosTres = set()
    for numero in numeros:
        if numero % 3 == 0:
            numerosMultiplosTres.add(numero)
    return numerosMultiplosTres

def interseccion(numeroPar:set,numeroMultiploDeTres:set):
    '''
    crea un conjunto con los numeros de la interseccion entre ambos conjuntos

    parameters
    ----------
    numeroPar(set): conjunto de numeros pares
    numeroMultiploDeTres(set): conjunto de numeros multiplos de tres

    returns
    -------
    devuelve el conjunto de numeros que se repiten en numeroPar y numeroMultiploDeTres.
    '''

    pares_y_multiplos_de_tres = numeroPar & numeroMultiploDeTres
    return pares_y_multiplos_de_tres

def main():
    '''programa principal'''
    #entrada
    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    #proceso
    numeroPar = pares(numeros)
    numeroMultiploDeTres = multiploTres(numeros)
    paresYMultiplosDeTres = interseccion(numeroPar,numeroMultiploDeTres)
    #salida
    print("Crea un conjunto pares que contenga los números pares del conjunto numeros: " + str(numeroPar))
    print("Crea un conjunto multiplos_de_tres que contenga los números que son múltiplos de tres del conjunto numeros: " + str(numeroMultiploDeTres))
    print("Encuentra la intersección entre los conjuntos pares y multiplos_de_tres y guárdala en un conjunto llamado pares_y_multiplos_de_tres: " + str(paresYMultiplosDeTres))

if __name__=="__main__":
    main()