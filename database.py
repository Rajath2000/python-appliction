from tkinter import *
import sqlite3

f = Tk()
f.title("database")

conn = sqlite3.connect('adress_book.db')

c = conn.cursor()
#c.execute("CREATE TABLE addresses(f_name text,l_name text,adress text,city text,state text,zipcode integer)")
 
def submit():
	conn = sqlite3.connect('address_book.db')
	c = conn.cursor()
	c.execute("INSERT INTO addresses VALUES(:f_name,:l_name,:adress,:city,:state,:zipcode)",
          {
              'f_name':f_name.get(),
              'l_name':l_name.get(),
              'adress':adress.get(),
              'city':city.get(),
              'state':state.get(),
              'zipcode':zipcode.get()
          }

		)
	conn.commit()
	conn.close()
	f_name.delete(0,END)
	l_name.delete(0,END)
	adress.delete(0,END)
	city.delete(0,END)
	state.delete(0,END)
	zipcode.delete(0,END)

def query():
	conn = sqlite3.connect('address_book.db')
	c = conn.cursor()
	c.execute("SELECT *,oid FROM addresses")
	records=c.fetchall()
	print(records)
	print_record=''
	for r in records:
		print_records= str(r) + "\n"
	query_label = Label(f,text=print_records)
	query_label.grid(row=8,column=0,columnspan=2)
	conn.commit()
	conn.close()


f_name = Entry(f,width=30)
f_name.grid(row=0,column=1,padx=20)

l_name = Entry(f,width=30)
l_name.grid(row=1,column=1,padx=20)

adress = Entry(f,width=30)
adress.grid(row=2,column=1,padx=20)

city = Entry(f,width=30)
city.grid(row=3,column=1,padx=20)

state= Entry(f,width=30)
state.grid(row=4,column=1,padx=20)

zipcode = Entry(f,width=30)
zipcode.grid(row=5,column=1,padx=20)


f_name_label=Label(f,text="first name")
f_name_label.grid(row=0,column=0)

l_name_label=Label(f,text="Last name")
l_name_label.grid(row=1,column=0)

adress_label=Label(f,text="adress")
adress_label.grid(row=2,column=0)

city_label=Label(f,text="city")
city_label.grid(row=3,column=0)

state_label=Label(f,text="state")
state_label.grid(row=4,column=0)

zipcode_label=Label(f,text="zipcode")
zipcode_label.grid(row=5,column=0)




submit_button = Button(f,text="add record to database",command=submit)
submit_button.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

query_btn=Button(f,text="show record",command=query)
query_btn.grid(row=7,column=0,columnspan=2,padx=10,pady=10,ipadx=137)

conn.commit()

conn.close()


f.mainloop()