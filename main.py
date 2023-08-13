import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import scrolledtext
import mysql.connector
import datetime
import resident
import admin

name=""
passwd=""
count = 0
dat = [()]
email = ""

f = mysql.connector.connect(host = "localhost", user = "root", passwd = "", database = "MyHome")
mycur = f.cursor()
 
def signin():
# authenticate an existing user

	global name
	global passwd
	global dat
	global email

	master = tk.Tk()
	master.geometry('400x200') 
	master.configure(background='pink')
	master.title("Facilities")

	lblname = Label(master, text="Username")
	lblname.grid(column=2, row=3, padx=70, pady=10)

	lblpwd = Label(master, text="Password")
	lblpwd.grid(column=2, row=5, pady=10)

	txtname = tk.Entry(master)
	txtpwd = tk.Entry(master, show="*")

	txtname.grid(row=3, column=3)
	txtpwd.grid(row=5, column=3)

	txtname.focus()
	
	def login():
		global count
		global name
		global passwd
		global dat
		name = txtname.get()
		passwd = txtpwd.get()

		st="select * from residents where USERNAME = '{}' and PASSWORD = '{}'".format(name, passwd)
		mycur.execute(st)
		dat = mycur.fetchall()
		if dat == []:
			messagebox.showinfo("Failure", "You have entered a wrong username or password")
			master.destroy()
			signin()
		else:
			master.destroy()
   
			for line in dat:
				isadmin = line[5]

			if isadmin == "Yes":
				admin.admin_welcome(mycur)
			else:
				resident.resident_welcome(line[3], mycur)

	button2 = tk.Button(master,text="Login",fg="black",width=15, height=1, command=login).place(x=150, y=100)

	button3 = tk.Button(master,text="New User Signup",fg="black",width=15, height=1, command=signup).place(x=150, y=150)
 
	master.mainloop()

def signup():
# Create a new user account
	master = tk.Tk()
	master.geometry('450x300') 
	master.configure(background='pink')
	master.title("New User Sign up")

	lblname = Label(master, text="Username")
	lblname.grid(column=1, row=1, padx=70, pady=2)

	lblpwd = Label(master, text="Password")
	lblpwd.grid(column=1, row=2, padx=70, pady=2)

	lblunit = Label(master, text="Unit number")
	lblunit.grid(column=1, row=3, padx=70, pady=2)

	lblemail = Label(master, text="Email")
	lblemail.grid(column=1, row=4, padx=70, pady=2)

	lblphone = Label(master, text="Phone number")
	lblphone.grid(column=1, row=5, padx=70, pady=2)

	txtname = tk.Entry(master)
	txtpwd = tk.Entry(master, show= "*")
	txtunit = tk.Entry(master)
	txtemail = tk.Entry(master)
	txtphone = tk.Entry(master)
	txtpwd1 = tk.Entry(master, show="+")

	txtname.grid(row=1, column=2, padx=10, pady=5)
	txtpwd.grid(row=2, column=2, padx=10, pady=5)
	txtunit.grid(row=3, column=2, padx=10, pady=5)
	txtemail.grid(row=4, column=2, padx=10, pady=5)
	txtphone.grid(row=5, column=2, padx=10, pady=5)
 
	

	def submit_request():
		mycur.execute("insert into PendingApprovals(USERNAME, PASSWORD, UNITNO, EMAIL, PHONENO)values('{}','{}','{}','{}','{}')".format(txtname.get(), txtpwd.get(), txtunit.get(), txtemail.get(), txtphone.get()))
		messagebox.showinfo("Sucess!!", "Your request has been sent to the admin.")
		master.destroy()
  
	button2 = tk.Button(master,text="Submit Request",fg="black",width=15, height=1, command=submit_request).place(x=170, y=160)
 
	def cancel():
		master.destroy()

	button3 = tk.Button(master,text="Cancel",fg="black",width=15, height=1, command=cancel).place(x=170, y=200)

	master.mainloop()
 
signin()