'''
Dado el conjunto de letras:

vocales = {'a', 'e', 'i', 'o', 'u'}

    Crea un conjunto consonantes que contenga las letras del alfabeto que no son vocales.
    Crea un conjunto letras_comunes que contenga las letras que están tanto en el conjunto vocales como en el conjunto consonantes.
'''

def unir(vocales:set,letras_consonantes:set) ->set:
    '''
    unión de dos conjuntos
    
    parameters
    ----------
    vocales(set): conjunto de vocales
    letras_consonantes(set): conjunto de consonantes
    
    Returns
    -------
    devuelve el conjunto de vocales y consonantes.
    '''
    letras_comunes = set()
    letras_comunes = vocales | letras_consonantes
    return letras_comunes


def main():
    #entrada
    vocales = {'a', 'e', 'i', 'o', 'u'}
    letras_consonantes = {'b','c','d','f','g','h','j','k','l','m','n','ñ','p','q','r','s','t','v','w','x','y','z'}
    #proceso
    union = unir(vocales,letras_consonantes)
    #salida
    print(union)

if __name__=="__main__":
    main()