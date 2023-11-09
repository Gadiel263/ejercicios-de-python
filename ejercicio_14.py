#Gadiel Alfonso
#44091593
def pulsasiones(edad,entrena):
    if entrena=='si' or entrena =='sí':
        return (210-edad)/10
    elif entrena=='no':
        return (220-edad)/10
    else:
        return 'la entreada no es valida'
años=int(input('ingrese la edad: '))
se_ejercita=input('se ejercita?: ')
print (pulsasiones(años,se_ejercita.lower()))