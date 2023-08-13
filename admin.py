import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
import mysql.connector
import datetime
from datetime import date

def admin_welcome(mycur):
    event = tk.Tk()
    event.geometry('500x500')
    event.configure(background="pink")
    event.title("Administrative Console")
    head = Label(event, text= "Pending Approvals: ")
    head.pack(pady=5)
    
    mycur.execute("select * from PendingApprovals;")
    approvals = mycur.fetchall()

    lb = Listbox(event, width=60)
    lb.pack()
    #lb.insert(END, "User name   Unit No   Email Address   Contact Number")
    
    temp = ""
    for line in approvals:
        for i in [0, 2, 3, 4]:
            temp = temp + "   " + line[i]
        lb.insert(END, temp)
        temp =""
        
    def reject():
        selection = lb.curselection()
        value = lb.get(selection[0])
        ll = value.split(sep="   ")
        email = ll[3]
        mycur.execute("delete from PendingApprovals where EMAIL = '{}'".format(email))
        lb.delete(tk.ACTIVE)
        
    def approve():
        selection = lb.curselection()
        value = lb.get(selection[0])
        ll = value.split(sep="   ")
        user = ll[1]        
        unit = ll[2]
        
        mycur.execute("select PASSWORD from PendingApprovals where email = '{}'".format(ll[3]))
        pas = mycur.fetchall()
        for i in pas:
            pasw = i[0]
        email = ll[3]
        phone = ll[4]
        isadmin = "No"
        
        mycur.execute("delete from PendingApprovals where EMAIL = '{}'".format(email))  
        mycur.execute("insert into residents(USERNAME, PASSWORD, UNITNO, EMAIL, PHONENO, ISADMIN)values('{}','{}','{}','{}','{}','{}')".format(user,pasw,unit,email,phone,isadmin))
        lb.delete(tk.ACTIVE)

    def facility_management():
        f = tk.Tk()
        f.geometry('400x400')
        f.configure(background="pink")
        f.title("Facilities Management")
        head = Label(f, text= "All facilities: ")
        head.pack(pady=5)
        
        mycur.execute("select * from facilities;")
        facilities = mycur.fetchall()
        lb = Listbox(f, width=100)
        lb.pack()
        temp = ""
        for line in facilities:
            for i in range(0,2):
                temp = temp + "   " + line[i]
            lb.insert(END, temp)
            temp =""
        def remove_facility():
            selection = lb.curselection()
            value = lb.get(selection[0])
            ll = value.split(sep="   ")
            name = ll[1]
            mycur.execute("delete from facilities where NAME = '{}'".format(name))
            messagebox.showinfo("Success", "The facility has been removed")
            lb.delete(tk.ACTIVE)
            f.lift()
            
        def add_facility():
            add = tk.Tk()
            add.geometry('500x500')
            add.configure(background="pink")
            add.title("Add a new facility")
            
            lblname = Label(add, text="Facility name")
            lblname.pack(pady=5)
            txtname = tk.Entry(add)
            txtname.pack(pady=5)
            
            lbldes = Label(add, text="Description")
            lbldes.pack(pady=5)
            txtdes = tk.Entry(add)
            txtdes.pack(pady=5)
            
            def add_db():
                mycur.execute("insert into facilities(NAME, DESCRIPTION)values('{}','{}')".format(txtname.get(), txtdes.get()))
                messagebox.showinfo("Success", "The facility has been added successfully")
                lb.insert(END, "      " + txtname.get() + "      " + txtdes.get())
                add.destroy()
                f.lift()
                
            add_facility = tk.Button(add,text="Confirm",fg="black",width=20, height=1, command=add_db)
            add_facility.pack(pady=10)
            
            def cancel():
                add.destroy()
                
            cancel_facility = tk.Button(add,text="Cancel",fg="black",width=20, height=1, command=cancel)
            cancel_facility.pack(pady=10)
            
        def bookings():
            add = tk.Tk()
            add.geometry('500x700')
            add.configure(background="pink")
            add.title("Bookings")

            today = datetime.date.today()
            one_day = datetime.timedelta(days=1) 
            
            mycur.execute("select * from bookings order by date DESC;")
            bookings = mycur.fetchall()
            lb = Listbox(add, width=60, height= 100)
            lb.pack()
            temp = ""
            for line in bookings:
                d = line[2].strftime("%y-%m-%d")
                temp =  line[0] + "     " + line[1] + "      " + d
                lb.insert(END, temp)
                temp =""
            

            
        remove_f = tk.Button(f,text="Remove facility",fg="black",width=20, height=1, command=remove_facility)
        remove_f.pack(pady=5)
        
        add_facility = tk.Button(f,text="Add facility",fg="black",width=20, height=1, command=add_facility)
        add_facility.pack(pady=5)
        
        view_bookings = tk.Button(f,text="View Bookings",fg="black",width=20, height=1, command=bookings)
        view_bookings.pack(pady=5)
        
        def cancel():
            f.destroy()
            
        cancel_b = tk.Button(f,text="Cancel",fg="black",width=20, height=1, command=cancel)
        cancel_b.pack(pady=5)

        
    def residents():
        residents = tk.Tk()
        residents.geometry('500x500')
        residents.configure(background="pink")
        residents.title("Residents Management")
        head = Label(residents, text= "Active Residents: ")
        head.pack(pady=5)
        
        mycur.execute("select * from residents;")
        ppl = mycur.fetchall()
        lb = Listbox(residents, width=60)
        lb.pack(pady=5)
        temp = ""
        for line in ppl:
            for i in [0,2,3,4]:
                temp = temp + "   " + line[i]
            lb.insert(END, temp)
            temp =""
            
        def remove_residents():
            selection = lb.curselection()
            value = lb.get(selection[0])
            ll = value.split(sep="   ")
            name = ll[1]
            mycur.execute("delete from residents where USERNAME = '{}'".format(name))
            messagebox.showinfo("Success", "The selected resident has been removed")
            lb.delete(tk.ACTIVE)
            residents.lift()
            
        remove_resident = tk.Button(residents,text="Remove resident",fg="black",width=20, height=1, command=remove_residents)
        remove_resident.pack(pady=5)
        
        def done_res():
            residents.destroy()
            
        done = tk.Button(residents,text="Done",fg="black",width=20, height=1, command=done_res)
        done.pack(pady=5)

    remove_button = tk.Button(event,text="Reject",fg="black",width=20, height=1, command=reject)
    remove_button.pack(pady=5)
    
    add_button = tk.Button(event,text="Approve",fg="black",width=20, height=1, command = approve)#.place(x=100, y=100)
    add_button.pack(pady=5)
    
    faculty_management = tk.Button(event,text="Facility Management",fg="black",width=20, height=1, command=facility_management)
    faculty_management.pack(pady=5)
    
    resident_management = tk.Button(event,text="Resident Management",fg="black",width=20, height=1, command=residents)
    resident_management.pack(pady=5)
    
    def signout():
        mycur.execute("Commit;")
        event.destroy()
    des_button = tk.Button(event,text="Sign Out",fg="black",width=20, height=1, command=signout)
    des_button.pack(pady=5)
    
    event.mainloop()    

