from tkinter import *

win = Tk()
win.title("Radio Buttons")
win.geometry("500x500")


def welcome_window():
    radio_button_value = var.get()  # "radio_button_value" is variable which access the value of "var" in which radio button and is saved checked by the user.
    if radio_button_value == 1:
        win1 = Tk()
        win1.title("Python")
        Label(win1, text="Welcome to Python", font=("Arial Black", 20)).pack()
    if radio_button_value == 2:
        win2 = Tk()
        win2.title("C")
        Label(win2, text="Welcome to C", font=("Arial Black", 20)).pack()
    if radio_button_value == 3:
        win3 = Tk()
        win3.title("C++")
        Label(win3, text="Welcome to C++", font=("Arial Black", 20)).pack()
    if radio_button_value == 4:
        win4 = Tk()
        win4.title("Java")
        Label(win4, text="Welcome to Java", font=("Arial Black", 20)).pack()
    if radio_button_value == 5:
        win5 = Tk()
        win5.title("Html")
        Label(win5, text="Welcome to Html", font=("Arial Black", 20)).pack()


var = IntVar()  # variable of Int Type used to accept the value of radio button(1,2,3....) which is selected by the user

var.set(5)  # it is used to default check the 2nd radio button we can change it.

array = [("Python", 1), ("C", 2), ("C++", 3), ("Java", 4), ("Html", 5)]  # array with (language,value) as its one index.

for txt, val in array:  # txt shows language and val shows its value in one index of array(list).
    # and for loop creates the radiobutton according to the no of indexes in the loop
    Radiobutton(
        win, text=txt, variable=var, value=val, padx=20, pady=15, font=("Arial Black", 18, 'bold'),
        command=welcome_window
    ).pack(anchor=W)  # This function is used to create a Radio button

    # padx and pady are used to specify the space at x-axis and y-axis for a specified radio button

    win.mainloop()
