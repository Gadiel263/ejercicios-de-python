#administrar Kiosco

productos=[[100,'galletas', 'jorgito', 200, 15, False], [102,'bebidas', 'cocacola', 700, 20, True]]

def mostrar_productos(tipo):
    productipos=[]
    for x in productos:
        if x[1].lower()==tipo.lower():
            productipos.append(x)
    return productipos

def prod_sin_stock():
    sin_stock=[]
    for x in productos:
        if x[4]==0:
            sin_stock.append(x)
    return sin_stock

def mayores_650_y_refrigeracion():
    cumplen=[]
    for x in productos:
        if x[3]>650 and x[-1]==True:
            cumplen.append(x)
    return cumplen


print(mayores_650_y_refrigeracion())