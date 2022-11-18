from tkinter import *
from PIL import ImageTk,Image
window=Tk()
# add widgets here
def front_page():
    window.destroy()
    import front_page

def loginPage():
    window.destroy()
    import login
def book_apnmnt():
    window.destroy()
    import book_apnmnt
window.title('Home Page')
window.geometry("1500x1700")
window.configure(bg='gray')
frame=Frame(window,bd=400,height=150,width=1700,bg="skyblue")##HEADLINE FRAME
photo=ImageTk.PhotoImage(Image.open("C:/Users/UMA/Desktop/Hospital_project/logo.jpg"))##LOGO IMAGE
pic1=Label(image=photo,height=145,width=200)
pic1.place(x=43,y=0)
##MENUBAR
frame=Frame(window,bd=5,height=20,width=1500,bg="skyblue")
Button(window,text="Home",font=("Ariel",13,'bold'),fg='skyblue',bg='green',command=front_page).place(x=350,y=120)
mb2=Menubutton(window,text="Department",font=("Ariel",13,"bold"),fg="skyblue",bg="green")
mb3=Menubutton(window,text="About Us",font=("Ariel",13,"bold"),fg="skyblue",bg="green")
mb4=Menubutton(window,text="Contact Us",font=("Ariel",13,"bold"),fg="skyblue",bg="green")
Button(window,text="Login",font=("Ariel",13,'bold'),fg='skyblue',bg='green',command=loginPage).place(x=1400,y=120)
mb2.menu=Menu(mb2,bg='skyblue',font=('times new roman',15,'bold'))
mb2["menu"]=mb2.menu
mb2.menu.add_command(label="ENT")
mb2.menu.add_command(label="Gynaecology")
mb2.menu.add_command(label="Cardiology")
mb2.menu.add_command(label="Neurology",)
mb2.place(x=450,y=120)
mb3.menu=Menu(mb3)
mb3["menu"]=mb3.menu
mb3.menu.add_command(label="")
mb3.place(x=600,y=120)
mb4.menu=Menu(mb4)
mb4["menu"]=mb4.menu
mb4.menu.add_command(label="")
mb4.place(x=740,y=120)
frame.place(x=0,y=0)
photo1=ImageTk.PhotoImage(Image.open("C:/Users/UMA/Desktop/Hospital_project/hom2.jpg"))#frond_image
pic=Label(image=photo1,height=540,width=1980)
##LOGIN PAGE
frame=Frame(window,bd=100,height=540,width=480)
Label(window,text="Find A Doctor & \n Book Appoinment",fg="green",font=("Times new roman",26,'bold')).place(x=30,y=250)
Button(window,text="Make An Appoinment",bg="gray",bd=2,font=("Times new roman",15,'bold'),fg='brown',command=book_apnmnt).place(x=60,y=400)
Button(window,text="About us",bg="gray",bd=2,font=("Times new roman",15,'bold'),fg='brown',relief=RAISED).place(x=290,y=400)
# Label(window,text="LOGIN HERE",font=("Ariel",20,"bold"),width=20,fg="green").place(x=-30,y=220)
# Label(window,text="USER NAME",fg="black",font=("Ariel",10,"bold")).place(x=50,y=300)
# e1=Entry(window,bd=3,bg="gray").place(x=138,y=300)
# Label(window,text="PASSWORD",fg="black",font=("Ariel",10,"bold")).place(x=50,y=350)
# e2=Entry(window,bd=3,bg="gray",show='*').place(x=138,y=350)
# Button(window,text="SUBMIT",bd=2,bg="sky blue",fg="blue",font=("Ariel",13,"bold")).place(x=100,y=400)
frame.place(x=10,y=150)
pic.place(x=0,y=150)
#

window.mainloop()
