"""
# Función para realizar una suma
def suma(a, b):
    return a + b

# Función para realizar una resta
def resta(a, b):
    return a - b

# Función para realizar una multiplicación
def multiplicacion(a, b):
    return a * b

# Función para realizar una división
def division(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a / b

# Función principal de la calculadora
def calculadora():
    while True:
        print("Opciones:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        opcion = input("Seleccione una opción (1/2/3/4/5): ")

        if opcion == "5":
            print("¡Hasta luego!")
            break

        if opcion not in ("1", "2", "3", "4"):
            print("Opción no válida. Intente nuevamente.")
            continue

        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if opcion == "1":
            resultado = suma(num1, num2)
            print(f"Resultado: {resultado}")
        elif opcion == "2":
            resultado = resta(num1, num2)
            print(f"Resultado: {resultado}")
        elif opcion == "3":
            resultado = multiplicacion(num1, num2)
            print(f"Resultado: {resultado}")
        elif opcion == "4":
            resultado = division(num1, num2)
            print(f"Resultado: {resultado}")

# Iniciar la calculadora
calculadora()
"""
import tkinter as tk

def realizar_operacion():
    num1 = float(entrada_num1.get())
    num2 =float(entrada_num2.get())
    operacion = operacion_var.get()

    if operacion == "Suma":
        resultado = num1 + num2
    elif operacion == "Resta":
        resultado = num1 - num2
    elif operacion == "Multiplicación":
        resultado = num1 * num2
    elif operacion == "División":
        if num2 == 0:
            resultado = "Error: No se puede dividir por cero"
        else:
            resultado = num1 / num2
    else:
        resultado = "Operación no válida"

    etiqueta_resultado.config(text=f"Resultado: {resultado}")

# Crear una ventana
ventana = tk.Tk()
ventana.title("Calculadora")

# Etiqueta e input para el primer número
etiqueta_num1 = tk.Label(ventana, text="Primer número:")
etiqueta_num1.pack()
entrada_num1 = tk.Entry(ventana)
entrada_num1.pack()

# Etiqueta e input para el segundo número
etiqueta_num2 = tk.Label(ventana, text="Segundo número:")
etiqueta_num2.pack()
entrada_num2 = tk.Entry(ventana)
entrada_num2.pack()

# Menú desplegable para seleccionar la operación
operacion_var = tk.StringVar()
operacion_var.set("Suma")  # Valor predeterminado
etiqueta_operacion = tk.Label(ventana, text="Selecciona una operación:")
etiqueta_operacion.pack()
menu_operacion = tk.OptionMenu(ventana, operacion_var, "Suma", "Resta", "Multiplicación", "División")
menu_operacion.pack()

# Botón para realizar la operación
boton_calcular = tk.Button(ventana, text="Calcular", command=realizar_operacion)
boton_calcular.pack()

# Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack()

# Iniciar la aplicación
ventana.mainloop()
