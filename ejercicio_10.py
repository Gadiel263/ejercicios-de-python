#Gadiel Alfonso
#44091593
def es_triangulo():
    a=int(input('ingrese una longitud: '))
    b=int(input('ingrese otra longitud: '))
    c=int(input('ingrese otra longitud: '))
    if a+b>c and a+c>b and b+c>a:
        return ('se forma un triangulo')
    else:
        return ('no se forma un triangulo')
print (es_triangulo())