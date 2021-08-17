from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('Hola Mundo')

# Solucion 1
# def open():
#     img = ImageTk.PhotoImage(Image.open('./img/2.png'))

#     #Abro una nueva ventana
#     top = Toplevel()
#     top.title('Hola Mundo Nueva Ventana')
#     l = Label(top, text='Soy un texto  en una segunda ventana')
#     l2 = Label(root, image=img)

#     l.pack()
#     l2.pack()
#     top.mainloop()


#Solucion 2
# def open():
#     global img
#     img = ImageTk.PhotoImage(Image.open('./img/2.png'))

#     #Abro una nueva ventana
#     top = Toplevel()
#     top.title('Hola Mundo Nueva Ventana')
#     l = Label(top, text='Soy un texto  en una segunda ventana')
#     l2 = Label(top, image=img)
#     l.pack()
#     l2.pack()


#Solucion 3
def open(img):

    #Abro una nueva ventana
    top = Toplevel()
    top.title('Hola Mundo Nueva Ventana')
    l = Label(top, text='Soy un texto  en una segunda ventana')
    l2 = Label(top, image=img)
    l.pack()
    l2.pack()



img = ImageTk.PhotoImage(Image.open('./img/2.png'))
btn = Button(root, text='Click', command=lambda: open(img)).pack()

#btn = Button(root, text='Click', command= open).pack()


root.mainloop()