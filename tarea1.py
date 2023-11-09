def armar_lista():
    lista=[]
    numero=int(input('agregar un numero a la lista: '))
    while numero != 0:
        lista.append (numero)
        numero=int(input('agregar un numero a la lista: '))
    return (lista)

def promedio_lista(lista):
    suma=0
    cantidad=len(lista)
    for numero in lista:
        suma+=numero
    return (suma / cantidad)

def suma_lista(lista):
    suma=0
    for numero in lista:
        suma+=numero
    return suma 

def calcular_maximo(lista):
    maximo=lista[0]
    for numero in lista:
        if numero>maximo:
            maximo=numero
        else :
            maximo=maximo
    return maximo

def calcular_minimo(lista):
    minimo=lista[0]
    for numero in lista:
        if numero<minimo:
            minimo=numero
        else :
            minimo=minimo
    return minimo

def porcentaje(total,valor):
    porcentaje=(valor*100)/total
    return porcentaje

def opciones():
    print('1. Ver el promedio de los números')
    print('2. Ver la suma de los números')
    print('3. Ver la cantidad de números')
    print('4. Ver el número máximo')
    print('5. Ver el número mínimo')
    print('6. Calcular porcentaje')
    print('7. Salir')

lista_numeros=armar_lista()
opciones()
eleccion=int(input('elija una de las opciones: '))
while eleccion!=7:
    if eleccion==1:
        print(promedio_lista(lista_numeros))
    elif eleccion==2:
      print(suma_lista(lista_numeros))
    elif eleccion==3:
      print(len(lista_numeros))
    elif eleccion==4:
        print(calcular_maximo(lista_numeros))
    elif eleccion==5:
        print(calcular_minimo(lista_numeros))
    elif eleccion==6:
        total=int(input('ingrese el total: '))
        valor=int(input('ingrese el valor para calcular el porcentaje con respecto al total: '))
        print(porcentaje(total, valor))
    else:
        print ('la entrada no es valida')
    opciones()
    eleccion=int(input('elija una de las opciones: '))
    


    