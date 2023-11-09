#Gadiel Alfonso
#44091593
def cargarFraccion():
	numerador=int(input('Ingrese el numerador: '))
	denominador=int(input('Ingrese el denominador: '))
	return [numerador,denominador]
def numeradorFraccion(x):
	return x[0]
def denominadorFraccion(x):
	return x[1]
def sumaFracciones(x,y):
	denominadorComun=x[1]*y[1]
	sumaNumerador=(x[0]*y[1])+(y[0]*x[1])
	return[sumaNumerador,denominadorComun]
def restaFracciones(x,y):
	denominadorComun=x[1]*y[1]
	restaNumerador=(x[0]*y[1])-(y[0]*x[1])
	return[restaNumerador,denominadorComun]
def divisionFracciones(x,y):
	divisionNumerador=x[0]*y[1]
	divisionDenominador=x[1]*y[0]
	return [divisionNumerador,divisionDenominador]
def multiplicacionFracciones(x,y):
	multiplicacionNominador=x[0]*y[0]
	multiplicacionDenominador=x[1]*y[1]
	return [multiplicacionNominador,multiplicacionDenominador]
print('Bienvenidos/as a cuentas con Fracciones')
print('Agregue los datos de la primera fraccion')
x=cargarFraccion()
print('Agregue los datos de la segunda fraccion')
y=cargarFraccion()
print ('El numerador de la primera fraccion es:',numeradorFraccion(x))
print ('El denominador de la primera fraccion es:',denominadorFraccion(x))
print ('El numerador de la segunda fraccion es:',numeradorFraccion(y))
print ('El denominador de la segunda fraccion es:',denominadorFraccion(y))
print ('La suma de dichas fracciones es:',sumaFracciones(x,y))
print ('La resta de dichas fracciones es:', restaFracciones(x,y))
print ('La multiplicacion de dichas fracciones es:', multiplicacionFracciones(x,y))
print ('La division de dichas fracciones es:', divisionFracciones(x,y))
#Gadiel Alfonso
#44091593