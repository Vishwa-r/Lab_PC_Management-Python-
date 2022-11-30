import socket
from tkinter import *
from PIL import ImageGrab
import io,keyboard
from ctypes import windll

h = windll.user32.FindWindowA(b'Shell_TrayWnd', None)

time = '000000000'
def timer(get):
    global time
    time = get
    print(time)

def client():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host = 'vishwa' #input('Enter Server Name : ')
    try:
        s.connect((host,4000))
    except:
        print(host,'is Disconnected')

    def blockKey():
        keyboard.block_key('alt')
        keyboard.block_key('esc')
        keyboard.block_key('win')
        windll.user32.ShowWindow(h, 0)
        # messagebox.showinfo('Block Keys Enabled','ALT & ESCAPE & WIN KEYS are Blocked')

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
                break
            if get == 'quit':
                s.close()
            if get == 'lock':
                print('True')
                blockKey()
            if get == 'unlock':
                print('Unlock -- True')
                disblockKey()
            if get.startswith('t'):
                print('Timer',get[1::])
                timer(get)
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
client()