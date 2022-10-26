import socket
from threading import Thread
from tkinter import*

nickname=input("Choose Your Name")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

client.connect((ip_address, port))
print("Connected to the Server!!")

class GUI:
    def __init__(self):
        self.Window=Tk()
        self.Window.withdraw()
        self.login=Toplevel()
        self.login.title("Login")

        self.login.resizable(width=False,height=False)
        self.login.configure(width=400,height=300)
        self.pls=Label(self.login,text="Please login to continue", justify=CENTER, font="Hlvetica 14 bold")
        self.pls.place(relheight=0.15, relx=0.2, rely=0.7)
        self.labelName=Label(self.login, text="Name:", font="helvetica 12")
        self.labelName.place(relheight=0.2, relx=0.)
        self.entryNme=Entry(self.login, font="Helvetica 14 bold")
        self.entryNme.place(relwidth=0.4, relheight=0.12, relx=0.35, rely=0.2)
        self.entryName.focus()

        self.go=Button(self.login, text="CONTINUE", font="Helvetica 14 bold")
        self.go.place(relx=0.4, rely=0.55)
        self.Window.meinloop()
        
def goAhead(self, name):
    self.login.destroy()
    self.name=name
    rcv=Thread(target=self.receive)
    rcv.start()

def receive(self):
    while True:
        try:
            message=client.recv(2048).decode('utf-8')
            if message=='NICKNAME':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("An error occured")
            client.close()
            break

g=GUI()