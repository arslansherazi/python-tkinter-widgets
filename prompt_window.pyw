from tkinter import *
from tkinter import messagebox

win1 = Tk()
win1.title("Text Editor")
win1.geometry("500x500")


def save():
    # Creating a prompt for user
    messagebox.showinfo(title="Save", message="Successfully Saved")


def _quit():
    # The following code ask user to Quit.If he/she press yes then the specified window is vanished.
    opt = messagebox.askyesno(title="Quit",
                              message="Are you want to Quit?")  # opt is returned 1 if user press yes otherwise 0.
    if opt == 1:
        win1.destroy()  # if opt is 1(user press yes) then this function vanish(destroy) the Specified Window(win1)


Button(win1, text="Press To Save", bg="Green", fg="White", font=('algerian', 24, 'bold'), command=save).pack()
Button(win1, text="Press To Quit the Screen", bg="Green", fg="White", font=('bauhaus 93', 24, 'bold'),
       command=_quit).pack()

win1.mainloop()
