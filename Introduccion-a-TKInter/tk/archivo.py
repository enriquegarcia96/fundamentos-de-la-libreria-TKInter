from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog # es un objeto que entregara unos metodos para usar con los archivos

root = Tk()
root.title('Hola mundo: archivos')

# root.filename = filedialog.askopenfile(title='Elige una foto', filetypes=(("Archivos PNG", "*.png"), ('Todos', '*')))
# l = Label(root, text=root.filename)
# l.pack()
# img = Image.open(root.filename)
# imgTK = ImageTk.PhotoImage(img)

# l2 = Label(root, image=imgTK)
# l2.pack()


def open():
    global imgTk
    root.filename = filedialog.askopenfile(title='Elige una foto', filetypes=(("Archivos PNG", "*.png"), ('Todos', '*')))
    l = Label(root, text=root.filename)
    l.pack()
    img = Image.open(root.filename)
    imgTK = ImageTk.PhotoImage(img)

    l2 = Label(root, image=imgTK)
    l2.pack()

btn = Button(root, text='Cargar Imagen', command=open)
btn.pack()

root.mainloop()