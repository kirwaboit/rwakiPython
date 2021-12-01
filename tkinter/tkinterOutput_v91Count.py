from tkinter import *

heightVariable = 230
instanceCount = 0 
instanceSize = 230
originalCanvas = 300
yhit = 150

class Ec2ServerWindow(Tk):
   
    print('value of global variable  is :',instanceCount)
    def __init__(self):
        super(). __init__()
        self.title('Ec2 Server Status')
        self.geometry("800x900")  # X by Y
        self.resizable(False,False)
        
    def Label(self):
        global originalCanvas 
        originalCanvas = 300 # original Y value of canvas
        self.backGroundImage = PhotoImage(file = r"tkinter/bluebackground_v2.png")
        self.backGroundImageLabel = Label(self,image = self.backGroundImage)
        self.backGroundImageLabel.place(x = 0,y = 0)
        originalCanvas = originalCanvas+instanceSize
        print("canvas size is now =" , originalCanvas)

        self.canvas = Canvas(self,width = 740, height = (originalCanvas))  # Original Y is 300, increase grey space by 
        self.canvas.place(x = 30,y=60)

        self.title = Label(self,text = 'Ec2 Server Status', font = 'Bold 25')
        self.title.place(x = 240,y=80)

        # self.userName = Label(self,text = 'User Name', font = '8')
        # self.userName.place(x = 420,y=155)
        #self.userName.place(x = 320, y = 155)

        # self.password = Label(self,text = 'Password', font = '8')
        # self.password.place(x = 200,y=200)

    def Entry(self,instanceCount):
        yhit = 150
    
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
        
        self.server1Box.place(x = 50, y = yhit)
        self.server1Box.insert('end', message)
        
        yhit = yhit+230

        # self.server2Box = Text(
        #     self,borderwidth = 0, 
        #     highlightthickness = 0,
        #     width = 60,
        #     height = 10,
        #     bg = "black",
        #     fg="white",
        #     font=("Consolas", 12)
        #     )
        # self.server2Box.place(x = 50, y = 380)   #380 Y new distance was 380-150 = 230, so add 230 for the new Y Place
        # self.server2Box.insert('end', message)

        # self.server3Box = Text(
        #     self,borderwidth = 0, 
        #     highlightthickness = 0,
        #     width = 60,
        #     height = 10,
        #     bg = "black",
        #     fg="white",
        #     font=("Consolas", 12)
        #     )
        # self.server3Box.place(x = 50, y = 610)   #added  230, so add 230 for the new Y Place
        # self.server3Box.insert('end', message)


       


    def Button(self):
        self.loginButtonImage = PhotoImage(file = r"tkinter/button_resized_v2.png")
        self.loginButton = Button(self,image = self.loginButtonImage,height = 40,width = 100, command = self.Login,border = 0)
        self.loginButton.place(x = 650,y = 150)
         
   
    
    def Login(self):
        print('online')



if __name__ =="__main__":
    instanceCount = 1
    
      # create new login object
    Ec2Status = Ec2ServerWindow()
    for x in range(0, instanceCount):
        print("now on server :", x )
        Ec2Status.Label()
        Ec2Status.Entry(x)
    #Ec2Status.Button(instanceCount)
    Ec2Status.mainloop()


        


