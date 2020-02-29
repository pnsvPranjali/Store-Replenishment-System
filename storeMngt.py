from tkinter import *
import tkinter.messagebox
import pymysql as p
class Module:
	aen=None
	e11=None
	e22=None
	aep=None
	aeph=None
	aeci=None
	aead=None
	ne=None
	pe=None
	ee=None
	w=None
	w2=None
	de1=de2=None
	__shop_id='0'

	
	def register(self):
	
		con=p.connect("localhost","root","","storemngt")
		cur=con.cursor()
		a=self.ne.get()
		pas=self.pas.get()
		b=self.pe.get()
		c=int(self.ee.get())
		d=int(self.sce.get())
		e=int(self.shlfe.get())

		q1="insert into login values('%s','%s')"
		cur.execute(q1%(a,pas))
		con.commit()

		q="insert into signup values('%s','%s',%d,%d,%d)"
		cur.execute(q %(a,b,c,d,e))
		con.commit()
		
		var=','.join("0"*e)
		q2="insert into store values('%s','%s')"
		cur.execute(q2 %(a,var))
		con.commit()
		
		con.close()

		self.ne.delete(0,'end')
		self.pas.delete(0,'end')
		self.pe.delete(0,'end')
		self.ee.delete(0,'end')
		self.sce.delete(0,'end')
		self.shlfe.delete(0,'end')

		tkinter.messagebox.showinfo("Success","You are registered successfully !!")	


	def login(self):
		
		def verify():
			self.w2=Tk()
			self.w2.geometry('600x400')
			self.w2.title('Login')	
			h1=Label(self.w2,text="WELCOME !!",font="Times 14 bold")
			Label(self.w2,text="     ").grid(row=0,column=2)
			h1.grid(row=1,column=2)
			Label(self.w2,text="     ").grid(row=2,column=2)
			#------------------------------------------------------------------
			con=p.connect("localhost","root","","storemngt")
			cur=con.cursor()
			q="select types_of_shelf from signup where userid='%s'"
			cur.execute(q%(Module.__shop_id))
			self.Data=cur.fetchone()
			num_shelf=self.Data[0]
			con.close()
			choices=[]
			for i in range(int(num_shelf)):
				choices.append("Shelf "+str(i+1))
			#------------------------------------------------------------------
			self.tkvar=StringVar(self.w2)
			
			self.tkvar.set(choices[0]) # set the default option
			popupMenu = OptionMenu(self.w2, self.tkvar, *choices)
			popupMenu.config(width=50)
			Label(self.w2, text="Choose the Shelf ", font=('Helvetica', 12)).grid(row = 3, column = 1)
			popupMenu.grid(row = 3, column =2)
			Label(self.w2,text="     ").grid(row=4,column=1)
			labelTest = Label(self.w2,text="", font=('Helvetica', 12), fg='red')
			Label(self.w2,text="     ").grid(row=5,column=1)
			labelTest.grid(row=6,column=1)

			#---------------------------------------
			con=p.connect("localhost","root","","storemngt")
			cur=con.cursor()
			q="select current_capacity from store where userid='%s'"
			cur.execute(q%(Module.__shop_id))
			self.Data=cur.fetchone()
			curr=self.Data[0]
			curr=curr[0:].split(',')
			print(curr)
			con.close()

			def callback(*args):
			    labelTest.configure(text="The {} contains {} ".format(self.tkvar.get(),curr[int(self.tkvar.get()[-1])-1]))

			self.tkvar.trace("w", callback)

			#---------------------------------------------------------------------------------

			Label(self.w2,text="     ").grid(row=7,column=1)
			Label(self.w2,text="     ").grid(row=10,column=0)
			but5=Button(self.w2,text="   EXIT   ",bg="gray",fg="white",font='Times 10  ',cursor='plus',command=self.quit)
			but5.grid(row=10,column=2)
			modify=Button(self.w2,text=" Update ",bg="blue",fg="white",font='Times 10  ',cursor='plus',command=self.update_)
			modify.grid(row=8,column=1)
			rep=Button(self.w2,text=" Replenish ",bg="blue",fg="white",font='Times 10  ',cursor='plus',command=self.replenish)
			rep.grid(row=8,column=3)
			Label(self.w2,text="     ").grid(row=9,column=1)
			
			self.w2.mainloop()
			

		c=0
		if self.e1.get() == '' or self.e2.get() == '':
			c=-1
		else:

			con=p.connect("localhost","root","","storemngt")
			cur=con.cursor()
			q="select * from login where userid='%s'"
			cur.execute(q%(self.e1.get()))
			self.data=cur.fetchone()
			if self.data : 
				l=list(self.data)
			
				if l[1] != self.e2.get():
					c=-1
				else :
					tkinter.messagebox.showinfo("LOGIN", "Login Successfull")
				
					Module.__shop_id=self.e1.get()

					self.e1.delete(0, 'end')
					self.e2.delete(0, 'end')
					verify()
			else:
				c=-1

		if c==-1:
			tkinter.messagebox.showerror("Error","Oops!! Invalid User ID or Password !!")		
			self.e1.delete(0,'end')
			self.e2.delete(0,'end')
	
	def quit(self):
		self.w2.destroy()			


	def signin(self):
		self.w.withdraw()
		self.w1=Tk()
		self.w1.geometry('800x600')
		self.w1.title('SignIn')
	
		h=Label(self.w1,text="NEW USER ? REGISTER NOW !! ",font="Times 14 bold")
		h.grid(row=0,column=2)
		s_id=Label(self.w1,text="ShopID ",font="Times 12",padx=10,pady=10).grid(row=2,column=0)
		s_pas=Label(self.w1,text="Password ",font="Times 12",padx=10,pady=10).grid(row=4,column=0)
		s_name=Label(self.w1,text="Shop Name ",font="Times 12",padx=10,pady=10).grid(row=6,column=0)
		s_cap=Label(self.w1,text="Store Capacity",font="Times 12",padx=10,pady=10).grid(row=8,column=0)
		shelf=Label(self.w1,text="Shelf Capacity",font="Times 12",padx=10,pady=10).grid(row=10,column=0)
		types=Label(self.w1,text="Types of Shelf",font="Times 12",padx=10,pady=10).grid(row=12,column=0)
		self.ne=Entry(self.w1)
		self.ne.grid(row=2,column=1)
		self.pas=Entry(self.w1,show='*')
		self.pas.grid(row=4,column=1)
		self.pe=Entry(self.w1)
		self.pe.grid(row=6,column=1)
		self.ee=Entry(self.w1)
		self.ee.grid(row=8,column=1)
		self.sce=Entry(self.w1)
		self.sce.grid(row=10,column=1)
		self.shlfe=Entry(self.w1)
		self.shlfe.grid(row=12,column=1)
		bb1=Button(self.w1,text="SIGNIN",bg="blue",fg="white",font='Times 10 ',cursor='plus', command=self.register)
		bb1.grid(row=13,column=2)
		
		bb2=Button(self.w1,text="BACK",cursor='plus',command=self.backk)
		bb2.grid(row=14,column=3)

		self.w1.mainloop()
		
	def backk(self):
		self.w.update()	
		self.w.deiconify()
		self.w1.destroy()

	def exitt(self):
		self.a.destroy()

	

	def back(self):
		self.w2.update()	
		self.w2.deiconify()
		self.a.destroy()
		
	def replenish(self):
		con=p.connect("localhost","root","","storemngt")
		cur=con.cursor()
		shelf_no=int(self.tkvar.get()[-1])
		q1="select shelf_capacity from signup where userid='%s'"
		cur.execute(q1%(Module.__shop_id))
		self.caps=cur.fetchone()
		max_cap=self.caps[0]

		q="select current_capacity from store where userid='%s'"
		cur.execute(q%(Module.__shop_id))
		self.Data=cur.fetchone()
		curr=self.Data[0] 
		curr=curr[0:].split(',')
		amount=int(max_cap)-int(curr[shelf_no-1])
		if amount>0:
			tkinter.messagebox.showinfo("Replenishment Amount", "You need {} Quantities to replenish {}  ".format(str(amount),self.tkvar.get()))
		else:
			tkinter.messagebox.showinfo("Replenishment Amount","Shelf reached maximum limit !")
		con.close()
		
	def update_(self):
		
		self.w2.withdraw()
		self.a=Tk()
		self.a.geometry('600x400')
		self.a.title('Modify')
		d1=Label(self.a,text="Modify Details !! ",font="Times 14 bold")
		d1.grid(row=1,column=2)
		Label(self.a,text="     ").grid(row=2,column=1)
		
		#------------------------------------------------------------------
		con=p.connect("localhost","root","","storemngt")
		cur=con.cursor()
		q="select types_of_shelf from signup where userid='%s'"
		cur.execute(q%(Module.__shop_id))
		self.Data=cur.fetchone()
		num_shelf=self.Data[0]
		con.close()
		choices=[]
		for i in range(int(num_shelf)):
			choices.append("Shelf "+str(i+1))
		#------------------------------------------------------------------
		self.tkvar1=StringVar(self.a)
		
		self.tkvar1.set(choices[0]) # set the default option
		popupMenu = OptionMenu(self.a, self.tkvar1, *choices)
		popupMenu.config(width=50)
		Label(self.a, text="Choose the Shelf ", font="Times 12").grid(row = 3, column = 1)
		popupMenu.grid(row = 3, column =2)
		Label(self.a,text="     ").grid(row=4,column=2)
		l1=Label(self.a,text='Enter the value to be added: ',font="Times 12",padx=10,pady=10)
		l1.grid(row=5,column=1)
			
		self.E1=Entry(self.a)
		self.E1.grid(row=5,column=2)
		Label(self.a,text="     ").grid(row=6,column=2)
		labelTest = Label(self.a,text="", font=('Helvetica', 12), fg='red')
		labelTest.grid(row=7,column=2)

		def callback(*args):
			    labelTest.configure(text="The {} is selected  ".format(self.tkvar1.get()))

		self.tkvar1.trace("w", callback)

		Label(self.a,text="     ").grid(row=8,column=2)
		B3=Button(self.a,text=" MODIFY ",cursor='plus',bg="blue",fg="white",font='Times 10',command=self.modify)
		B3.grid(row=9,column=2)
		Label(self.a,text="     ").grid(row=10,column=2)
		
		B2=Button(self.a,text="BACK",cursor='plus',bg="gray",font='Times 10',command=self.back)
		B2.grid(row=11,column=1)

		B1=Button(self.a,text="EXIT",cursor='plus',bg="gray",font='Times 10',command=self.exitt)
		B1.grid(row=11,column=3)

		self.a.mainloop()

	def modify(self):

		con=p.connect("localhost","root","","storemngt")
		cur=con.cursor()
		idx=int(self.tkvar1.get()[-1])

		q="select current_capacity from store where userid='%s'"
		cur.execute(q%(Module.__shop_id))
		self.val=cur.fetchone()
		curr=self.val[0] 
		curr=curr[0:].split(',')
		shelf=int(curr[idx-1])
		q1="select shelf_capacity from signup where userid='%s'"
		cur.execute(q1%(Module.__shop_id))
		self.caps=cur.fetchone()
	
		cap=int(self.caps[0])
		print(cap,':',self.E1.get())
		if (shelf+int(self.E1.get()))>cap:
			tkinter.messagebox.showerror("Error"," Shelf Capacity exceeded !!")		
			self.E1.delete(0,'end')
		else:
		
			q="select current_capacity from store where userid='%s'"
			cur.execute(q%(Module.__shop_id))
			self.Data=cur.fetchone()
			curr=self.Data[0] 
			curr=curr[0:].split(',')
			curr[idx-1]=str(int(self.E1.get())+int(curr[idx-1]))
			curr=",".join(curr)
			q="update store set current_capacity='%s' where userid='%s'"
			cur.execute(q %(curr,Module.__shop_id))
			con.commit()
			tkinter.messagebox.showinfo("Success", "Updated Successfully !!")

		con.close()
			
	

	def __init__(self):

		self.p1=None
		
		self.w=Tk()
		self.w.geometry('1000x500')
		self.data=tuple()
		self.w.title("Welcome")
		self.frame1=Frame(self.w)
		self.frame1.pack()
		self.frame2=Frame(self.w)
		self.frame2.pack()
		self.password=StringVar()
		
		l=Label(self.frame1,text="WELCOME !! TO STORE REPLENISHMENT SYSTEM ",font="Helvetica 16 bold")
		
		l1=Label(self.frame1,text="ShopID",font="Times 14 bold",padx=10,pady=10)
		l2=Label(self.frame1,text="Password",font="Times 14 bold",padx=10,pady=10)
		photo=PhotoImage(file='tenor.gif')
		label=Label(self.frame1,image=photo)
		label.grid(row=0,column=0)

		self.e1=Entry(self.frame1)

		self.e2=Entry(self.frame1,textvariable=self.password,show='*')
	
		b1=Button(self.frame2,text="LOGIN",bg="blue",fg="white",font='Times 10 bold',cursor='plus', command=self.login)
		nu=Label(self.frame2,text="    New User?",fg="blue",font='Times 12 bold')
		b2=Button(self.frame2,text="SIGN IN",bg="blue",fg="white",font='Times 10 bold',cursor='plus', command=self.signin)
		
		l.grid(row=0,column=1)
		l1.grid(row=2,column=0)
		l2.grid(row=3,column=0)
		self.e1.grid(row=2,column=1)
		self.e2.grid(row=3,column=1)
		nu.grid(row=6,column=2)
		b1.grid(row=6,column=1)
		b2.grid(row=6,column=3)
		self.w.mainloop()
Module()