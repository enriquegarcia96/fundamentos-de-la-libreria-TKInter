from tkinter import *
from tkinter import ttk


root = Tk()
root.title('Hola mundo: Treeview')

tree = ttk.Treeview(root)

#creo el arbol con las columnas
tree['columns'] = ('Nombre', 'Telefono', 'Empresa')

#especifico los indices de las columnas
#tree.column('#0')
tree.column('#0', width=0, stretch=NO)
tree.column('Nombre')
tree.column('Telefono')
tree.column('Empresa')


# los nombre que van a tener cada una de las columnas
#tree.heading('#0', text='id')
tree.heading('#0')
tree.heading('Nombre', text='Nombre')
tree.heading('Telefono', text='Telefono')
tree.heading('Empresa', text='Empresa')


#agrego el witget a la vista
tree.grid(column=0, row=0)

tree.insert('', END, 'lala', values=('Uno','Dos', 'Tres'), text='Chanchito feliz')
tree.insert('', END, 'lele', values=('cuatro','cinco', 'seis'), text='Chanchito triste')
tree.insert('', END, 'lili', values=('4','5', '6'), text='Hijo')


root.mainloop()