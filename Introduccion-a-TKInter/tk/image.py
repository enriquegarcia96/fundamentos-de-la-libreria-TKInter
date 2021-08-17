from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Hola mundo')


# habro la imagen 
# image = Image.open('code.png')
# image.show()


#toma la imagen y lo tranforma en un tipo de dato para utilizar
img = ImageTk.PhotoImage(Image.open('code.png'))
l = Label(image=img)
l.pack()


root.mainloop()