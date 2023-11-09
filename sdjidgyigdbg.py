
colores_calidos=('rojo','naranja','amarillo')
colores_frios=('azul','celeste','violeta','verde')
colores_primarios=('rojo','azul','amarillo')
colores_secundarios=('naranja','violeta','verde')
def es_calido(color2):
    if color2 in colores_calidos:
        return 'es calido'
    elif color2 in colores_frios:
        return 'es frio'
    else:
        return 'no es frio ni calido'
def es_primario(color1):
    if color1 in colores_primarios:
        return 'es primario'
    elif color1 in colores_secundarios:
        return 'es secundario'
    else:
        return 'no es primario ni secundario'
x=input('ingresa un color: ')
print (es_calido(x),' y ',es_primario(x))
