from tkinter import *
  
''' THIS TKINTER GUI  STARTS OUT WITH SERVER INFO , THEN ALLOWS ONE TO PRESS A REFRESH BUTTON AND IT WILL SHOW THE CURRENT STATUS OF MY EC2 INSTANCES'''


def clear_textbox():
    text_box.delete(1.0, 'end')


ws = Tk()
ws.title('PythonGuides')
ws.geometry('600x700')   #X by Y
ws.config(bg='#84BF04')

message =\
'''Instance No.#  3
Name of Server :  SUSE Linux 
ImageId :  ami-0a16c2295ef80ff63 
InstanceId :  i-04e52c00bb4934304 
InstanceType : t2.micro
Public DNS : ec2-54-164-107-204.compute-1.amazonaws.com
Instance State : running'''

text_box = Text(
    ws,
    height=13,
    width=55,
    bg = "black", #background color
    fg="white"
)
text_box.pack(expand=True)
text_box.insert('end', message)

# Add Colour change for the text
text_box.tag_add("start", "1.0", "1.13")
#text_box.tag_config("start", background="black",foreground="red")
text_box.tag_config("start", background="black",foreground="red")

Button(
    ws,
    text='Clear',
    width=15,
    height=2,
    command=clear_textbox
).pack(expand=True)

ws.mainloop()