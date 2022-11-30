# from tkinter import *

# a = Tk()
# a.state('zoomed')
# can = Canvas(a,background='pink')
# can.pack(fill= BOTH, expand= 0,pady=20)

# button = []
# for i in range(62):
#    button.append(Button(can, text='App '+str(i+1), command=lambda: None ))
#    button[i].pack(side='left',pady=2)

# btn = Button( text='New')
# btn.pack()

# a.mainloop()

# from tkinter import *


# root = Tk()
# root.geometry('400x400')

# auxframe=Frame(root)
# auxframe.pack(fill=BOTH, expand=YES)

# i = 0.01
# def move_Next():
#    global i
#    print(i)
#    i+=0.01
#    cv.xview_moveto(i)
#    if i > 0.80:
#       i = 0.01

# cv = Canvas(auxframe, scrollregion=(0,0,8000,8000))
# vscrollbar = Scrollbar(auxframe, orient=VERTICAL)
# vscrollbar.pack(fill=Y, side=RIGHT)
# vscrollbar.config(command=cv.yview)
# cv.configure(scrollregion=cv.bbox('all'))
# cv.pack(side=LEFT, fill=BOTH, expand=TRUE)

# btn_Next = Button(root,text='>>', relief='flat', overrelief='solid', background='#444', activebackground='#111', foreground='#fff', activeforeground='#fff', command=move_Next)
# # btn_Next.pack()

# # def bind_Next(e):
# #    global i
# #    print(i)
# #    i+=0.01
# #    cv.xview_moveto(i)
# #    if i > 0.99:
# #       i = 0.01
# # root.bind('<Right>', bind_Next)

# app_list=[]    
# for row_index in range(8):
#    for col_index in range(8):
#       iconimage = PhotoImage(file="D:\Python\Py Projects\Assets\ConvertedIMAGe.png")
#       b=Button(cv,image=iconimage)
#       app_list.append(iconimage)             
#       b.grid(row=row_index, column=col_index, sticky=N+S+E+W)  


# mainloop()

# from tkinter import *

# a = Tk()
# a.geometry('300x300')
# a.state('zoomed')
# Label(a,text='Welcome !!!').pack()

# f = Frame(a,background="#333",highlightbackground='pink',highlightcolor='pink',highlightthickness=8,relief='raised')
# f.pack(before=None,fill='both',ipady=100,pady=50)

# i = 0.01
# def move_Next():
#    global i
#    print(i)
#    i+=0.01
#    c.xview_moveto(i)
#    if i > 0.80:
#       i = 0.01

# c = Canvas(f,background='#4A7A8C')

# for i in range(30):
#    Button(c,text=f'HI {i}',bg='#fff788').pack(side='left')

# s = Scrollbar(f,orient='horizontal')
# s.pack(fill='x')

# c.configure(scrollregion=c.bbox('all'),xscrollcommand=s.set)

# c.pack(before=None,fill='both',ipady=100,pady=50)

# Button(a,text='Next',command=move_Next).pack()

# mainloop()

# from tkinter import *

# a = Tk()
# a.geometry('350x200')
# f = Frame(a)
# s = Scrollbar(f,orient='vertical')
# s.pack(fill='y',side='right')
# Label(f,text='Hello').pack(pady=10)
# Button(f,text='Button').pack(pady=10)
# Entry(f).pack(pady=100)
# f.pack()
# mainloop()

# import Client
# Client.client()                 

# from tkinter import *
# import os

# a = Tk()
# a.state('zoomed')
# Label(text='Label').pack()


# fra = Frame(a,highlightbackground='skyblue',highlightcolor='#000',highlightthickness=3)
# app_list=['Chrome','Python','Xamp','Notepad','VsCode','Terminal','Android Studio','Chrome','Python','Xamp','Text-Editor','Vs-Code','Terminal']    

# button={}
# for i in app_list:
#    def func(x=i):
#       return os.startfile(x)

#    button[i]=Button(fra, text= i,relief='solid',overrelief='solid',border=1,borderwidth=1,bg='#4A7A8C',foreground='#fff', command= func)
#    button[i].pack(side='left',padx=3)

# fra.pack(pady=50)
# mainloop()

# from ctypes import windll
# h = windll.user32.FindWindowA(b'Shell_TrayWnd', None)
# # get the handle to the taskbar

# # hide the taskbar
# windll.user32.ShowWindow(h, 0)

# # show the taskbar again
# windll.user32.ShowWindow(h, 9)

# import socket as s
# print(s.gethostbyname())

# s = 'appchrome'
# if s.startswith('apps'):
#     print('True')

# from tkinter import *

# t = Tk()
# t.geometry('400x400')
# def btn():
#     l1.config(text=s)
#     for i in applist:
#         btn[i].destroy()
#     t.update()
#     b1.destroy()

# s = 'Text1'
# l1 = Label(t,text=s)
# l1.pack()
# s = 'Vishwa'
# b1 = Button(t,text='update',command=btn)
# b1.pack()
# applist = ['chrome','cmd','Firefox']
# btn = {}
# for i in applist:
#     btn[i]=Button(t,text=i)
#     btn[i].pack(side='left')

# mainloop()

# l= [1,2,3,4,5,6,7,8,9]
# print(l)
# l.remove(1)
# print(l)
