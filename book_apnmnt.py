from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from tkcalendar import Calendar,DateEntry
##database connection
connection=pymysql.connect(host="localhost",user="root",password="",database="hospital_mngmnt")
print("conection success")
cursor=connection.cursor()
window=Tk()
def front_page():
    window.destroy()
    import front_page
# cursor.execute("CREATE TABLE Appoinment(Patient_name varchar(30),age varchar(20),gender varchar(20),address varchar(50),aptime varchar(30),phone varchar(10))")
window.title("Appoinment form")
pid=StringVar()
n1=StringVar()
a1=StringVar()
opgender=StringVar()
ad1=StringVar()
optime=StringVar()
opdoctor=StringVar()
ph1=StringVar()
app=StringVar()
app_date=StringVar()
def clear():
    n1.set('')
    a1.set('')
    opgender.set('')
    ad1.set('')
    optime.set('')
    opdoctor.set('')
    ph1.set('')
    app_date.delete(0, END)
def submit():
    cursor.execute("INSERT INTO appoinment(patient_id,patient_name,age,gender,address,aptime,doctor,phone,app_date)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                   (pid.get(),
                    n1.get(),
                    a1.get(),
                    opgender.get(),
                    ad1.get(),
                    optime.get(),
                    opdoctor.get(),
                    ph1.get(),
                    app_date.get()
                    ))
    connection.commit()
    messagebox.showinfo("INSERTION SUCCESSFUL","Values Added Successfully")
    # import front_page


def doctor_manage():
    window.destroy()
    import doctor_manage

window.geometry("1500x1700")
window.configure(bg='gray')
frame=Frame(window,bd=400,height=150,width=1700,bg="skyblue")##HEADLINE FRAME
photo=ImageTk.PhotoImage(Image.open("C:/Users/UMA/Desktop/Hospital_project/logo.jpg"))##LOGO IMAGE
pic=Label(image=photo,height=145,width=200)
pic.place(x=43,y=0)
##MENUBAR
frame=Frame(window,bd=5,height=20,width=1500,bg="skyblue")
Button(window,text="Back To Home",font=("Ariel",13,"bold"),command=front_page,fg="skyblue",bg="green")
frame.place(x=0,y=0)
frame=Frame(window,bd=100,height=540,width=1980)
Label(window,text="Appoinment Booking",font=('Ariel',20,'bold'),bg='skyblue',padx=500,pady=10).place(x=80,y=220)
Label(window,text="Patient Name",fg="black",font=("Ariel",12,"bold")).place(x=490,y=300)
e1=Entry(window,bd=3,bg="gray",textvariable=n1,width=20).place(x=600,y=300)
Label(window,text="Age",fg="black",font=("Ariel",12,"bold")).place(x=490,y=350)
e2=Entry(window,bd=3,bg="gray",textvariable=a1,width=20).place(x=600,y=350)
Label(window,text="Gender",fg="black",font=("Ariel",12,"bold")).place(x=490,y=400)
gender_options=("Male","Female","Trans")
gender_options=OptionMenu(window,opgender,*gender_options)
gender_options.config(width=15,bg="gray")
gender_options.place(x=595,y=400)
Label(window,text="Address",fg="black",font=("Ariel",12,"bold")).place(x=490,y=450)
e4=Entry(window,bd=3,bg="gray",textvariable=ad1).place(x=595,y=450)

Label(window,text="Doctor",fg="black",font=("Ariel",12,"bold")).place(x=850,y=300)
doc_options=("Dr.Thomas(ENT)","Dr.Meera(Ortho)")
# optime.set("Time")
doc_options=OptionMenu(window,opdoctor,*doc_options)
doc_options.config(width=15,bg="gray")
doc_options.place(x=990,y=300)
Label(window,text="Appoinment Time",fg="black",font=("Ariel",12,"bold")).place(x=850,y=350)
time_options=("10.30 am","2.30 pm")
# optime.set("Time")
time_options=OptionMenu(window,optime,*time_options)
time_options.config(width=15,bg="gray")
time_options.place(x=990,y=350)


Label(window,text="Contact Number",fg="black",font=("Ariel",12,"bold")).place(x=850,y=450)
e6=Entry(window,bd=3,bg="gray",textvariable=ph1).place(x=990,y=450)

Label(window,text="Appoinment Date",fg="black",font=("Ariel",12,"bold")).place(x=850,y=400)
app_date = DateEntry(window, width= 16,bg="gray",bd=3,foreground= "gray")
app_date.place(x=1000,y=400)
# e6=Entry(window,bd=3,bg="gray",textvariable=app_date).place(x=990,y=450)
Button(window,text="SUBMIT",bd=2,bg="sky blue",fg="blue",font=("Ariel",13,"bold"),command=submit).place(x=580,y=550)
Button(window,text="Clear",bd=2,bg="sky blue",fg="blue",font=("Ariel",13,"bold"),command=clear).place(x=700,y=550)
Button(window,text="Back To Home",bd=2,bg="sky blue",fg="blue",font=("Ariel",13,"bold"),command=front_page).place(x=790,y=550)
frame.place(x=0,y=150)

window.mainloop()
#Import tkinter library
# from tkinter import *
# from tkcalendar import Calendar, DateEntry
# #Create an instance of tkinter frame
# win= Tk()
# #Set the Geometry
# win.geometry("750x250")
# win.title("Date Picker")
# #Create a Label
# Label(win, text= "Choose a Date", background= 'gray61', foreground="white").pack(padx=20,pady=20)
# #Create a Calendar using DateEntry
# cal = DateEntry(win, width= 16, background= "magenta3", foreground= "white",bd=2)
# cal.pack(pady=20)
# win.mainloop()