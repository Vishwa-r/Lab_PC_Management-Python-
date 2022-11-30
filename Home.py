from tkinter import *
from threading import *
from tkinter import messagebox
import keyboard,socket,io,time,os
from PIL import ImageGrab
from ctypes import windll

h = windll.user32.FindWindowA(b'Shell_TrayWnd', None)

sc2 = Tk()
sc2.state('zoomed')
sc2.resizable(width=False,height=False)
sc2.protocol('WM_DELETE_sc2DOW',None)
sc2.attributes("-fullscreen", True)
sc2.config(bg='#4A7A8C')

def Exit():
    windll.user32.ShowWindow(h, 9)
    sc2.destroy()

btn_Exit = Button(text='Exit',foreground='#888',bg='#111',command= Exit)
btn_Exit.place(x=10,y=10)

fra_time = Frame(sc2, highlightbackground="red", highlightthickness=2, background='#222', )
fra_time.pack()
fra_time.place(x=1800, y=20)

hrs= StringVar()
mins= StringVar()
sec = StringVar()
Entry(fra_time, textvariable = hrs, width =2, font = 'Jost 14', state='disabled', relief='flat', disabledbackground='#222', disabledforeground='#fff' ).pack(side = LEFT)
Label(fra_time,text=':',bg='#222',foreground='red').pack(side = LEFT)
Entry(fra_time, textvariable = mins, width =2, font = 'Jost 14', state='disabled', relief='flat', disabledbackground='#222', disabledforeground='#fff' ).pack(side = LEFT)
Label(fra_time,text=':',bg='#222',foreground='red').pack(side = LEFT)
Entry(fra_time, textvariable=sec, width = 2, font = 'Jost 14', state='disabled', relief='flat', disabledbackground='#222', disabledforeground='#fff' ).pack(side = LEFT)
hrs.set('00')
mins.set('00')
sec.set('00')

hostName = StringVar()

def client():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host = hostName.get() #input('Enter Server Name : ')

    try:
        s.connect((host,4000))
        Label(frame_admin,text=f'Connected to {host}.\n........').pack(pady=20)
    except:
        print(hostName.get(),'is Disconnected')

    def blockKey():
        keyboard.block_key('alt')
        keyboard.block_key('esc')
        keyboard.block_key('win')
        messagebox.showinfo('Block Keys Enabled','ALT & ESCAPE & WIN KEYS are Blocked')
        windll.user32.ShowWindow(h, 0)

    def disblockKey():
        keyboard.unblock_key('alt')
        keyboard.unblock_key('esc')
        keyboard.unblock_key('win')
        windll.user32.ShowWindow(h, 9)

    def rec(): 
        while True:
            try:
                get = s.recv(1024).decode()
            except:
                print("Connecton Failed")
                Label(frame_admin,text=f'Connecton Failed.\n........').pack(pady=20)
                break
            if get == 'quit':
                s.close()
            if get.startswith('app'):
                # global app_list
                app_list.append(get[3::])
                sc2.update()
                c = len(app_list)-1
                print(c)
                for i in app_list[c::]:
                    def func(x=i):
                        return os.startfile(x)

                    button[i]=Button(fra, text= i,relief='solid',overrelief='solid',border=1,borderwidth=1,bg='#4A7A8C',foreground='#fff', command= func)
                    button[i].pack(side='left',padx=3)
                print(app_list[13::])
            if get.startswith('removeapp'):
                if get[9::] in app_list:
                    for i in app_list:
                        button[i].destroy()
                    
                    app_list.remove(get[9::])

                    for i in app_list:
                        def func(x=i):
                            return os.startfile(x)

                        button[i]=Button(fra, text= i,relief='solid',overrelief='solid',border=1,borderwidth=1,bg='#4A7A8C',foreground='#fff', command= func)
                        button[i].pack(side='left',padx=3)
                else:
                    messagebox.showwarning('Unable to remove',f'No Application Like this {get[9::]}')
                print(get[9::])
            if get == 'lock':
                print('True')
                Label(frame_admin,text=f'Locked.\n........').pack(pady=20)
                blockKey()
            if get == 'unlock':
                print('Unlock -- True')
                Label(frame_admin,text=f'UnLocked.\n........').pack(pady=20)
                disblockKey()
            if get.startswith('t'):
                print('Timer',get[1::])
                print('hr:',get[1:3],'Min:',get[3:5],'Sec:',get[5::])
                hrs.set(get[1:3])
                mins.set(get[3:5])
                sec.set(get[5::])
                Thread(target=timer, daemon=True).start()
            if get == 'img':
                while True:
                    img = ImageGrab.grab()
                    img_bytes = io.BytesIO()
                    img.save(img_bytes, format='PNG')
                    try:
                        s.send(img_bytes.getvalue())
                    except:
                        pass
    rec()

