import tkinter as tk
import math

# Función para evaluar la expresión y mostrar el resultado
def calcular():
    try:
        expresion = entrada.get()
        resultado = eval(expresion)
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except Exception as e:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Error")

# Funciones científicas
def sin():
    entrada.insert(tk.END, "math.sin(")

def cos():
    entrada.insert(tk.END, "math.cos(")

def tan():
    entrada.insert(tk.END, "math.tan(")

def sqrt():
    entrada.insert(tk.END, "math.sqrt(")

# Crear una ventana
ventana = tk.Tk()
ventana.title("Calculadora Científica")

# Crear una caja de entrada (Entry)
entrada = tk.Entry(ventana, width=30)
entrada.grid(row=0, column=0, columnspan=5)

# Botones para números y operaciones
botones = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

fila, columna = 1, 0
for boton_texto in botones:
    tk.Button(ventana, text=boton_texto, width=7, height=2, command=lambda b=boton_texto: entrada.insert(tk.END, b)).grid(row=fila, column=columna)
    columna += 1
    if columna > 3:
        columna = 0
        fila += 1

# Botones para funciones científicas
tk.Button(ventana, text="senos", width=7, height=2, command=sin).grid(row=1, column=5)
tk.Button(ventana, text="culos", width=7, height=2, command=cos).grid(row=2, column=5)
tk.Button(ventana, text="tetas", width=7, height=2, command=tan).grid(row=3, column=5)
tk.Button(ventana, text="squirt", width=7, height=2, command=sqrt).grid(row=4, column=5)

# Botón para calcular
tk.Button(ventana, text="=", width=7, height=2, command=calcular).grid(row=5, column=5)

ventana.mainloop()
