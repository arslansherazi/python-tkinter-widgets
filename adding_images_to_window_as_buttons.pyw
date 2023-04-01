from tkinter import *

win = Tk()

win.title("Tic Toc Toe Game")
win.geometry("500x500")
win.resizable(0, 0)

# Image should reside in the same directory where the Python file exist.(.jpg images are not compatible)
photo = PhotoImage(file='pause.png')

label = Button(win, image=photo, command=win.destroy)
label.pack()

win.mainloop()
