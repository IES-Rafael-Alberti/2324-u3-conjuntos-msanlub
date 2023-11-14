'''Solicitar al usuario que introduzca los nombres de pila de los alumnos de primaria de una escuela, finalizando cuando se introduzca “x”. A continuación, solicitar que introduzca los nombres de los alumnos de secundaria, finalizando al introducir “x”.

    Mostrar los nombres de todos los alumnos de primaria y los de secundaria, sin repeticiones.
    Mostrar qué nombres se repiten entre los alumnos de primaria y secundaria.
    Mostrar qué nombres de primaria no se repiten en los de nivel secundaria.
    Mostrar si todos los nombres de primaria están incluidos en secundaria.
'''

def nombreTodosLosAlumnos(primaria:set,secundaria:set) -> set:
    '''Une los dos conjuntos de nombres de alumnos de primaria y secundaria
    
    parameters
    ----------
    primaria(set): conjunto de alumnos de primaria
    secundaria(set): conjunto de alumnos de secundaria
    
    returns
    -------
    devuelve la unión de primaria y secundaria
    '''

    return primaria | secundaria

def nombreRepetidos(primaria:set,secundaria:set) -> set:
    ''' devuelve los elementos que se repiten en primaria y secundaria
    
    parameters
    ----------
    primaria(set): conjunto de alumnos de primaria
    secundaria(set): conjunto de alumnos de secundaria
    
    returns
    -------
    devuelve los nombres que se repiten de primaria y secundaria
    '''

    return primaria & secundaria

def nombreNoRepetidos(primaria:set,secundaria:set) -> set:
    ''' devuelve los elementos que no se repiten de primaria en secundaria
    
    parameters
    ----------
    primaria(set): conjunto de alumnos de primaria
    secundaria(set): conjunto de alumnos de secundaria
    
    returns
    -------
    devuelve los nombres que no se repiten de primaria en secundaria
    '''

    return primaria - secundaria

def nombreIncluidos(primaria:set,secundaria:set) -> set:
    ''' 
    controla si todos los nombres de primaria están incluidos en secundaria.

    parameters
    ----------
    primaria(set): conjunto de alumnos de primaria
    secundaria(set): conjunto de alumnos de secundaria
    
    returns
    -------
    devuelve True si todos los nombres de primaria están incluidos en secundaria y False si no.
    '''

    return primaria <= secundaria

def main():
    '''programa principal'''
    #entrada
    FIN = "x"
    alumnoPrimaria = ""
    alumnoSecundaria = ""
    primaria = set()
    secundaria = set()

    while alumnoPrimaria != FIN:
        alumnoPrimaria = input("Indica el nombre del alumno de primaria: ")
        if alumnoPrimaria != FIN:
            primaria.add(alumnoPrimaria)
    print("Fin.")

    while alumnoSecundaria != FIN:
        alumnoSecundaria = input("Indica el nombre del alumno de secundaria: ")
        if alumnoSecundaria != FIN:
            secundaria.add(alumnoSecundaria)
    print("Fin.")

    #proceso y salida
    print("Mostrar los nombres de todos los alumnos de primaria y los de secundaria, sin repeticiones: " + str(nombreTodosLosAlumnos(primaria,secundaria)))
    print("Mostrar qué nombres se repiten entre los alumnos de primaria y secundaria: " + str(nombreRepetidos(primaria,secundaria)))
    print("Mostrar qué nombres de primaria no se repiten en los de nivel secundaria: " + str(nombreNoRepetidos(primaria,secundaria)))
    if nombreIncluidos(primaria,secundaria) == True:
        print("Mostrar si todos los nombres de primaria están incluidos en secundaria: Sí están incluidos.")
    else:
        print("Mostrar si todos los nombres de primaria están incluidos en secundaria: No están incluidos.")



if __name__=="__main__":
    main()