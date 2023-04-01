from tkinter import *

win1 = Tk()
win1.title("Text Editor")
win1.geometry("500x500")


# Functions for File Drop Down Menu

def new_file():
    Label(text="NEW FILE", font=20).pack()


def open_file():
    Label(text="OPEN FILE", font=20).pack()


def save_file():
    Label(text="SAVE FILE", font=20).pack()


def save_as_file():
    Label(text="SAVE AS FILE", font=20).pack()


def select_all():
    Label(text="SELECT ALL", font=20).pack()


manu_bar = Menu()

file_list = Menu()

manu_bar.add_cascade(label="File", menu=file_list)
manu_bar.add_cascade(label="Edit")
manu_bar.add_cascade(label="Format")
manu_bar.add_cascade(label="Run")
manu_bar.add_cascade(label="Options")
manu_bar.add_cascade(label="Window")
manu_bar.add_cascade(label="Help")

file_list.add_command(label="New", command=new_file)
file_list.add_command(label="Open", command=open_file)
file_list.add_command(label="Save", command=save_file)
file_list.add_command(label="Save As", command=save_as_file)

# add_checkbutton is used to add a checkbox as a drop-down menu item of a menu bar item
file_list.add_checkbutton(label="Select All", command=select_all)

win1.config(menu=manu_bar)

win1.mainloop()
