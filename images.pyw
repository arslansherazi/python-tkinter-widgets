from tkinter import *

win = Tk()
win.title("Tic Toc Toe Game")
win.geometry("500x500")

# this function is used to fix the window(user cant change its size using mouse).It also disables the maximize button.
win.resizable(0, 0)
# The size remains same as defined.

background = PhotoImage(file="../images/logo.gif")

win.mainloop()  # It is used to control the window in console works same as input() function.
