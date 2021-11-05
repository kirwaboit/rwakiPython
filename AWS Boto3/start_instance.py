
'''Use info from here :- 
https://stackoverflow.com/questions/66364247/how-to-stop-and-start-ec2-instance-using-boto3-and-lambda-function '''

# latest instance I am working on : ami-0b0af3577fe5e3532
import boto3

ec2client = boto3.client('ec2')
#client = boto3.client('ec2',region_name='us-east-1') #Add your region

response = ec2client.start_instances(
    InstanceIds=[  # don't forget the comma in the list if starting two or more instances at the same time
        'i-0808ef104dc98bf71'   #  RHEL8_v1 
        #'i-04e52c00bb4934304'  #  SUSE Linux
    ],
    AdditionalInfo='string',
    DryRun=False
)

print(response)


