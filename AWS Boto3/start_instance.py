
'''Use info from here :- 
https://stackoverflow.com/questions/66364247/how-to-stop-and-start-ec2-instance-using-boto3-and-lambda-function '''

import boto3

client = boto3.client('ec2',region_name='us-east-1') #Add your region

print('Loading function')

def lambda_handler(event, context):
    responses = client.start_instances(
    InstanceIds=[
        'i-0b2b7ca94e00cfb8c'
    ],

    DryRun=True # Make it False to test
)