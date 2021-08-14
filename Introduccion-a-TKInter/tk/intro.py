from tkinter import *

root = Tk()
root.title('Hola mundo')
root.geometry('500x500')#las dimensiones que la ventana que tendra

label = Label(root, text='Hola mundo! mi primera etiqueta')
#Label(root, text='Hola mundo! mi primera etiqueta').pack()
label.pack()#para que el elemento sea visible en la ventana


root.mainloop() #se queda escuchando los posibles cambios que se creean dentro de root.
