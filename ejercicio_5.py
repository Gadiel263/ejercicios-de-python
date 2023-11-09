destinos=['Bariloche', 'Chilecito', 'Rosario', 'Salta', 'Tilcara', 'Pumamarca']
def agregarDestino(nuevo_destino):
    destinos.append(nuevo_destino)
    return destinos
x=input('ingrese un nuevo destino: ')
print(agregarDestino(x))
