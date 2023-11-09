#Nos contratan para realizar un sistema para una editorial. Se recibe un texto y se desea obtener la siguiente información:
texto= 'Tengo 1 perro muy lindo. Mi perro se llama Carlitos. En las vacasiones, yo y mi perro paseamos por 8 horas. El ama correr. A mi perro le gusta comer carne.'
# La longitud total del texto.

def longitud_de_texto(texto):
    longitud=len(texto)
    return longitud

# La cantidad de palabras que componen el texto.

def cantidad_de_palabras(texto):
    palabras=texto.split()
    cantidad=len(palabras)
    return cantidad

# La cantidad de oraciones que componen el texto.

def cantidad_de_oraciones(texto):
    cantidad=0
    for x in texto:
        if x == '.':
            cantidad+=1
    return cantidad

# La cantidad de palabras que comienzan con vocal o con consonante, dependiendo del valor ingresado por el usuario.

def cuantas_con_vocal(texto):
    palabras=texto.split()
    vocales='aeiouAEIOU'
    contador=0
    for palabra in palabras:
        if palabra[0] in vocales:
            contador+=1
    return contador

def cuantas_con_consonante(texto):
    palabras=texto.split()
    consonantes='bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ'
    contador=0
    for palabra in palabras:
        if palabra[0].lower() in consonantes:
            contador+=1
    return contador

# Buscar una palabra ingresada por el usuario y retornar la cantidad de veces que se encuentra en el texto.

def buscar_palabra(texto, palabra):
    palabras=texto.split()
    contador=0
    for x in palabras:
        if x.lower() == palabra.lower():
            contador+=1
    return contador

# La cantidad de palabras que comienzan con mayúscula.

def cuantas_con_mayus(texto):
    palabras=texto.split()
    contador=0
    mayusculas='ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    for x in palabras:
        if x[0]in mayusculas:
            contador+=1
    return contador

# La cantidad de caracteres que son números.

def cuantos_num(texto):
    numeros='1234567890'
    contador=0
    for x in texto:
        if x in numeros:
            contador += 1
    return contador

# La cantidad de palabras que comienzan con vocal y la cantidad de palabras que comienzan con consonante.

# Imprimir todas las palabras que terminan en infinitivo (terminadas en ar er o ir).

def palabras_en_infinitivo(texto):
    palabras=texto.split()
    infinitivos= ['ar','er','ir']
    palabras_infinit=[]
    for palabra in palabras:
        if palabra[-2:] in infinitivos:
            palabras_infinit.append(palabra)
    print (palabras_infinit)

def opciones():
    print('1) saber la cantidad de caracteres total del texto ')
    print('2) saber la cantidad de palabras del texto')
    print('3) saber la cantidad de oraciones del texto')
    print('4) saber cuantas palabras comienzan con vocal y cuantas con consonante')
    print('5) buscar cuantas veces aparece una palabra en el texto')
    print('6) saber cuantas palabras comienzan con mayuscula')
    print('7) saber cuantos caracteres son numeros ')  
    print('0) cerrar programa')


texto=input('ingrese el texto a analizar: ')
opciones()
opcion=input('ingrese una opcion: ')
while opcion!='0':
    if opcion == '1':
        print('el texto contiene ', longitud_de_texto(texto), ' caracteres en total')
    elif opcion=='2':
        print('El texto contiene ', cantidad_de_palabras(texto),' palabras en total')
    elif opcion=='3':
        print('el texto contiene ',cantidad_de_oraciones(texto),' oraciones')
    elif opcion=='4':
        print('1) saber cuantas palabras comienzan con vocal')
        print('2) saber cuantas palabras comienzan con consonante')
        print('3) saber cuantas palabras comienzan con vocal y consonante')
        seleccion=input('seleccione la accion que desea realizar: ')
        if seleccion=='1':
            print('el texto contiene', cuantas_con_vocal(texto), 'palabras que comienzan con vocal')
        elif seleccion=='2':
            print('el texto contiene', cuantas_con_consonante(texto), 'palabras que comienzan con consonante')
        elif seleccion=='3':
            print('el texto contiene', cuantas_con_vocal(texto), 'palabras que comienzan con vocal')
            print('el texto contiene', cuantas_con_consonante(texto), 'palabras que comienzan con consonante')
        else :
            print('la entrada no es valida')
    elif opcion=='5':
        palabra_a_buscar=input('ingrese la palabra que quiere buscar: ')
        print ('la palabra aparece ', buscar_palabra(texto, palabra_a_buscar), 'veces en el texto')
    elif opcion=='6':
        print('en el texto ', cuantas_con_mayus(texto), ' palabras comienzan con mayuscula')
    elif opcion== '7':
        print('el texto contiene ', cuantos_num(texto), ' caracteres que son numeros')
    else:
        print('la entrada no es valida, vuelva a intentarlo.')
    opciones()
    opcion=input('ingrese una opcion: ')



