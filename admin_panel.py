from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
window=Tk()
# add widgets here
def front_page():
    # window.destroy()
    import front_page
def doctor_manage():
    # window.destroy()
    import doctor_manage

def appoinment_view():
    # window.destroy()
    import appoinment_view
def patient_view():
    # window.destroy()
    import patient_view
window.geometry("1500x1700")
window.configure(bg='gray')
frame=Frame(window,bd=400,height=150,width=1700,bg="skyblue")##HEADLINE FRAME
photo=ImageTk.PhotoImage(Image.open("C:/Users/UMA/Desktop/Hospital_project/logo.jpg"))##LOGO IMAGE
pic=Label(image=photo,height=145,width=200)
pic.place(x=43,y=0)
##MENUBAR
frame=Frame(window,bd=5,height=20,width=1500,bg="skyblue")
Button(window,text="Back to Page<<",font=("Ariel",13,"bold"),fg="skyblue",bg="green",command=front_page).place(x=350,y=120)
frame.place(x=0,y=0)
frame=Frame(window,bd=100,height=540,width=1980)
Button(window,text="DOCTOR",bd=2,bg="sky blue",fg="blue",font=("Ariel",13,"bold"),command=doctor_manage).place(x=300,y=220)
Button(window,text="PATIENT",bd=2,bg="sky blue",fg="blue",font=("Ariel",13,"bold"),command=patient_view).place(x=500,y=220)
Button(window,text="APPOINMENT",bd=2,bg="sky blue",fg="blue",font=("Ariel",13,"bold"),command=appoinment_view).place(x=300,y=300)
Button(window,text="ABOUT US",bd=2,bg="sky blue",fg="blue",font=("Ariel",13,"bold")).place(x=500,y=300)

frame.place(x=0,y=150)

window.mainloop()
