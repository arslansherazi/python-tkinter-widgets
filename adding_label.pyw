from tkinter import *

win = Tk()
win.title("Tic Toc Toe Game")
win.geometry("500x500")

# Creating Label

# Object of window creation e.g. win=Tk() should be pass when we use a new class of tkinter module to distinguish
# if more than two windows are created
label = Label(win, text='Press Enter to Start the Game', fg='red')

# Direction should be defined for label otherwise it is not shown
# (direction can be shown by using any  of the following method)

# it is used to place the content at the center.Anchor is used to specify direction (East,West,South,North)
label.pack(anchor=E)

# it is used to place the content at specific location.Sticky is used to specify direction (East,West,South,North)
label.grid(row=500, column=500, sticky=E)

label.place(x=160, y=200)  # it is used to place the content at specific location

win.mainloop()
