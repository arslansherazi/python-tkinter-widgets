import tkinter as tk

win = tk.Tk()
win.title("Tic Toc Toe Game")
win.geometry("500x500")

counter = 0


def counter_label(_label):
    counter = 0

    def count():
        global counter  # global variable can accessed everywhere
        counter += 1
        _label.config(text=str(counter))  # converting counter into string because label should be in string
        _label.after(1, count)  # this function change the value of counter after 100 milliseconds we can change it.

    count()


label = tk.Label(win, fg="Green")  # Creating Empty label for Counter
label.pack()

# Calling the counter function by passing L (label) as a parameter because counter shows on the place of label
counter_label(label)

# destroy is a function of Tk() class which can access by its object(win) and used to terminate the window.
button = tk.Button(win, text="Stop", comman=win.destroy, bg="Green", fg="black", width=40, height=5)
button.pack()

win.mainloop()
