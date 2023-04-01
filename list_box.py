from tkinter import *

if__name__ = "__main__"

win = Tk()
win.geometry("500x500")
win.configure(background="lightblue")  # Window background color also shows to list elements if we select them.if it is not set
win.resizable(0, 0)

scrollbar = Scrollbar(win)
scrollbar.pack(side=RIGHT, fill=Y)

programming_languages = Listbox(win, bg="blue", bd=10, highlightcolor="orange", fg="pink", selectbackground="Chartreuse",
                                cursor="heart", width="100", yscrollcommand=scrollbar.set)  # bd=border size
# selectbackground property sets the color when we select an element from the list.
# cursor property sets the cursor when we move our mouse to List box or selects any element from ListBox.


programming_languages.insert(1, "C")

programming_languages.insert(2, "C++")

programming_languages.insert(3, "Java")

programming_languages.insert(4, "Cobol")

programming_languages.insert(5, "C")

programming_languages.insert(6, "C++")

programming_languages.insert(7, "Java")

programming_languages.insert(8, "Cobol")

programming_languages.insert(9, "C")

programming_languages.insert(10, "C++")

programming_languages.insert(11, "Java")

programming_languages.insert(12, "Cobol")

programming_languages.pack()  # List should be packed or placed or grid after done inserting elements in it.

scrollbar.config(command=programming_languages.yview)

win.mainloop()
