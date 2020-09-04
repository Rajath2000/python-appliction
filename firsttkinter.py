#https://www.tutorialspoint.com/python/tk_canvas.htm
from tkinter import *
#basics
from PIL import ImageTk,Image
#from tkinter import messsagebox
top = Tk()
top.title("intro to tkinter")
# Code to add widgets will go here...
#label
#fg(text color),bg(background color),bd(border width in px)
mylabel1 = Label(top,bg="blue",text="rajath",cursor="dot",padx=50)
mylabel2 = Label(top,bg="red",text="rahul")
#mylabel1.grid(row=0,column=0)(like css)
#mylabel2.grid(row=1,column=1)
#label packing(bootstrap)
mylabel1.pack()
mylabel2.pack()

#buttons,padx,pady,state(active,disable),command(for calling the funtion on click(button))
def onclick1():#called function perform action after clicking the button
	labelbuttton =Label(top,text="hey I cicked",fg="blue")
	labelbuttton.pack()
#button syntax
button1=Button(top,text="click me",padx=50,bg="yellow",command=onclick1,bd=6,font=60)
button1.pack()

#Entry(user input)
#width(in px),fg,bg,get() is function returns the vaue enterd in the checkbox,insert(post the defalt value inside the checkbox)
def myfunc():
	mylab = Label(top,text="hello "+ myentry.get())
	mylab.pack()

myentry = Entry(top,width=60,bd=6)
myentry.insert(0,"rajath")
but=Button(top,text="enter the name",command=myfunc)#by using lambda we can pass parameter whie calling
but.pack()
#syntax is 
#command= lambda: functionname(parameters)
myentry.pack()

#icons
top.iconbitmap('C:\\Users\\user\\Downloads\\c-01.ico')
#images(PIL->PILLO)
myimg = ImageTk.PhotoImage(Image.open('E:\\ic project\\login\\bg-01.jpg'))
myl=Label(image=myimg)
myl.pack()


#radiobuttons
#syntax
#object = Radiobuttion(master,variable=variable_name,value=anytype of value)
#to defind the type of the variable before using the variabe define it syntax is 
#variabe_name=typrvar()
def sel():
	l100=Label(top,text="selected is "+ m.get()).pack()

m=StringVar()
m.set("male")
r1=Radiobutton(top,variable=m,value='male',text="male",command=sel).pack()
r2=Radiobutton(top,variable=m,value='female',text="female",command=sel).pack()


#messsageboxes
#showinfo()
#showwarning()
#showerror ()
#askquestion()
#askokcancel()
#askyesno ()
#askretrycancel ()
#def showmessage():
	#messsagebox.showinfo("this is title","this is a message")



#bon = Button(top,text="go",command=showmessage).pack()

#canvas
#w = Canvas ( master, option=value, ... )

#scorll
vs = Scale(top,from_=0,to=200)
vs.pack()
hs = Scale(top,from_=0,to=200,orient=HORIZONTAL)
hs.pack()


#set the size of the window
top.geometry("500x800")

#check boxes
fm= Frame(top).pack()
def cb():
	lam = Label(fm,text=vaue.get()).pack()

vaue = IntVar()
c = Checkbutton(fm,text="python",variable=vaue,).pack()

bn = Button(fm,text="wow",command=cb).pack()





#exit button
b=Button(top,text="Exit",command=top.quit)
b.pack()
top.mainloop()






#TASKS
#task 1:building A simpe calculator
#task 2:building a gallary















