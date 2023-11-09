#Gadiel Alfonso
#44091593
dia_de_semana=['Domingo','Lunes','Martes','Miercoles','Jueves','Viernes','Sabado']
def que_dia_es():
    dia=int(input('ingrese un numero del 1 al 7: '))
    if dia<=7 and dia>=1:
        return(dia_de_semana[dia-1])
    else:
        return ('el valor ingresado no esta dentro del rango')
print (que_dia_es())