from tkinter import *

root = Tk()
root. title('Hola mundo')

#funciones para el boton (solo se crea una vez el texto)
l = Label(root, text='¡Hola Mundo!')
def click():
    l.pack() #agrego el label a la interfaz



#va sin parentesis porque no quiero que se ejecute automaticamente
btn = Button(root, text='Clickeame', command=click, fg='#ffff00', bg='blue')
btn.pack()

root.mainloop()