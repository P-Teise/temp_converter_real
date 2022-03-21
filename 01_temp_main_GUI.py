from tkinter import *
import random

root = Tk()
root.title("Temperature converter")

# first label test
temp_label = Label(root, text="temperature converter", bg="blue")
temp_label.grid(row=0, column=0, padx=3, pady=3)

root.mainloop()
