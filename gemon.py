"""
Gadiel Tomas Alfonso 44091593
"""
"""
nota1=int(input('ingrese una nota a promediar: '))
nota2=int(input('ingrese otra nota a promediar: '))
nota3=int(input('ingrese otra nota a promediar: '))
notafinal= (nota1+nota2+nota3)/3
print (notafinal)
"""
"""
nombre=str(input('ingrese el nombre del alumno: '))
apellido=str(input('ingrese el apellido del alumno: '))
nroalumno=str(input('ingrese el numero de alumno: '))
comision=str(input('ingrese la comision a la que se desea anotar: '))
print('ls solicitud de inscripcion a la comision ', comision, ' solicitada por el/la alumno/a ', apellido, nombre, ' esta siendo procesada')
"""
"""
palabra1=str(input('ingrese una palabra: '))
palabra2=str(input('ingrese otra palabra: '))
palabra3=str(input('ingrese otra palabra: '))
palabra4=str(input('ingrese otra palabra: '))
palabra5=str(input('ingrese otra palabra: '))
longitud=(len(palabra1)+len(palabra2)+len(palabra3)+len(palabra4)+len(palabra5))
print(longitud)
"""
#Zona de definiciones de funciones
def cargarFraccion():
	numerador=int(input('ingrese el numerador de la fraccion: '))
	denominador=int(input('ingrese el denominador de la fraccion: '))
	x=[numerador, denominador]
	return x
#Solicita al usuario el numerador y denominador. Arma la fraccion como una lista y la retorna
def numeradorFraccion(x):
	return x[0]
print(cargarFraccion())
