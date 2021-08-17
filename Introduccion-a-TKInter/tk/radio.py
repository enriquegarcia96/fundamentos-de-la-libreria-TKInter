from tkinter import *


root  = Tk()
root.title('Hola mundo')

r = IntVar()
r.set('2')

CHANCHITOS = [
    ('Feliz', 'Feliz'),
    ('Triste', 'Triste'),
    ('Amargado', 'Amargado'),
    ('Wolfgang', 'Wolfgang')
]


chanchito = StringVar()
chanchito.set('Wolfgang')


#muestro en pantalla
for text, chancho in CHANCHITOS:
    Radiobutton(root, text=text, variable=chanchito, value=chancho).pack()


l = Label(root, textvariable=chanchito)
l.pack()

root.mainloop()
