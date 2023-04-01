from tkinter import *

win = Tk()
win.title("Conversion Calculator")
win.geometry("500x120")
win.resizable(0, 0)


def _calculate():
    var = cal.get()
    box2.insert(1, var / 1.6)  # insert calculated value in the Miles Box


def clear():
    box1.delete(0, END)  # Delete is a Function which is used to delete (clear) the calculated or inserted values in the text fields.
    box2.delete(0, END)


cal = IntVar()

L1 = Label(win, text="KiloMeters \t", font=("Arial Black", 18, 'bold'))
L1.grid(row=0)

box1 = Entry(win,
             textvariable=cal)  # Entry is a class which is used to make a text box in which user can input any data
box1.grid(row=0, column=1)
box1.insert(0, 0)  # we can insert any data in text fields at the programming end using insert function of Entry class.fisrt 0 is for positioning the data
# in text field.At second zero we can also write text

L2 = Label(win, text="Miles \t", font=("Arial Black", 18, 'bold'))
L2.grid(row=1)

box2 = Entry(win)
box2.grid(row=1, column=1)

calculate = Button(win, text="Calculate", bg="green", fg="White", font=("broadway", 18), width=10, command=_calculate)
calculate.grid(row=2, column=0)

reset = Button(win, text="Reset", bg="green", fg="White", font=("broadway", 18), width=10, command=clear)
reset.grid(row=2, column=1)

_exit = Button(win, text="Exit", bg="green", fg="White", font=("broadway", 18), command=win.destroy, width=10)
_exit.grid(row=2, column=2)

win.mainloop()
