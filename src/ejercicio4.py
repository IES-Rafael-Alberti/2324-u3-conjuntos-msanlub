'''Dadas las siguientes listas:

frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]

    Crea conjuntos a partir de estas listas y nómbralos set_frutas1 y set_frutas2.
    Encuentra las frutas que están en ambas listas y guárdalas en un nuevo conjunto llamado frutas_comunes.
    Encuentra las frutas que están en frutas1 pero no en frutas2 y guárdalas en un conjunto llamado frutas_solo_en_frutas1.
    Encuentra las frutas que están en frutas2 pero no en frutas1 y guárdalas en un conjunto llamado frutas_solo_en_frutas2.
'''

def frutasIguales(setFrutas1:set,setFrutas2:set) -> set:
    '''
    detectamos las frutas repetidas y añadimos un nuevo conjunto

    parameters
    ----------
    setFrutas1(set): conjunto de frutas 1
    setFrutas2(set): conjunto de frutas 2
    
    Returns
    -------
    devuelve el conjunto nuevo de frutas repetidas    
    
    '''

    frutasComunes = set()
    frutasComunes = setFrutas1 & setFrutas2
    return frutasComunes

def frutasDesigualesEnUno(setFrutas1:list,setFrutas2:list) -> set:
    '''
    detectamos las frutas que no se repiten

    parameters
    ----------
    setFrutas1(set): conjunto de frutas 1
    setFrutas2(set): conjunto de frutas 2
    
    Returns
    -------
    devuelve el conjunto nuevo de frutas que no se repiten en el uno
    
    '''

    frutasSoloEnFrutas1 = set()
    frutasSoloEnFrutas1 = setFrutas1 - setFrutas2
    return frutasSoloEnFrutas1

def frutasDesigualesEnDos(setFrutas1:list,setFrutas2:list) -> set:
    '''
    detectamos las frutas que no se repiten

    parameters
    ----------
    setFrutas1(set): conjunto de frutas 1
    setFrutas2(set): conjunto de frutas 2
    
    Returns
    -------
    devuelve el conjunto nuevo de frutas que no se repiten en el dos
    
    '''

    frutasSoloEnFrutas2 = set()
    frutasSoloEnFrutas2 = setFrutas2 - setFrutas1
    return frutasSoloEnFrutas2

def main():
    '''programa principal'''
    #entrada
    frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
    frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]
    setFrutas1 = set(frutas1)
    setFrutas2 = set(frutas2)
    
    #proceso y salida
    print("Crea conjuntos a partir de estas listas y nómbralos set_frutas1 y set_frutas2: " + str(setFrutas1) + str(setFrutas2))
    print("Encuentra las frutas que están en ambas listas y guárdalas en un nuevo conjunto llamado frutas_comunes: " + str(frutasIguales(setFrutas1,setFrutas2)))
    print("Encuentra las frutas que están en frutas1 pero no en frutas2 y guárdalas en un conjunto llamado frutas_solo_en_frutas1: " + str(frutasDesigualesEnUno(setFrutas1,setFrutas2)))
    print("Encuentra las frutas que están en frutas2 pero no en frutas1 y guárdalas en un conjunto llamado frutas_solo_en_frutas2: " + str(frutasDesigualesEnDos(setFrutas1,setFrutas2)))

if __name__=="__main__":
    main()