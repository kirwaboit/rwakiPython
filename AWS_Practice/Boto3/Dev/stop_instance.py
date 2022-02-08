import boto3
import pprint
import yaml


ec2client = boto3.client('ec2')

response = ec2client.stop_instances(
    InstanceIds=[      # don't forget comma if adding multiple values
        #'i-0808ef104dc98bf71'   #  RHEL8_v5 
        #'i-01317b948441c0e7e'  #  RHEL8_v0007
        'i-021d0bed25732d9c7'  # UBUNTU
    ],
    Hibernate=False,
    DryRun=False, # If true then it will test to see if you have permissions, without running the actual code
    Force=False
)


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