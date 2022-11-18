from tkinter import *

ws = Tk()
ws.geometry('400x300')
ws.title('PythonGuides')
ws['bg'] = '#5d8a82'

f = ("Times bold", 14)


def nextPage():
    ws.destroy()
    import login


def prevPage():
    ws.destroy()
    import admin_panel


Label(ws, text="This is First page",padx=20,
    pady=20,
    bg='#5d8a82',
    font=f
).pack(expand=True, fill=BOTH)

Button(
    ws,
    text="Login here",
    font=f,
    command=nextPage
).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    ws,
    text="Next Page",
    font=f,
    command=''
).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()