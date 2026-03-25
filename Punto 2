import tkinter as tk
from tkinter import messagebox
import time
from collections import deque
#isEmpty() len(pila) == 0 Verifica si está vacía
#push(objeto) append(objeto) Agrega a la cima de la pila
class tarea:
    def __init__(self,tarea1,tiempoxtar):
        self.tarea1=tarea1
        self.tiempoxtar=tiempoxtar
pila=[]
procesando = False
ventana=tk.Tk()
ventana.title("Robot")
ventana.geometry("600x600")
def agregar_tarea():
    global procesando
    nueva_tarea = entry_tarea.get()
    tiempo = entry_tiempo.get()
    if nueva_tarea == "" or  tiempo == "":
        messagebox.showerror("Error", "Complete todos los campos")
        return
    try:
        tiempo = float(tiempo)
    except:
        messagebox.showerror("Error", "Tiempo debe ser números")
        return

    tar=tarea(nueva_tarea,tiempo)
    pila.append(tar)

    listbox_tareas.insert(0, f"{nueva_tarea} - {tiempo} seg")
    entry_tarea.delete(0, tk.END)
    entry_tiempo.delete(0, tk.END)
    inicio_procesar()

def realizar_tarea():
    global procesando
    if len(pila)==0:
        procesando = False
        estado_label.config(text="Sin tareas en la pila", fg="green")
        return
    #procesando=True
    tarea_actual = pila.pop()
    listbox_tareas.delete(0)
    estado_label.config(text=f"Procesando: {tarea_actual.tarea1}...",fg="yellow")
    ms = int(tarea_actual.tiempoxtar * 1000)
    ventana.after(ms, realizar_tarea)

def inicio_procesar():
    global procesando
    if procesando:
        return

    if len(pila) == 0:
        estado_label.config(text="No hay tareas en la pila :D", fg="orange")
        return
    procesando = True
    realizar_tarea()

tk.Label(ventana, text="Tarea a Realizar: ").grid(row=0, column=0, padx=10, pady=10)
entry_tarea = tk.Entry(ventana)
entry_tarea.grid(row=0, column=1)
tk.Label(ventana, text="Tiempo por Tarea (seg):").grid(row=1, column=0, padx=10, pady=10)
entry_tiempo = tk.Entry(ventana)
entry_tiempo.grid(row=1, column=1)
tk.Button(ventana, text="Agregar Tarea", command=agregar_tarea).grid(row=2, column=0, columnspan=2, pady=10)

tk.Label(ventana, text="Tareas en la pila").grid(row=0, column=3,columnspan=2, padx=30)
listbox_tareas = tk.Listbox(ventana)
listbox_tareas.grid(row=1, column=3, columnspan=2, padx=30)

estado_label = tk.Label(ventana, text="Esperando...", fg="blue", bg="black")
estado_label.grid(row=2, column=3, columnspan=2)

ventana.mainloop()
