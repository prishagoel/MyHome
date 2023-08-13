import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
#from tkinter import scrolledtext
import mysql.connector
import datetime
from datetime import date

name=""
passwd=""
cur = ""
em = ""
lb = ""

def resident_welcome(email, mycur):
    global cur
    global em
    global lb
    cur = mycur
    em=email
    event = tk.Tk()
    event.geometry('500x400')
    event.configure(background="pink")
    event.title("Resident Homepage")
    head = Label(event, text= "Your bookings: ")
    head.pack(pady=5)
    
    today = datetime.date.today()
    one_day = datetime.timedelta(days=1)       
    
    mycur.execute("select FACILITYNAME, DATE, TIME from bookings where EMAIL = '{}' and DATE > '{}'".format(email, today-one_day))
    bookings = mycur.fetchall()
    lb = Listbox(event, width=45)
    lb.pack()
    
    temp = ""
    # Adding elements in the listbox
    for line in bookings:
        d = line[1].strftime("%y-%m-%d")
        temp =  line[0] + "   " + d  + "   "+ line[2]
        lb.insert(END, temp)
        temp =""
        
    def remove_booking():
        selection = lb.curselection()
        value = lb.get(selection[0])
        ll = value.split("   ")
        facility = ll[1]
        dd = ll[2]
        tt = ll[3]

        mycur.execute("delete from bookings where FACILITYNAME = '{}' and DATE = '{}' and TIME = '{}'".format(facility, dd, tt))
        lb.delete(tk.ACTIVE)
        messagebox.showinfo("Success", "Your booking has been deleted successfully")  


    def signout():
        event.destroy()
        
    remove_button = tk.Button(event,text="Remove this booking",fg="black",width=20, height=1, command=remove_booking)
    remove_button.pack(pady=5)
    
    add_button = tk.Button(event,text="Add a booking",fg="black",width=20, height=1, command = add_booking)
    add_button.pack()
    
    exit_button = tk.Button(event,text="Exit",fg="black",width=20, height=1, command = signout)
    exit_button.pack(pady=10)
    
    event.mainloop()


def add_booking():
    global cur
    mycur = cur
    event = tk.Tk()
    event.geometry('300x250')
    event.configure(background="lightblue")
    event.title("Add new booking")
    head = Label(event, text= "Add a booking: ")
    head.pack(pady=5)
 
    facilities = ttk.Combobox(event, width = 20) 
    mycur.execute("select NAME from facilities;") 
    dat = mycur.fetchall()
    temp = []
    for line in dat:
        temp.append(line[0])
    facilities['values'] = temp

    facilities.pack(pady=5)
    facilities.set("Choose the facility")
    facilities.current() 
    
    today = datetime.date.today()
    one_day = datetime.timedelta(days=1)
    weekset = [today]

    dates = ttk.Combobox(event, width = 20)
    for i in range(0, 7):
        today += one_day
        weekset.append(today)
    dates['values'] = tuple(weekset) 
    dates.set("Choose the date")
    
    timeset = ttk.Combobox(event, width = 20)  
    timeset['values'] = ('8AM to 9AM','9AM to 10AM','10AM to 11AM','11AM to 12PM', '12PM to 1PM', '1PM to 2PM', '2PM to 3PM','3PM to 4PM', '4PM to 5PM','5PM to 6PM','6PM to 7PM','7PM to 8PM') 
    dates.pack(pady=5)
    timeset.pack(pady=5)
    timeset.current()
    timeset.set("Choose the timings")
    dates.current() 
        
  
    
    def add_database():
        global em
        global lb
        opt1 = facilities.get()
        opt2 = dates.get()
        opt3 = timeset.get()
        
        mycur.execute("select EMAIL from bookings where FACILITYNAME = '{}' and DATE = '{}' and TIME = '{}'".format(opt1, opt2, opt3))
        dat = mycur.fetchall()

        if dat == []:
            mycur.execute("insert into bookings(FACILITYNAME, EMAIL, DATE, TIME)values('{}','{}','{}','{}')".format(opt1, em, opt2, opt3))
            messagebox.showinfo("Success!", "Your booking has been made successfully")
            event.destroy()
            temp = "   " + opt1 + "   " + opt2 + "   " + opt3
            lb.insert(END, temp)

        else: 
            email = dat[0][0]
            mycur.execute("select USERNAME from residents where EMAIL = '{}'".format(email))
            dat = mycur.fetchall()
            username = dat[0][0]
            messagebox.showinfo("Failed","Sorry the slot is already booked by '{}'. Please try again with a different slot".format(username))
            event.lift()

            
    
    add_db = tk.Button(event,text="Submit",fg="black",width=20, height=1, command = add_database)
    add_db.pack(pady=10)
    
    def cancel():
        event.destroy()

    cancel_button = tk.Button(event,text="Cancel",fg="black",width=20, height=1, command = cancel)
    cancel_button.pack(pady=10)

    event.mainloop()