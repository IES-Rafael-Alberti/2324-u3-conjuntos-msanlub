'''El conjunto potencia de un conjunto S es el conjunto de todos los subconjuntos de S.

Por ejemplo, el conjunto potencia de {1,2,3} es:

{∅,{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}}

Escriba la función conjunto_potencia(s) que reciba como parámetro un conjunto cualquiera s y retorne su «lista potencia» (la lista de todos sus subconjuntos):


def conjuntoPotencias(s:set) :
    algoritmo que da la lista potencia del conjunto
    
    Parameters
    ----------
    s(set): conjunto
    
    returns
    -------
    devuelve la lista potencia del conjunto



def main():
    s = set({1,2,3,4})

    listaPotencia = {set(), set(1),set(2),set(3),set(4),set(1,2),set(2,3),set(3,4),set(1,3),set(1,4),set(2,4),set(1,2,3),set(2,3,4),set(1,3,4),set(1,2,4),set(1,2,3,4)}

    return listaPotencia

if __name__=="__main__":
    main()
'''
