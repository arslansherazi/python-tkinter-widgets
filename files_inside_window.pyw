from tkinter import *
from tkinter import filedialog

win = Tk()
win.geometry("500x500+120+150")


def open_file():
    file1 = filedialog.askopenfile()
    # filedialog() is a class in tkinter() module and askopenfile is a function in it which is used to open a file open
    # dialog box when user opens file from computer then its path is saved in object (file1)

    file2 = file1.name  # in this line of code we save name of opened file in file2

    f = open(file2)  # in this line of code we exactly opens the file and save in "f" variable.

    # using label we show the text data of file in window and read() function reads data from file.
    Label(text=f.read(), font=('Arial', 12)).pack()


Button(text="Click to Open File", font=('goudy stout', 15, 'bold'), command=open_file).pack()

win.mainloop()
