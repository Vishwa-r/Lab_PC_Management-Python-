from tkinter import *
from tkinter import messagebox
import mysql.connector

def MainScreen():

     Splash.destroy()

     # mydb = mysql.connector.connect(
     # host="localhost",
     # user="root",
     # password="root",
     # database="mini"
     # )

     def Register():   

          pname = e1.get()
          ppass = e2.get()
          
          # mycursor = mydb.cursor()
          # sql = "SELECT * FROM details WHERE reg_no =%s and password = %s"
          # mycursor.execute(sql,[(pname),(ppass)])

          myresult = True# mycursor.fetchall()
          
          if myresult:
               Label(app, text=f'{pname}, Login SuccessFully!', pady=20, bg='#ffbf00').grid(row=6,column=1,pady=28)     #.place(x=820,y=400)
               app.destroy()
               import Home
          else:
               # t.Label(app, text=f'{pname}, Login unSuccessFull', pady=20, bg='#ffbf00').grid(row=6,column=1,pady=28)
               messagebox.showerror(''," Login Unsuccessful \n Incorrect Password and Reg.no")

          

     app = Tk()
     app.config( bg= "#000")
     app.title("Login")
     h = app.winfo_height()
     w = app.winfo_width()
     app.geometry(f'{h}x{w}')
     # app.attributes('-alpha',0.9)
     app.state('zoomed')

     border = Frame(app,highlightbackground='red',highlightthickness=1.3,bd=0)

     l1 = Label(text="Login",height=2,width=0,bg= "#000",fg="#fff",font=('bold',30))
     l1.grid(row=0,column=9,sticky=N)
     # l1.pack(fill= t.Y,side=t.TOP)

     # Name & Reg.no
     Name = Label(text="Register Number",bg= "#001",fg="#fff",font=('bold',14))
     e1=Entry(relief='flat',
          border=0,
          borderwidth=0,
          background='#333',
          foreground='red',
          highlightbackground='red',
          highlightthickness=1,
          insertbackground='#FFF',
          insertwidth=0,
          selectbackground='#777',
     )


     Name.grid(row=1,column=0)
     e1.grid(row=1,column=1,ipadx=20)

     RegNo = Label(text="Password",bg= "#001",fg="#fff",font=('bold',14))
     e2=Entry(
          relief='flat',
          border=0,
          borderwidth=0,
          background='#333',
          foreground='red',
          highlightbackground='red',
          highlightthickness=1,
          insertbackground='#FFF',
          insertwidth=0,
          selectbackground='#777',
          show='*'
     )

     RegNo.grid(row=2,column=0)
     e2.grid(row=2,column=1,ipadx=40)

     # Submit Button
     def onEnter(e):
          btn['background']='#111'       # OnHover bg Color
          btn['foreground']='red'       # OnHover Text Color


     def onLeave(e):
          btn['background']='red'
          btn['foreground']='#111'


     btn = Button(text="Register",bg= "red",fg="#111",height=1,width=20,relief="flat",highlightbackground='red',highlightthickness=1,activebackground='#111',border=0,borderwidth=0,command=Register)
     btn.grid(row=5,column=1,pady=28)
     btn.bind('<Enter>',onEnter)
     btn.bind('<Leave>',onLeave)

     border.grid(sticky=W)

     l1.place(x=960,y=30,anchor= "n")
     Name.place(x=740, y=200)
     RegNo.place(x=740, y=260)
     e1.place(x=960, y=200)
     e2.place(x=960, y=260)
     btn.place(x=900, y=360)

     app.mainloop()


Splash = Tk()
Splash.geometry('1920x1080')
Splash.state('zoomed')
Splash.overrideredirect(True)


Lb_img = PhotoImage(file=r"C:/Users/Vishwa/Pictures/Guru-Nanak-College-Logo.png").subsample(1,1).zoom(1,1)
Label(image=Lb_img).pack(pady=400)

Splash.after(1000,MainScreen)

Splash.mainloop()
