import tkinter
from tkinter import messagebox
import webbrowser

# Funciones para los botones
def boton1():
    messagebox.showinfo(title="Boton1", message ="¡Este es un mensaje de alerta por oprimir el boton 1!")# abrir ventana emergende de información

def boton2():
    url='https://www.youtube.com/watch?v=DSoSQau24cQ' # guardar url en una variable
    webbrowser.open(url) #navegar hasta la url

ventana = tkinter.Tk() 
ventana.title('mi ventana')
ventana.geometry("400x350")  # dar más amplitud a la interfaz
ventana.config(bg='purple')
#ventana.iconbitmap('colibri.ico')

# Con GRID se puede convertir la ventana en una matriz
# Repartir la ventana en 4 partes utilizando 2 filas y 2 columnas
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)
ventana.grid_rowconfigure(0, weight=1)
ventana.grid_rowconfigure(1, weight=1)

# ordenar el código
frame1 = tkinter.Frame(ventana)  # crea un objeto de la clase frame
frame1.configure(bd=6, bg='aqua')
frame2 = tkinter.Frame(ventana)
frame2.configure(bd=6, bg='thistle')
frame3 = tkinter.Frame(ventana)
frame3.configure(bd=6, bg='red')
frame4 = tkinter.Frame(ventana)
frame4.configure(bd=6, bg='blue')

# boton1
button1 = tkinter.Button(frame3, text='generar alerta', command=boton1)
button1.pack(side='bottom', pady=5)
# etiquetas
label1 = tkinter.Label(frame3, text='¡Precaución!', bg='white')
label1.pack(side='bottom', pady=5)
label2 = tkinter.Label(frame4, text='Mirar', bg='white')
label2.pack(side='left', pady=10)
# boton2
button2 = tkinter.Button(frame4, text='ver video', command=boton2)
button2.pack(side='left', pady=10)

# primero se llaman los frames y luego la ventana
frame1.grid(row=0, column=0, sticky="nsew")  # se ve dentro de la ventana y se le da a cada frame una ubicación
frame2.grid(row=0, column=1, sticky="nsew") # Con sticky="nsew" el frame ocupa todo el espacio asignado en la ventana
frame3.grid(row=1, column=0, sticky="nsew")
frame4.grid(row=1, column=1, sticky="nsew")

ventana.mainloop()  # lleva registro de lo que sucede en la ventana. bucle infinito




# Referencia
# https://adictosaltrabajo.com/2020/06/30/interfaces-graficas-en-python-con-tkinter/
# https://farwebs.es/programacion/como-utilizar-los-grids-en-tkinter/
# https://recursospython.com/guias-y-manuales/cuadros-de-dialogo-messagebox-en-tkinter/
