from tkinter import *
from PIL import ImageTk,Image
window=Tk()
# add widgets here
def doctor_manage():
    # window.destroy()
    import doctor_manage
def frond_page():
    # window.destroy()
    import front_page
window.geometry("1500x1700")
window.configure(bg='gray')
frame=Frame(window,bd=400,height=150,width=1700,bg="skyblue")##HEADLINE FRAME
photo=ImageTk.PhotoImage(Image.open("C:/Users/UMA/Desktop/Hospital_project/logo.jpg"))##LOGO IMAGE
pic1=Label(image=photo,height=145,width=200)
pic1.place(x=43,y=0)
##MENUBAR
frame=Frame(window,bd=5,height=20,width=1500,bg="skyblue")
Button(window,text="Back To Home",font=("Ariel",13,'bold'),fg='skyblue',bg='green',command=frond_page).place(x=350,y=120)
frame.place(x=0,y=0)
frame=Frame(window,bd=100,height=540,width=1980)
Label(window,text="MANAGE DOCTORS",font=('Ariel',20,'bold'),bg='skyblue',padx=500,pady=10).place(x=80,y=220)
Label(window,text="NAME",fg="black",font=("Ariel",15,"bold")).place(x=500,y=300)
e1=Entry(window,bd=3,bg="gray").place(x=600,y=300)
Label(window,text="Specialization",fg="black",font=("Ariel",15,"bold")).place(x=800,y=300)
e2=Entry(window,bd=3,bg="gray").place(x=900,y=300)
Label(window,text="Contact",fg="black",font=("Ariel",15,"bold")).place(x=500,y=350)
e3=Entry(window,bd=3,bg="gray").place(x=600,y=350)

Button(window,text="SUBMIT",bd=2,bg="sky blue",fg="blue",font=("Ariel",13,"bold")).place(x=580,y=550)

frame.place(x=0,y=150)

window.mainloop()
