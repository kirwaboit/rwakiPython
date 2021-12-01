from tkinter import *


class login(Tk):
    def __init__(self):
        super(). __init__()
        self.title('Ec2 Server Status')
        self.geometry("800x900")  # X by Y
        self.resizable(False,False)
        
    def Label(self):
        self.backGroundImage = PhotoImage(file = r"tkinter/bluebackground_v2.png")
        self.backGroundImageLabel = Label(self,image = self.backGroundImage)
        self.backGroundImageLabel.place(x = 0,y = 0)

        self.canvas = Canvas(self,width = 740, height = 760)  # Original Y is 300, increase grey space by 
        self.canvas.place(x = 30,y=60)

        self.title = Label(self,text = 'Ec2 Server Status', font = 'Bold 25')
        self.title.place(x = 240,y=80)

        self.userName = Label(self,text = 'User Name', font = '8')
        self.userName.place(x = 420,y=155)
        #self.userName.place(x = 320, y = 155)

        # self.password = Label(self,text = 'Password', font = '8')
        # self.password.place(x = 200,y=200)

    def Entry(self):
        message =\
    '''
    Instance No.#  3
    Name of Server : SUSE Linux 
    ImageId :  ami-0a16c2295ef80ff63 
    InstanceId :  i-04e52c00bb4934304 
    InstanceType : t2.micro
    Public DNS : ec2-54-164-107-204.compute-1.amazonaws.com
    Instance State : running'''
        self.server1Box = Text(
            self,borderwidth = 0, 
            highlightthickness = 0,
            width = 60,
            height = 10,
            bg = "black",
            fg="white",
            font=("Consolas", 12)
            )
        self.server1Box.place(x = 50, y = 150)
        self.server1Box.insert('end', message)

        self.server2Box = Text(
            self,borderwidth = 0, 
            highlightthickness = 0,
            width = 60,
            height = 10,
            bg = "black",
            fg="white",
            font=("Consolas", 12)
            )
        self.server2Box.place(x = 50, y = 380)   #380 Y new distance was 380-150 = 230, so add 230 for the new Y Place
        self.server2Box.insert('end', message)

        self.server3Box = Text(
            self,borderwidth = 0, 
            highlightthickness = 0,
            width = 60,
            height = 10,
            bg = "black",
            fg="white",
            font=("Consolas", 12)
            )
        self.server3Box.place(x = 50, y = 610)   #added  230, so add 230 for the new Y Place
        self.server3Box.insert('end', message)


       

        # self.Password = Entry(
        #     self,borderwidth = 0,
        #     show = "+", 
        #     highlightthickness = 0)
        # self.Password.place(x = 320, y = 205, width = 175, height = 20)

    def Button(self):
        self.loginButtonImage = PhotoImage(file = r"tkinter/button_resized_v2.png")
        self.loginButton = Button(self,image = self.loginButtonImage,height = 40,width = 100, command = self.Login,border = 0)
        self.loginButton.place(x = 650,y = 150)
         
   
    
    def Login(self):
        print('online')



if __name__ =="__main__":
    Login = login()  # create new login object
    Login.Label()
    Login.Entry()
    Login.Button()
    Login.mainloop()


        


