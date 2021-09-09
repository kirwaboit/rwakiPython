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

'''Create Resource to access instance state'''
ec2_resource = boto3.resource('ec2')
# for key, value in response.items():
#     print(key, ' : ', value, "\n")

#print(yaml.dump(response, default_flow_style=False))


# print(yaml.dump(response
# ['Reservations']
# [3]  # Select First instance, in this case there are 4 instances
# ['Instances']
# [0] 
# ['ImageId']
# , default_flow_style=False))


# print(yaml.dump(response['Reservations'][3]['Instances'][0]['ImageId']
# , default_flow_style=False))




# print(
#     response['Reservations'] # check Reservations
#     [0] # Chose the first reservation group
#     ['Instances'] # select instances in this first group
#     [0]# Only one group in this category so 0 is the only option
#     ['ImageId'] # print out for me this instances ID
#     )

# print(
#     response['Reservations'][0]['Instances'][0]['ImageId'] # print out for me this instances ID
#     )

    #TODO: need to print out the number of reservation groups programattically, so that I can print out ALL the instances at once

# print(
# "Image Id is:  {ImageId} \n\
# The type of instance is:  {InstanceType}"
# .format(**response['Reservations'][0]['Instances'][0]))


# for item in response['Reservations']:
#     print(
#     "Image Id is:  {ImageId} \n\
#     The type of instance is:  {InstanceType}"
#     .format(**item['Instances'][0]))
#     print("\n")
    
# print("\n")
# print("\n")

# for item in response['Reservations']:
#     print(
#     "Image Id is: \033[34m {ImageId}\033[0m" , "\n"
#     "Instance Id is: \033[34m {InstanceId}\033[0m" ,"\n"
#     "The type of instance is: \033[34m {InstanceType}\033[0m"
#     .format(**item['Instances'][0]))
#     print("\n")
#     print("\n")

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

    print("For instance number: " ,instanceCount,"\n") 
    print(
        "Image Id is: \033[35m {ImageId}\033[0m\n\
Server Name is: \033[34m {Tags[1][Value]}\033[0m\n\
Instance Id is: \033[34m {InstanceId}\033[0m\n\
The type of instance is: \033[34m {InstanceType}\033[0m"
        .format(**item['Instances'][0]))
    print("Instance is : \033[{} {} \033[0m ".format(instanceStateColor,instanceState.state['Name']))
    instanceCount = instanceCount + 1
    print("\n")

#TODO the different colours can be found here : https://stackoverflow.com/questions/5947742/how-to-change-the-output-color-of-echo-in-linux      
#TODO Add owner of instace
#TODO Tag Order matters when making queries in Boto3 because it selects from groups, either create a universal policy /standard or create 
# a way to tell the difference between the tag groups 

# for item in response['Reservations']:
#     print("Image Id is: \033[31m response['Reservations'][0]['Instances'][0]['ImageId']\033[0m" "\n")
#     print("Image Id is: \033[31m item['ImageId']\033[0m" "\n")
#     print("Image Id is: \033[31m item['ImageId']\033[0m" "\n")
#     print("\n")


#print(json.dumps(response,sort_keys=True,default=str,indent=4))
#print(json.dumps(response,sort_keys=True,default=str,indent=4))

print("\033[31m Hi this si suppose to be red .\033[0m")