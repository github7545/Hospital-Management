from tkinter import *
import pymysql
from PIL import ImageTk,Image
from tkinter import messagebox
window=Tk()
##database connection
connection=pymysql.connect(host="localhost",user="root",password="",database="hospital_mngmnt")
print("conection success")
cursor=connection.cursor()
def admin_login():
    username=e1.get()
    password=e2.get()
    sql="select *from login where username= %s and password =%s"
    cursor.execute(sql,[(username),(password)])
    results=cursor.fetchall()
    # print(results)
    if results:
        messagebox.showinfo("LOGIN SUCCESS","LOGIN SUCCESS")
        # window.destroy()
        import admin_panel
    else:
        messagebox.showinfo("INVALID USERNAME/PASSWORD...TRY AGAIN","INVALID USERNAME/PASSWORD...TRY AGAIN")
        return False

def front_page():
    window.destroy()
    import front_page
window.geometry("1500x1700")
window.configure(bg='gray')
frame=Frame(window,bd=400,height=150,width=1700,bg="skyblue")##HEADLINE FRAME
photo=ImageTk.PhotoImage(Image.open("C:/Users/UMA/Desktop/Hospital_project/logo.jpg"))##LOGO IMAGE
pic=Label(image=photo,height=145,width=200)
pic.place(x=43,y=0)
##MENUBAR
frame=Frame(window,bd=5,height=20,width=1500,bg="skyblue")
Button(window,text="Back To Home",font=("Ariel",13,'bold'),fg='skyblue',bg='green',command=front_page).place(x=350,y=120)

frame.place(x=0,y=0)
frame=Frame(window,bd=100,height=540,width=1980)
global e1
global e2
Label(window,text="LOGIN HERE",font=("Ariel",20,"bold"),width=20,fg="green").place(x=500,y=220)
Label(window,text="USER NAME",fg="black",font=("Ariel",10,"bold")).place(x=500,y=300)
e1=Entry(window,bd=3,bg="gray")
e1.place(x=600,y=300)
Label(window,text="PASSWORD",fg="black",font=("Ariel",10,"bold")).place(x=500,y=350)
e2=Entry(window,bd=3,bg="gray",show='*')
e2.place(x=600,y=350)
Button(window,text="LOGIN",bd=2,bg="sky blue",fg="blue",font=("Ariel",13,"bold"),command=admin_login).place(x=580,y=450)

frame.place(x=0,y=150)

window.mainloop()
