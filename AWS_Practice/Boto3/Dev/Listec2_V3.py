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
    print('Instance No.# ',instanceCount)
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
#    

def main():
    '''Main function'''
  
    # call function1
     

if __name__ == "__main__":
    main()
