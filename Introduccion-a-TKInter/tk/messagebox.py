from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Hola mundo')

# def click():
#     messagebox.showwarning('Popup', 'Hola mundo')

# def click():
#      messagebox.showinfo('Popup', 'Hola mundo')

# def click():
#      messagebox.showerror('Popup', 'Hola mundo :(')


# def click():
#     respuesta = messagebox.askquestion('popup', 'Hola mundo')
#     if respuesta == 'yes':
#         messagebox.showinfo('Respuesta', 'la respuesa fue ' + respuesta)
#     else: 
#         messagebox.showinfo('Respuesta', ':( la respuesa fue '+ respuesta)

# def click():
#     respuesta = messagebox.askokcancel('Hola Mundo', 'Desea realizar accion?')
#     if respuesta:
#         messagebox.showinfo('Hola mundo', ' la respuesta fue OK')
#     else:
#         messagebox.showinfo('Hola mundo', ' la respuesta fue cancelar')
    
def click():
    respuesta = messagebox.askyesno('Hola Mundo', 'Desea realizar accion?')
    if respuesta:
        messagebox.showinfo('Hola mundo', ' la respuesta fue Yes')
    else:
        messagebox.showinfo('Hola mundo', ' la respuesta fue No')


btn = Button(root, text='Presioname', command=click)
btn.pack()


root.mainloop()