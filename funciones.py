"""
def cuantas_vocales(texto):
    vocales=0
    for x in texto:
        if x.lower() =='a' or x.lower() =='e' or x.lower() =='i' or x.lower() =='o' or x.lower() =='u':
            vocales+=1
    return vocales

def generar_lista():
    lista=[]
    palabra=input('ingrese una palabra para agregar a la lista. La carga termina al igresar la palabra "fin": ')
    while palabra != 'fin':
        lista.append ([palabra, cuantas_vocales(palabra)])
        palabra=input('ingrese una palabra para agregar a la lista. La carga termina al igresar la palabra "fin": ')
    return lista

def mas_de_tres(lista):
    for x in lista:
        if x[1] >= 3:
            print (x[0])
"""

"""
def controlar_equipos():
    liga=[]
    equipos=input('ingrese el nombre del equipo. Para concluir la carga ingrese "999": ')
    while equipos!='999':
        puntaje=input('ingrese el puntaje del equipo: ')
        goles=input('ingrese los goles a favor que tenga el equipo: ')
        liga.append([equipos, puntaje, goles])
        equipos=input('ingrese el nombre del equipo. Para concluir la carga ingrese "999": ')
    return liga
"""
#Ejercicio 3:
"""
def cargar_datos_alumno():
    base_datos=[]
    legajo=int(input('ingrese el numero de legajo. la carga termina cuando ingrese el nº 0: '))
    while legajo != 0:
        nombre=input('ingrese el nombre del alumno: ')
        apellido=input('ingrese el apellido del alumno: ')
        contraseña=input('ingrese la contraseña: ')
        base_datos.append([legajo, nombre, apellido, contraseña])
        legajo=int(input('ingrese el numero de legajo. la carga termina cuando ingrese el nº 0: '))
    return base_datos


def imprimir_alumno(lista_de_alumnos):  
    print('LEGAJO: ' , lista_de_alumnos[0])   
    print('NOMBRE: ' , lista_de_alumnos[1])   
    print('APELLIDO: ' , lista_de_alumnos[2])
    print('CONTRASEÑA: ' , lista_de_alumnos[3])

def legajo_menor(lista):
    menor=lista[0][0]
    for alumno in lista:
        if alumno[0]<menor:
            menor=alumno[0]
            alumnito=alumno
    return alumnito

def nombre_mas_largo(lista):
    nombre_largo=''
    nombre_mas_large=''
    for alumno in lista:
        if len(alumno[1])>=len(nombre_largo):
            nombre_largo=alumno[1]
            nombre_mas_large=alumno
    return nombre_mas_large


def controlar_clave(alumno):
    numeros='1234567890'
    if alumno[-1][-1] in numeros and len(alumno[-1])>=6:
        print(alumno)
    elif alumno[-1][-1] in numeros and len(alumno[-1])<6:
        print('la contraseña tiene menos de 6 caracteres')
    elif alumno[-1][-1] not in numeros and len(alumno[-1])>=6:
        print ('la contraseña no termina con un numero')
    else:
        print('la contraseña no cumple ninguna de las 2 condiciones')

def verificar_claves(lista):
    for alumno in lista:
        print ('el alumno', alumno[1],alumno[2])
        controlar_clave(alumno)

    
def opciones():
    print('seleccione una opcion: ')
    print('(1) imprimir los datos de todos los alumnos')
    print('(2) imprimir los datos del alumno que tiene el legajo más chico')
    print('(3) imprimir los datos del alumno que tiene el nombre más largo')
    print('(4) Imprimir si las contraseñas de cada alumno cumplen con un tamaño mayor a 6 caracteres y terminan con un número')
    print('(0) salir del menu')
    print()


lista_de_alumnos=cargar_datos_alumno()
opciones()
opcion=input('ingrese una de las opciones: ')
while opcion!='0':
    if opcion=='1':
        for alumno in lista_de_alumnos:
            print()
            imprimir_alumno(alumno)
            print()
    elif opcion=='2':
        print (legajo_menor(lista_de_alumnos))
    elif opcion=='3':
        print(nombre_mas_largo(lista_de_alumnos))
    elif opcion=='4':
        verificar_claves(lista_de_alumnos)
    else:
        print('la entrada no es valida, vuelva a intentarlo:')
    print()
    opciones()
    opcion=input('ingrese una de las opciones: ')
    
    """

#Ejercicio 6

def longitud_de_texto(texto):
    longitud=len(texto)
    return longitud

def cantidad_de_palabras(texto):
    palabras=1
    palabra=' '
    for x in texto:
        if x == palabra:
            palabras+=1
    return palabras

def cantidad_de_oraciones(texto):
    oraciones=0
    oracion='.'
    for x in texto:
        if x == oracion:
            oraciones+=1
    return oraciones

def comienzan_con_vocal(texto):
    vocales='aeiou'
    contador=0
    for x in texto:
        if x in vocales:
            contador+=1
    return contador


texto=input('ingrese el texto: ')
print(comienzan_con_vocal(texto))
