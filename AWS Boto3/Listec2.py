import boto3
import yaml
import json

'''The attempt below unfortunately prints everything about the ec2, only need certain resources about it'''

# ec2 = boto3.client('ec2')
# response = ec2.describe_instances()
# print(response)


'''Create Client to access instance details'''
ec2 = boto3.client('ec2')
response = ec2.describe_instances()
#print(response)
#print(json.dumps(response, indent=4, sort_keys=True, default=str))
#print(response['Reservations'][2]['Instances'][0]['InstanceId'])
#print(response['Reservations'][2]['Instances'][0]['PublicDnsName'])
print
print(response['Reservations'][2]['Instances'][0]['InstanceId'])

'''Create Resource to access instance state'''
ec2_resource = boto3.resource('ec2')


'''Iterate through the resources'''
instanceCount = 0
instanceStateColor = ''

#print(json.dumps(response['Reservations'], indent=1))

for item in response['Reservations']:
    instanceState = ec2_resource.Instance(item['Instances'][0]['InstanceId'])
    if instanceState.state['Name'] == "running":
        instanceStateColor = '32m'
    elif instanceState.state['Name'] == "stopped":
        instanceStateColor = '31m'
    elif ((instanceState.state['Name'] == "pending") or (instanceState.state['Name'] == "stopping")) :
        instanceStateColor = '33m'
    print('Instance No.# ',instanceCount)
    #print("\033[31mThis is red font. {} \033[0m".format(instanceCount))
    #print('Name of Server :',response['Reservations'][instanceCount ]['Instances'][0]['Tags'][0]['Value'])
    print('Name of Server : \033[35m {} \033[0m'.format(response['Reservations'][instanceCount ]['Instances'][0]['Tags'][0]['Value']))
    print('ImageId : \033[34m {} \033[0m'.format(response['Reservations'][instanceCount ]['Instances'][0]['ImageId']))
    print('InstanceId : \033[34m {} \033[0m'.format(response['Reservations'][instanceCount ]['Instances'][0]['InstanceId']))
   # print('InstanceId :',response['Reservations'][instanceCount ]['Instances'][0]['InstanceId'])
    print('InstanceType :',response['Reservations'][instanceCount ]['Instances'][0]['InstanceType'])
    if response['Reservations'][instanceCount ]['Instances'][0]['PublicDnsName']:
        print('Public DNS :',response['Reservations'][instanceCount ]['Instances'][0]['PublicDnsName'])
    else:
        print('Public DNS : Instance is not online')
    print('Instance State :', instanceState.state['Name']) #Tag [0] refers to  the 'Name' value
   
    print('\n')
    
    instanceCount = instanceCount + 1
#     print(len(response['Reservations']))
#     print('current value of instance count',instanceCount)
#     #print(item)
#     #instanceState = ec2_resource.Instance(item['Instances'][0]['InstanceId'])
#     instanceState = ec2_resource.Instance(item[1][0][0])
#     if instanceState.state['Name'] == "running":
#         instanceStateColor = '32m'
#     elif instanceState.state['Name'] == "stopped":
#         instanceStateColor = '31m'
#     elif ((instanceState.state['Name'] == "pending") or (in 
# The type of instance is: \033[34m {InstanceType}\033[0m"
#         .format(**item[instanceCount]['Instances'][0]))
#     print("Instance is : \033[{} {} \033[0m ".format(instanceStateColor,instanceState.state['Name']))
#     instanceCount = instanceCount + 1
#     print("\n")


        