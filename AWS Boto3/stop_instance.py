import boto3
import pprint
import yaml


ec2client = boto3.client('ec2')

response = ec2client.stop_instances(
    InstanceIds=[
        'i-0b2b7ca94e00cfb8c','i-011a3cae618296a8a'
    ],
    Hibernate=False,
    DryRun=False, # If true then it will test to see if you have permissions, without running the actual code
    Force=False
)

#pprint.pprint(response)
print(yaml.dump(response, default_flow_style=False))   # printing it this way so that the dictionary response is easier to see and understand

# sample code:-
# response = client.stop_instances(
#     InstanceIds=[
#         'string',
#     ],
#     Hibernate=True|False,
#     DryRun=True|False,
#     Force=True|False
# )