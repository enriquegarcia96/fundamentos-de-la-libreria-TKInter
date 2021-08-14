from tkinter import *

root = Tk()

root.title('Hola Mundo')
root.geometry('500x500')


e = Entry(root, width=40)
e.pack()
e.insert(0, 'Ingresa texto:')


def click():
    texto = e.get() #obtiene el texto que se ingreso en el input

    textvariable.set(texto)
    valor = textvariable.get()
    #print(valor)
    # l = Label(root, text=texto)
    # l.pack()
    e.delete(0, END)#Elimina el texto del input
    #l.configure(text=texto)#actualiza la etiqueta con el texto que se ingreso en el input

btn = Button(root, text='click', command=click)
btn.pack()

textvariable = StringVar()

l  = Label(root, textvariable=textvariable)
l.pack()

root.mainloop()

