from tkinter import *
from PIL import ImageTk,Image
master = Tk()
master.title('tkinterGUI creator')
master.configure(background="black")
master.geometry("600x600")


#frames
main_frame = Frame(master).pack()
title_frame=Frame(master).pack()

main_Label = Label(main_frame,text="Create your dream GUI",fg="green",font=("Helvectica",20),bg="black").pack()

title_label = Label(title_frame,text ="Tite",fg="green",bg="black",font=20).place(height=75,width=50,x=125,y=100)
title_box = Entry(title_frame,bd=5,bg="black",fg="red").place(height=20,width=150,x=200,y=116)

















master.mainloop()