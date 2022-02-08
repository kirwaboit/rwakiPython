import boto3
import argparse

'''BRING IN ARGPARSE CODE TO GET USER INPUT'''

parser = argparse.ArgumentParser()
parser.add_argument('--serverNumber', type=int, required=True)
args = parser.parse_args()

#Argument brought in has now been stored under variable  'args.serverNumber'

'''REFRESH SERVER STATUS AND ASSOCIATE NUMBER INPUT AND INTACE_ID TO DICTIONARY'''

# dictionary to house instance number and instance ID
serverDict = {}

'''Create Client to access instance details'''
ec2 = boto3.client('ec2')
response = ec2.describe_instances()


'''Create Resource to access instance state'''
ec2_resource = boto3.resource('ec2')


'''Iterate through the resources'''
instanceCount = 0
instanceStateColor = ''



for item in response['Reservations']:
    instanceState = ec2_resource.Instance(item['Instances'][0]['InstanceId'])
    if instanceState.state['Name'] == "running":
        instanceStateColor = '32m'
    elif instanceState.state['Name'] == "stopped":
        instanceStateColor = '31m'
    elif ((instanceState.state['Name'] == "pending") or (instanceState.state['Name'] == "stopping")) :
        instanceStateColor = '33m'
    
    serverDict[instanceCount] = response['Reservations'][instanceCount ]['Instances'][0]['InstanceId']
    
    
    
    # print('Instance No.# \033[165m {} \033[0m'.format(instanceCount))
    # print('Name of Server : \033[35m {} \033[0m'.format(response['Reservations'][instanceCount ]['Instances'][0]['Tags'][0]['Value']))
    # print('ImageId : \033[36m {} \033[0m'.format(response['Reservations'][instanceCount ]['Instances'][0]['ImageId']))
    # print('InstanceId : \033[36m {} \033[0m'.format(response['Reservations'][instanceCount ]['Instances'][0]['InstanceId']))
  
    # print('InstanceType : \033[36m {} \033[0m'.format(response['Reservations'][instanceCount ]['Instances'][0]['InstanceType']))
    # if response['Reservations'][instanceCount ]['Instances'][0]['PublicDnsName']:
    #     print('Public DNS :\033[36m {} \033[0m'.format(response['Reservations'][instanceCount ]['Instances'][0]['PublicDnsName']))
    # else:
    #     print('Public DNS : \033[36m Instance is not online \033[0m')
       

    # print('Instance State : \033[{} {} \033[0m'.format(instanceStateColor,instanceState.state['Name'])) #Tag [0] refers to  the 'Name' value
   
    # print('\n')
    
    instanceCount = instanceCount + 1



ec2client = boto3.client('ec2')
#client = boto3.client('ec2',region_name='us-east-1') #Add your region

response = ec2client.start_instances(
    InstanceIds=[  # don't forget the comma in the list if starting two or more instances at the same time
        #'i-0808ef104dc98bf71'   #  RHEL8_v1 
        #'i-01317b948441c0e7e'  #  RHEL8_v0007
        #'i-021d0bed25732d9c7'  # uBUNTU
        serverDict[args.serverNumber]
    ],
    AdditionalInfo='string',
    DryRun=False
)

print('Starting server No :\033[36m {} \033[0m Refresh server stats to see status'.format(args.serverNumber) )
print('Starting server ID No :\033[36m {} \033[0m Refresh server stats to see status'.format(serverDict[args.serverNumber]) )
#print(response)


