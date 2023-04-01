from tkinter import *
from tkinter import ttk


def func():
    print("ComboBox")


if__name__ = "__main__"

win = Tk()

win.geometry("500x500")
win.configure(background="lightblue")
win.title("Combo Box")
win.resizable(0, 0)

options = ['BMW', 'Honda', 'Ferrari', 'Civic', 'Mahran', 'Yamaha', 'Lamber Gini', 'Prado', 'Rose Rise', 'Range Rovers']
var = StringVar()

cb = ttk.Combobox(win, justify=CENTER, values=options, width=30, textvariable=var, takefocus=FALSE, height=6,
                  cursor="dot", postcommand=func)
cb.place(x=150, y=200)

cb.set('Select Car Name from List')

style = ttk.Style()

style.configure('Alarm.TCombobox', foreground='light blue')

cb.config(style='Alarm.TCombobox')

win.mainloop()
