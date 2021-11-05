from tkinter import *
import boto3
import yaml
import json

'''PREPARE THE FRAME'''
ws = Tk()
ws.title('EC2 Server Status')
ws.geometry('600x700')   #X by Y
ws.config(bg='grey67')


'''@@@ EXTRACTING SERVER DATA TO PRESENT @@@''' 

def refreshInstance():
    '''Create Client to access instance details'''
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances() 

    '''Create Resource to access instance state'''
    ec2_resource = boto3.resource('ec2')


    '''Iterate through the resources'''
    instanceCount = 0
    instanceStateColor = ''
    dataList = []
    runColorList = []
    #message = ''
    for item in response['Reservations']:
        instanceState = ec2_resource.Instance(item['Instances'][0]['InstanceId'])
        if instanceState.state['Name'] == "running":
            runColorList.append("spring green")
            instanceStateColor = '32m'
        elif instanceState.state['Name'] == "stopped":
            instanceStateColor = '31m'
            runColorList.append("red")
        elif ((instanceState.state['Name'] == "pending") or (instanceState.state['Name'] == "stopping")) :
            instanceStateColor = '33m'
            runColorList.append("orange")
        
        string1 = 'Instance No.# {} '.format(instanceCount)
        dataList.append('Instance No.# {} '.format(instanceCount)+'\n')
        
        dataList.append('Name of Server : {} '.format(response['Reservations'][instanceCount ]['Instances'][0]['Tags'][0]['Value'])+'\n')
        
        dataList.append('ImageId : {} '.format(response['Reservations'][instanceCount ]['Instances'][0]['ImageId'])+'\n')
        
        dataList.append('InstanceId : {} '.format(response['Reservations'][instanceCount ]['Instances'][0]['InstanceId'])+'\n')
        
        dataList.append('InstanceType : {}'.format(response['Reservations'][instanceCount ]['Instances'][0]['InstanceType'])+'\n')
        
        if response['Reservations'][instanceCount ]['Instances'][0]['PublicDnsName']:
            dataList.append('Public DNS :{}'.format(response['Reservations'][instanceCount ]['Instances'][0]['PublicDnsName']+'\n'))
        else:
            dataList.append('Public DNS : Instance is not online'+'\n')
    
        dataList.append('Instance State :{}'.format(instanceState.state['Name'])+'\n')
        dataList.append('\n')
    
        
        
        instanceCount = instanceCount + 1



    '''@@@ PREPARING TKINTER GUI @@@'''


    

    

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
        fg="white",
        font=("Consolas", 12)
    )
    text_box.delete(1.0, 'end')
    text_box.pack(expand=True)
    text_box.insert('end', message)

    lineCount = 1
    for x in range(0, instanceCount):
        text_box.tag_add("firstLine", "{}.13".format(lineCount), "{}.16".format(lineCount))
        lineCount = lineCount + 1
        text_box.tag_add("secondLine", "{}.16".format(lineCount), "{}.70".format(lineCount))
        lineCount = lineCount + 1
        text_box.tag_add("thirdLine", "{}.10".format(lineCount), "{}.70".format(lineCount))
        lineCount = lineCount + 1
        text_box.tag_add("fourthLine", "{}.13".format(lineCount), "{}.70".format(lineCount))
        lineCount = lineCount + 1
        text_box.tag_add("fifthLine", "{}.14".format(lineCount), "{}.70".format(lineCount))
        lineCount = lineCount + 1
        text_box.tag_add("sixthLine", "{}.13".format(lineCount), "{}.70".format(lineCount))
        lineCount = lineCount + 1
    # text_box.tag_add("lastLine{} "+"{}.16".format(lineCount) "{}.70".format(instanceCount,lineCount,lineCount))
        text_box.tag_add("lastLine{}".format(instanceCount), "{}.16".format(lineCount), "{}.70".format(lineCount))
        print(runColorList[x])

        text_box.tag_config("lastLine{}".format(instanceCount),foreground=runColorList[x])
        lineCount = lineCount + 2
        instanceCount = instanceCount + 1


    # Add Colour change for the text
    # lineCount = 1
    # text_box.tag_add("firstLine", "{}.13".format(lineCount), "{}.16".format(lineCount))
    # text_box.tag_add("secondLine", "2.16", "2.70")
    # text_box.tag_add("thirdLine", "3.10", "3.70")
    # text_box.tag_add("fourthLine", "4.13", "4.70")
    # text_box.tag_add("fifthLine", "5.14", "5.70")
    # text_box.tag_add("sixthLine", "6.13", "6.70")
    # text_box.tag_add("seventhLine", "7.16", "7.70")
    #text_box.tag_config("start", background="black",foreground="red")

    serverNumberFontColor = 'magenta'
    regularFontColor = 'light sky blue'

    text_box.tag_config("firstLine",foreground=serverNumberFontColor)
    text_box.tag_config("secondLine", foreground=regularFontColor)
    text_box.tag_config("thirdLine", foreground=regularFontColor)
    text_box.tag_config("fourthLine", foreground=regularFontColor)
    text_box.tag_config("fifthLine",foreground=regularFontColor)
    text_box.tag_config("sixthLine",foreground=regularFontColor)

def clear_textbox():
    #text_box.delete(1.0, 'end')
    refreshInstance()


def main():
    Button(
        ws,
        text='Refresh',
        width=15,
        height=2,
        command=clear_textbox
    ).pack(expand=True)
    refreshInstance()
    


    ws.mainloop()



    # call function1
    

if __name__ == "__main__":
    main()
