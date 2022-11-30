import socket
from tkinter import *
from PyQt5.QtGui import QPixmap
import sys,time
from PyQt5.QtWidgets import *
from threading import Thread

def addApp():
    d = 'app'+e1.get()
    print(d)
    conn.send(d.encode())
    e1.delete(0,END)

def removeApp():
    d = 'removeapp'+e2.get()
    print(d)
    conn.send(d.encode())
    e2.delete(0,END)

def lock():
    conn.send(b'lock')

def unlock():
    conn.send(b'unlock')

def timer():
    val = 't'+hrs.get()+mins.get()+sec.get()
    conn.send(val.encode())

def quit():
    conn.send(b'quit')
    app.destroy()
    conn.close()

def scr():
    conn.send(b'img')
    Qapp = QApplication(sys.argv)
    pixmap = QPixmap()
    l = QLabel()
    l.setGeometry(1000,1000,700,700)

    def server():
        while True:
            try:   
                global B_img                                     
                B_img = conn.recv(9999999)
                pixmap.loadFromData(B_img)
                l.setScaledContents(True)
                l.resize(l.width(), l.height())
                l.setPixmap(pixmap)
            except:
                print("Disconnected ...",addr)
                break  

    l.move(100,20)
    Thread(target=server, daemon=True).start()
    l.show()
    Qapp.exec()
    # sys.exit(Qapp.exec_())

def window2():
   Client_frame.pack(expand=True,fill='both')

def server():
    global conn,addr
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    s.bind((host,4000))
    s.listen()
    print('Listening. . .')
    conn,addr = s.accept()
    
    client_info = socket.gethostbyaddr(addr[0])
    print(conn,addr,client_info,end='\n')

    msg.config(text=f'{client_info[0]} connected,IP : {client_info[2]}')
    NoLabel.destroy()
    global img
    img = PhotoImage(file='D:\Python\Py Projects\Assets\Administrator.png').subsample(5,5)
    Button(frame,image=img,text=client_info[0],relief='solid',overrelief='solid',bg='#fff',foreground='#000',command=window2).pack(pady=10)
    time.sleep(2)
    window2()
    msg.destroy()

Thread(target=server,daemon=True).start()
app = Tk()
app.state('zoomed')
# app.resizable(False,False)
app.geometry('1300x700')
app.config(bg='grey')
Label(app,text='List of Connected Devices').pack(pady=10,fill='x')
frame = Frame(app,background='#555',highlightbackground='skyblue',highlightthickness=2)
msg = Message(frame,text='Waiting For Client Request...',font=('bold',12),background='lightgreen',justify='center',highlightbackground='skyblue',highlightthickness=2,width=5000)
msg.pack(pady=100)
NoLabel = Label(frame,text='No Device is connected')
NoLabel.pack()
frame.pack(fill='both',expand=1,padx=16,pady=10)

Client_frame = Frame(app,background='#444',highlightbackground='pink',highlightthickness=2)
# Button(Client_frame,text='X',foreground='#888',bg='#111',command=Client_frame.destroy).place(x=2,y=2)
fra_time = Frame(Client_frame, highlightbackground="red", highlightthickness=2, background='#222', )

hrs= StringVar()
mins= StringVar()
sec = StringVar()
Entry(fra_time, textvariable = hrs, width =2, font = 'Jost 14', relief='flat', insertbackground='#FFF', background='#222', foreground='#fff' ).pack(side = LEFT)
Label(fra_time,text=':',bg='#222',foreground='red').pack(side = LEFT)
Entry(fra_time, textvariable = mins, width =2, font = 'Jost 14', relief='flat', insertbackground='#FFF', background='#222', foreground='#fff' ).pack(side = LEFT)
Label(fra_time,text=':',bg='#222',foreground='red').pack(side = LEFT)
Entry(fra_time, textvariable=sec, width = 2, font = 'Jost 14', relief='flat', insertbackground='#FFF', background='#222', foreground='#fff' ).pack(side = LEFT)
hrs.set('00')
mins.set('00')
sec.set('00')

fra_time.place(x=800,y=10)

Button(Client_frame,text='Set Timer',relief='solid',overrelief='solid',width=12,bg='#4A7A8C',foreground='#fff',command=timer).place(x=930,y=11)
Button(Client_frame,text='Screen cast',relief='solid',overrelief='solid',width=60,height=2,bg='#4A7A8C',foreground='#fff',command=scr).pack(pady=60)
Button(Client_frame,text='Lock',relief='solid',overrelief='solid',width=60,height=2,bg='#4A7A8C',foreground='#fff',command=lock).pack(pady=5)
Button(Client_frame,text='Unlock',relief='solid',overrelief='solid',width=60,height=2,bg='#4A7A8C',foreground='#fff',command=unlock).pack(pady=8)

e1 = Entry(Client_frame, width = 38, font = 'Jost 14', relief='flat', background='#444', foreground='#fff', highlightbackground='#fff', highlightthickness=3, highlightcolor='green' )
e1.pack(pady=8)
Button(Client_frame,text='Add Application',relief='solid',overrelief='solid',width=60,height=2,bg='#4A7A8C',foreground='#fff',command=addApp).pack(pady=10)
e2 = Entry(Client_frame, width = 38, font = 'Jost 14', relief='flat', background='#444', foreground='#fff', highlightbackground='#fff', highlightthickness=3, highlightcolor='green' )
e2.pack(pady=8)
Button(Client_frame,text='Remove Application',relief='solid',overrelief='solid',width=60,height=2,bg='#4A7A8C',foreground='#fff',command=removeApp).pack(pady=0)
# Client_frame.pack(expand=True,fill='both',padx=16)
# Client_frame.place(x=100,y=200)

mainloop()