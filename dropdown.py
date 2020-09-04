from tkinter import *

top = Tk()
top.title("dropdown")
f = Frame(top).pack()

f1=Frame(f).pack()
clicked = StringVar()
clicked.set("monday")
drop = OptionMenu(f1,clicked,"monday","tuesday","wednesday","thursday","friday","saturday","sunday").pack()




top.mainloop()