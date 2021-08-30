import boto3
import yaml

'''The attempt below unfortunately prints everything about the ec2, only need certain resources about it'''

# ec2 = boto3.client('ec2')
# response = ec2.describe_instances()
# print(response)

ec2 = boto3.client('ec2')
response = ec2.describe_instances()
#print(response)

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



print(
    response['Reservations'] # check Reservations
    [0] # Chose the first reservation group
    ['Instances'] # select instances in this first group
    [0]# Only one group in this category so 0 is the only option
    ['ImageId'] # print out for me this instances ID
    )

    #TODO: need to print out the number of reservation groups programattically, so that I can print out ALL the instances at once