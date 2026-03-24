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

class colaimp:
  def __init__(self):
    self.cola=deque() #aqui es donde vienen los documentos en espera

  def agregar(self, documento):
    self.cola.append(documento) #entra por el el final

  def siguiente(self):
    return self.cola.popleft() #sale por el frente

  def vacio(self):
    return len(self.cola)==0

#Esta es la ventana, luego su titulo y en la parte de lo numeros es el ancho por el alto en pixeles :P

ventana=tk.Tk()
ventana.title("Cola Impresion <3")
ventana.geometry("600x600")
colap=colaimp() #aqui se constrimos el objeto
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
    colap.agregar(doc)

    listbox.insert(tk.END, f"{nombre} ({paginas} páginas)")
    entry_nombre.delete(0, tk.END)
    entry_paginas.delete(0, tk.END)
    entry_tiempo.delete(0, tk.END)

    estado_label.config(text="Documento agregado a la cola")


def imprimir_pag(doc, pagact):
  global imprimiendo

  if pagact<=doc.paginas:
    estado_label.config(text=f"Imprimiendo {doc.nombre} , pagina {pagact} de {doc.paginas}", fg="yellow")

    ventana.after(int(doc.tiempoxpagina*1000),lambda:imprimir_pag(doc, pagact+1))

  else:
    #cuando el documento se termino de imprimir entonces lo sacamos para no verlo mas
    listbox.delete(0)
    #luego revisamos si hay mas documentos en la cola
    if not colap.vacio():
      siguiente_doc=colap.siguiente()
      imprimir_pag(siguiente_doc, 1)
    else:
      imprimiendo=False
      estado_label.config(text="Sin documentos en cola", fg="green")


def inicio_imp():

  global imprimiendo

  if imprimiendo:
    return #como ya esta imprimiendo, entonces le dicimos que no haga nada :P

  if colap.vacio():
    estado_label.config(text="No hay documento en la cola :D",fg="orange")
    return

  imprimiendo=True
  doc=colap.siguiente()
  listbox.delete(0) #eliminarlo de la lista para que no se vea
  imprimir_pag(doc,1) #le decimos que empiece desde la pagina 1

tk.Label(ventana, text="Nombre del documento: ").pack()
entry_nombre=tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Numero de paginas:").pack()
entry_paginas=tk.Entry(ventana)
entry_paginas.pack()

tk.Label(ventana, text="Tiempo por pagina (seg):").pack()
entry_tiempo=tk.Entry(ventana)
entry_tiempo.pack()

botagregar=tk.Button(ventana, text="Agregar a la cola", command=agregar_documento)
botagregar.pack()

botimprimir=tk.Button(ventana, text="Iniciar impresion", command=inicio_imp)
botimprimir.pack()

tk.Label(ventana, text="Documentos en cola:").pack()
listbox=tk.Listbox(ventana, width=40) # es una caja que muestra una lista de items, el 40 con esa cosa rara significa que tiene 40 caracteres de ancho, aqui es donde aparecen los doumentos que agregamos a la cola
listbox.pack()

estado_label=tk.Label(ventana, text="Sin documentos en cola", fg="blue") #este lo guardamos en una variable, ya que el texto va a cambiar durante el programa, y pues el fg es color del texto, si mi vida, si puede ser rojo
estado_label.pack()

ventana.mainloop() #esto se coloca de ultimas, ya que esta cosa es la que mantiene la ventana abierta y tambien la que capta los cliks, cuando python llega a la linea se queda atascado captanto los clicks hasta que cerremos la ventana, TODO!!! lo que pongamos despues no se va a ejecutar :(
