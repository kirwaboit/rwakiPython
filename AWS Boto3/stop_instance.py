import boto3
import pprint
import yaml


ec2client = boto3.client('ec2')

response = ec2client.stop_instances(
    InstanceIds=[      # don't forget comma if adding multiple values
        #'i-0808ef104dc98bf71'   #  RHEL8_v5 
        'i-04e52c00bb4934304'  #  SUSE Linux
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