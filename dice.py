from tkinter import *
from random import randint

root = Tk()
root.title("Rulla tärning")
text_box = Label(root, text="")
text_box.pack()
# ändra hur många tärningar, historik, typ av tärning t4 t6 t8 t10 t12 t20
def show():
    roll = randint(1, 6)
    text_box.config(text=roll)

show_button = Button(root, text="Rulla en T6", width=50, command=show)
show_button.pack()
button = Button(root, text="Avsluta", width=50, command=root.destroy)
button.pack()

root.mainloop()