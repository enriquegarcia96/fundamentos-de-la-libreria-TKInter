from os import remove
from tkinter import *
import sqlite3  # base de datos similar a MYSQL


root = Tk()
root.title('Hola Mundo: TodoList')
root.geometry('500x500')

# conexion con la base de datos
conn = sqlite3.connect('todo.db')
c = conn.cursor()

# creo la tabla
c.execute("""
    CREATE TABLE if not exists todo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        create_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        description TEXT NOT NULL, 
        completed BOOLEAN NOT NULL
    );
""")

# la ejecuto en SQL
conn.commit()


# Curring! retrasar la ejecucion de una funcion
def remove(id):
    def _remove():
        c.execute("DELETE FROM todo WHERE  id = ?", (id, ))
        conn.commit()
        render_todos()

    return _remove


# Curring! retrasar la ejecucion de una funcion
def complete(id):
    def _complete():  # para que no agarre el ultimo id del TODOS, y asi tomar el id que le pertenece del TODOS, retrasa la funcion
        todo = c.execute("SELECT * FROM todo WHERE id = ?", (id, )).fetchone()
        c.execute("UPDATE todo SET completed = ? WHERE id = ?",
                  (not todo[3], id))
        conn.commit()
        render_todos()
        # print(id)

    return _complete


# Funcion para renderizar los TODOS
def render_todos():
    # devuelve todos los todos
    rows = c.execute("SELECT * FROM todo").fetchall()
    # print(rows)

    # para eliminar los TODOS dentro del elemento Frame
    for widget in frame.winfo_children():
        widget.destroy()  # para eliminar los elementos(boton de eliminar)

    # recibe una lista de elementos
    for i in range(0, len(rows)):
        id = rows[i][0]
        completed = rows[i][3]  # la columna para saber si esta completado o no
        description = rows[i][2]
        color = '#555555' if completed else 'red'

        l = Checkbutton(frame, text=description, fg=color,
                        width=42, anchor='w', command=complete(id))
        l.grid(row=i, column=0, sticky='w')  # pega la etiqueta a la izquierda

        btn = Button(frame, text='Eliminar', command=remove(id))
        btn.grid(row=i, column=1)

        l.select() if completed else l.deselect()


def addTodo():
    todo = e.get()
    if todo:
        # se encagarga de agregar a la tabla
        c.execute("""
            INSERT INTO todo (description, completed) VALUES (?, ?)
        """, (todo, False))
        conn.commit()

        # limpio el INPUT
        e.delete(0, END)
        render_todos()  # para renderizar  el TODOS ingresado
    else:
        pass


# creo la interfaz grafica
l = Label(root, text='Tarea')
l.grid(row=0, column=0)

e = Entry(root, width=40)
e.grid(row=0, column=1)

btn = Button(root, text='Agregar', command=addTodo)
btn.grid(row=0, column=2)


# creo el frame donde se agregaran todos los tareas ingresadas
frame = LabelFrame(root, text='Mis tareas', padx=5, pady=5)
frame.grid(row=1, column=0, columnspan=3, sticky='nswe', padx=5)
e.focus()


# rederiza el "todo" una vez ingresado
root.bind('<Return>', lambda x: addTodo())

# muestra los TODOS renderizados una vex que entre a la aplicacion
render_todos()

root.mainloop()
