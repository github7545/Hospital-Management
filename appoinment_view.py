from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
##database connection
connection=pymysql.connect(host="localhost",user="root",password="",database="hospital_mngmnt")
print("conection success")
cursor=connection.cursor()
window=Tk()

def front_page():
    window.destroy()
    import front_page

def admin_panel():
    window.destroy()
    import admin_panel
window.geometry("1500x1700")
window.configure(bg='')

Label(window,text="New Appoinments",font=('Ariel',20,'bold')).grid(row=0,column=0,columnspan=50,pady=100,padx=100)
Label(window,text="Patient\nId",font="time 12 bold",fg='red').grid(row=1,column=0,padx=10,pady=10)
Label(window,text="Patient\nName",font="time 12 bold",fg='red').grid(row=1,column=1,padx=10,pady=10)
Label(window,text="Age",font="time 12 bold",fg='red').grid(row=1,column=2,padx=10,pady=10)
Label(window,text="Gender",font="time 12 bold",fg='red').grid(row=1,column=3,padx=10,pady=10)
Label(window,text="Address",font="time 12 bold",fg='red').grid(row=1,column=4,padx=10,pady=10)
Label(window,text="Appoinment\nTime",font="time 12 bold",fg='red').grid(row=1,column=5,padx=10,pady=10)
Label(window,text="Appoinment\nDate",font="time 12 bold",fg='red').grid(row=1,column=6,padx=10,pady=10)
Label(window,text="Doctor",font="time 12 bold",fg='red').grid(row=1,column=7,padx=10,pady=10)
Label(window,text="Contact\nno",font="time 12 bold",fg='red').grid(row=1,column=8,padx=10,pady=10)
# Label(window,text="Actions",font="time 12 bold",fg='red').grid(row=1,column=9,padx=10,pady=10)


###Fetching
cursor.execute("SELECT * FROM appoinment where approval=0")
result=cursor.fetchall()
num=2

for i in result:


       Id = Label(window, text=i[0], fg="black", font=("Ariel", 12, "bold")).grid(row=num, column=0, padx=10, pady=10)
       Name=Label(window,text=i[1],fg="black",font=("Ariel",12,"bold")).grid(row=num,column=1,padx=10,pady=10)
       Age=Label(window, text=i[2], fg="black", font=("Ariel", 12, "bold")).grid(row=num,column=2,padx=10,pady=10)
       gender = Label(window, text=i[3], fg="black", font=("Ariel", 12, "bold")).grid(row=num,column=3,padx=10,pady=10)
       address = Label(window, text=i[4], fg="black", font=("Ariel", 12, "bold")).grid(row=num,column=4,padx=10,pady=10)
       aptime = Label(window, text=i[5], fg="black", font=("Ariel", 12, "bold")).grid(row=num,column=5,padx=10,pady=10)
       apdate = Label(window, text=i[9], fg="black", font=("Ariel", 12, "bold")).grid(row=num, column=6, padx=10,                                                                            pady=10)
       doctor = Label(window, text=i[6], fg="black", font=("Ariel", 12, "bold")).grid(row=num, column=7, padx=10,                                                                           pady=10)
       ph = Label(window, text=i[7], fg="black", font=("Ariel", 12, "bold")).grid(row=num,column=8,padx=10,pady=10)
       # Button(window,text='Approve',bg='steelblue',command=patient_view(Id)).grid(row=num,column=9,padx=10,pady=10)
       # Button(window, text='Delete',bg='steelblue').grid(row=num, column=9, padx=10, pady=10)
       num=num+1



Button(window,text="Back To Admin Panel",bd=2,bg="sky blue",fg="blue",font=("Ariel",13,"bold"),command=admin_panel).place(x=680,y=700)
# frame.place(x=0,y=150)

window.mainloop()
