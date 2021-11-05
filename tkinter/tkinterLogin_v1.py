from tkinter import *


class login(Tk):
    def __init__(self):
        super(). __init__()
        self.title('Login Window')
        self.geometry("700x500")
        self.resizable(False,False)
        
    def Label(self):
        self.backGroundImage = PhotoImage(file = r"tkinter/bluebackground_v2.png")
        self.backGroundImageLabel = Label(self,image = self.backGroundImage)
        self.backGroundImageLabel.place(x = 0,y = 0)

        self.canvas = Canvas(self,width = 400, height = 330)
        self.canvas.place(x = 150,y=60)

        self.title = Label(self,text = 'Login', font = 'Bold 30')
        self.title.place(x = 300,y=80)

        self.userName = Label(self,text = 'User Name', font = '8')
        self.userName.place(x = 200,y=150)

        self.password = Label(self,text = 'Password', font = '8')
        self.password.place(x = 200,y=200)

    def Entry(self):
        self.userName = Text(
            self,borderwidth = 0, 
            highlightthickness = 0,
            width = 22,
            height = 1,
            bg = "black",
            fg="white",
            font=("Consolas", 12)
            )
        self.userName.place(x = 320, y = 155)

        self.Password = Entry(self,borderwidth = 0,show = "+", highlightthickness = 0)
        self.Password.place(x = 320, y = 205, width = 175, height = 20)

    def Button(self):
        self.loginButtonImage = PhotoImage(file = r"tkinter/button_resized_v2.png")
        self.loginButton = Button(self,image = self.loginButtonImage,height = 40,width = 100, command = self.Login,border = 0)
        self.loginButton.place(x = 290,y = 250)
         
   
    
    def Login(self):
        print('gf')



if __name__ =="__main__":
    Login = login()  # create new login object
    Login.Label()
    Login.Entry()
    Login.Button()
    Login.mainloop()


        


