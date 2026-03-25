#Punto 1 Guia 3
import tkinter as tk
from tkinter import messagebox
import time
from collections import deque

class documento:
  def __init__(self, nombre, paginas, tiempoxpag):
    self.nombre=nombre
    self.paginas=paginas
    self.tiempoxpagina=tiempoxpag


#Esta es la ventana, luego su titulo y en la parte de lo numeros es el ancho por el alto en pixeles :P

ventana=tk.Tk()
ventana.title("Cola Impresion <3")
ventana.geometry("600x600")

colap=deque() #aqui se constrimos el objeto

imprimiendo = False

def agregar_documento():
    nombre = entry_nombre.get()
    paginas = entry_paginas.get()
    tiempo = entry_tiempo.get()

    if nombre == "" or paginas == "" or tiempo == "":
        messagebox.showerror("Error", "Complete todos los campos")
        return

    try:
        paginas = int(paginas)
        tiempo = float(tiempo)
    except:
        messagebox.showerror("Error", "Paginas y tiempo deben ser números")
        return

    doc=documento(nombre, paginas, tiempo)
    colap.append(doc)

    listbox.insert(tk.END, f"{nombre} ({paginas} páginas)")
    entry_nombre.delete(0, tk.END)
    entry_paginas.delete(0, tk.END)
    entry_tiempo.delete(0, tk.END)

    estado_label.config(text="Documento agregado a la cola")


def imprimir_pag(doc, pagact):
  global imprimiendo

  if pagact<=doc.paginas:
    estado_label.config(text=f"Imprimiendo {doc.nombre} , pagina {pagact} de {doc.paginas}", fg="blue")

    ventana.after(int(doc.tiempoxpagina*1000),lambda:imprimir_pag(doc, pagact+1))

  else:
    #cuando el documento se termino de imprimir entonces lo sacamos para no verlo mas

    listbox.delete(0)

    #luego revisamos si hay mas documentos en la cola

    if len(colap) !=0:
      siguiente_doc=colap.popleft()
      imprimir_pag(siguiente_doc, 1)

    else:
      imprimiendo=False
      estado_label.config(text="Sin documentos en cola", fg="green")


def inicio_imp():

  global imprimiendo

  if imprimiendo:
    return #como ya esta imprimiendo, entonces le dicimos que no haga nada :P

  if len(colap)==0:
    estado_label.config(text="No hay documento en la cola :D",fg="orange")
    return

  imprimiendo=True
  doc=colap.popleft()
  listbox.delete(0) #eliminarlo de la lista para que no se vea
  imprimir_pag(doc,1) #le decimos que empiece desde la pagina 1


#primero creo los frames, uno para cada lado

lado_izq=tk.Frame(ventana,bg="lightblue") 
lado_der=tk.Frame(ventana, bg="lightyellow")

lado_izq.grid(row=0,column=0) #la columna 0 es la de la izquierda
lado_der.grid(row=0,column=1) #la columna 1 es la de la derecha (lo malo es que soy dislexica)

#Aqui van a aparecer los frames del lado izquierdo

tk.Label(lado_izq, text="Nombre: ", bg="lightblue").grid(row=0, column=0)
entry_nombre=tk.Entry(lado_izq)
entry_nombre.grid(row=1,column=0)

tk.Label(lado_izq, text="Paginas: ", bg="lightblue").grid(row=2,column=0)
entry_paginas=tk.Entry(lado_izq)
entry_paginas.grid(row=3, column=0, pady=5)

tk.Label(lado_izq, text="Tiempo por pagina: ", bg="lightblue").grid(row=4, column=0)
entry_tiempo=tk.Entry(lado_izq)
entry_tiempo.grid(row=5, column=0)

botagregar=tk.Button(lado_izq, text="Agregar a la cola", command=lambda: agregar_documento())
botagregar.grid(row=6, column=0, pady=5)

botimprimir=tk.Button(lado_izq, text="Iniciar impresion", command=lambda: inicio_imp())
botimprimir.grid(row=7, column=0, pady=5)

#Aqui van a aparecer los frames del lado derecho

tk.Label(lado_der, text="Documentos en cola", bg="lightyellow").grid(row=0, column=0)
listbox=tk.Listbox(lado_der, width=35)
listbox.grid(row=1, column=0)

estado_label=tk.Label(lado_der, text="Sin documentos en cola", fg="blue", bg="lightyellow")
estado_label.grid(row=2, column=0)


ventana.mainloop()