fra = Frame(sc2,highlightbackground='yellow',highlightcolor='#000',highlightthickness=3,background='skyblue')
app_list=['Chrome','Python','Xamp','Notepad','VsCode','Terminal','Android Studio','Word','Excel','Powerpoint','Powershell','Vs-Code','cmd']    

button={}
for i in app_list:
   def func(x=i):
      if x=='Xamp':
        return os.startfile("C:/xampp/xampp-control.exe")
      elif x=='VsCode':
        return os.startfile("code")
      elif x=='Word':
        return os.startfile("C:/Program Files/Microsoft Office/root/Office16/winword.exe")
      elif x=='Excel':
        return os.startfile("C:/Program Files/Microsoft Office/root/Office16/excel.exe")
      elif x=='Powerpoint':
        return os.startfile("C:/Program Files/Microsoft Office/root/Office16/powerpnt.exe")
      elif x=='Android Studio':
        return os.startfile('C:/Program Files/Android/Android Studio/bin/studio64.exe')  
      elif x=='Terminal':
        return os.startfile('cmd')
      elif x=='Command Prompt':
        return os.startfile('cmd')
      else:
        return os.startfile(x)

   button[i]=Button(fra, text= i,relief='solid',overrelief='solid',border=1,borderwidth=1,bg='#4A7A8C',foreground='#fff', command= func)
   button[i].pack(side='left',padx=3)
fra.pack(pady=50)

def timer():
   times = int(hrs.get())*3600+ int(mins.get())*60 + int(sec.get())
   while times > -1:
      minute,second = (times // 60 , times % 60)
      hour =0
      if minute > 60:
         hour , minute = (minute // 60 , minute % 60)
      sec.set(second)
      mins.set(minute)
      hrs.set(hour)
      try:
         sc2.update()
      except:
         print('Force shutdown')
      time.sleep(1)
      if(times == 0):
         sc2.destroy()
      times -= 1

frame_admin = Frame(sc2,highlightbackground='#000',highlightthickness=3)
Label(frame_admin,text='Enter Host(Server) Name').pack()
getHost = Entry(frame_admin,justify='center', width = 38, font = 'Jost 14', relief='flat', background='#444', foreground='#fff', highlightbackground='#fff', highlightthickness=3, highlightcolor='green')
getHost.pack()
def fra_admin():
   print(getHost.get())
   hostName.set(getHost.get())
   Thread(target=client, daemon=True).start()
   Label(frame_admin,text=f'Connecting To SerVer.........').pack(pady=6)
#    frame_admin.pack(pady=80)
   # Thread(target=timer, daemon=True).start()

Button(frame_admin, text= 'Submit',relief='solid',overrelief='solid',border=1,borderwidth=1,bg='#4A7A8C',foreground='#fff', command= fra_admin).pack()
img_app = PhotoImage(file="D:\Python\Py Projects\Assets\Admin.png").subsample(10,10)
# img_app = PhotoImage(file="./Admin.png").subsample(10,10)
btn_fraOpen=Button(text='Admin',image=img_app,border=1,borderwidth=0,activebackground='#4A7A8C',background='#4A7A8C',command=lambda:frame_admin.pack(pady=80))
btn_fraOpen.pack()
btn_fraOpen.place(x=10,y=120)

sc2.mainloop()