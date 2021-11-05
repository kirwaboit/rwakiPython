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
print(response['Reservations'][5]['Instances'][0]['InstanceId'])

'''Create Resource to access instance state'''
ec2_resource = boto3.resource('ec2')


'''Iterate through the resources'''
instanceCount = 0
instanceStateColor = ''

#print(json.dumps(response['Reservations'], indent=1))
# for item in response['Reservations']:
#     print(item)
#     instanceState = ec2_resource.Instance(item['Instances'][0]['InstanceId'])
#     if instanceState.state['Name'] == "running":
#         instanceStateColor = '32m'
#     elif instanceState.state['Name'] == "stopped":
#         instanceStateColor = '31m'
#     elif ((instanceState.state['Name'] == "pending") or (instanceState.state['Name'] == "stopping")) :
#         instanceStateColor = '33m'

 
#     print("For instance number: " ,instanceCount,"\n") 
#     print(
#         "Image Id is: \033[35m {ImageId}\033[0m\n\
# Server Name is: \033[34m {Tags[1][Value]}\033[0m\n\
# Instance Id is: \033[34m {InstanceId}\033[0m\n\
# The type of instance is: \033[34m {InstanceType}\033[0m"
#         .format(**item['Instances'][0]))
#     print("Instance is : \033[{} {} \033[0m ".format(instanceStateColor,instanceState.state['Name']))
#     instanceCount = instanceCount + 1
#     print("\n")

        