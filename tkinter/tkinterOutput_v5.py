from tkinter import *
import boto3
import yaml
import json

'''@@@ EXTRACTING SERVER DATA TO PRESENT @@@''' 


'''Create Client to access instance details'''
ec2 = boto3.client('ec2')
response = ec2.describe_instances() 

'''Create Resource to access instance state'''
ec2_resource = boto3.resource('ec2')


'''Iterate through the resources'''
instanceCount = 0
instanceStateColor = ''
dataList = []
#message = ''
for item in response['Reservations']:
    instanceState = ec2_resource.Instance(item['Instances'][0]['InstanceId'])
    if instanceState.state['Name'] == "running":
        instanceStateColor = '32m'
    elif instanceState.state['Name'] == "stopped":
        instanceStateColor = '31m'
    elif ((instanceState.state['Name'] == "pending") or (instanceState.state['Name'] == "stopping")) :
        instanceStateColor = '33m'
    print('Instance No.# ',instanceCount)
    string1 = 'Instance No.# {} '.format(instanceCount)
    dataList.append('Instance No.# {} '.format(instanceCount)+'\n')
    print('Name of Server : \033[35m {} \033[0m'.format(response['Reservations'][instanceCount ]['Instances'][0]['Tags'][0]['Value']))
    dataList.append('Name of Server : {} '.format(response['Reservations'][instanceCount ]['Instances'][0]['Tags'][0]['Value'])+'\n')
    print('ImageId : \033[34m {} \033[0m'.format(response['Reservations'][instanceCount ]['Instances'][0]['ImageId']))
    dataList.append('ImageId : {} '.format(response['Reservations'][instanceCount ]['Instances'][0]['ImageId'])+'\n')
    print('InstanceId : \033[34m {} \033[0m'.format(response['Reservations'][instanceCount ]['Instances'][0]['InstanceId']))
    dataList.append('InstanceId : {} '.format(response['Reservations'][instanceCount ]['Instances'][0]['InstanceId'])+'\n')
    print('InstanceType :'.format(response['Reservations'][instanceCount ]['Instances'][0]['InstanceType']))
    dataList.append('InstanceType : {}'.format(response['Reservations'][instanceCount ]['Instances'][0]['InstanceType'])+'\n')
    if response['Reservations'][instanceCount ]['Instances'][0]['PublicDnsName']:
        print('Public DNS :',response['Reservations'][instanceCount ]['Instances'][0]['PublicDnsName'])
        dataList.append('Public DNS :{}'.format(response['Reservations'][instanceCount ]['Instances'][0]['PublicDnsName']+'\n'))
    else:
        print('Public DNS : Instance is not online')
        dataList.append('Public DNS : Instance is not online'+'\n')
    print('Instance State :', instanceState.state['Name']) #Tag [0] refers to  the 'Name' value
    dataList.append('InstanceType : {}'.format(response['Reservations'][instanceCount ]['Instances'][0]['InstanceType']+'\n'))
    dataList.append('\n')
   
    print('\n')
    
    instanceCount = instanceCount + 1



'''@@@ PREPARING TKINTER GUI @@@'''


def clear_textbox():
    text_box.delete(1.0, 'end')


ws = Tk()
ws.title('PythonGuides')
ws.geometry('600x700')   #X by Y
ws.config(bg='#84BF04')

# need 7 strings
message = ''
string1 ="hello world of mine"
string2 = "glad to be here!!"

text1 = ['Instance No.#  2',"\n",'Name of Server :  RHEL8_v5 ', "\n",'ImageId :  ami-0b0af3577fe5e3532 ',"\n", '4', '5']
singleString = ''.join(dataList)

message = singleString

# message = string1 +"\n"+string2
# message =\
# '''Instance No.#  3
# Name of Server :  SUSE Linux 
# ImageId :  ami-0a16c2295ef80ff63 
# InstanceId :  i-04e52c00bb4934304 
# InstanceType : t2.micro
# Public DNS : ec2-54-164-107-204.compute-1.amazonaws.com
# Instance State : running'''

text_box = Text(
    ws,
    height=90,
    width=60,
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