from tkinter import *

#frames
root= Tk()
root.title("frames")
#height,width
fmain = Frame(root,bg="yellow",padx=20)
fmain.pack()

f = Frame(fmain,bg="red",padx=20)
f.pack()
f1 = Frame(fmain,bg="red",padx=20)
f1.pack()

b1 = Button(f,text="b1",padx=10,pady=10)
b2 = Button(f,text="b2",padx=10,pady=10)
b3 = Button(f1,text="b3",padx=10,pady=10)
b4 = Button(f1,text="b4",padx=10,pady=10)


b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)
b4.pack(side=LEFT)



b=Button(fmain,text="exit",command=root.quit)
b.pack()
root.mainloop()