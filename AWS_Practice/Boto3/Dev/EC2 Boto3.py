import boto3
ec2 = boto3.resource('ec2')   # both ec2 client and resource have different code for accessing aws, resource is less verbose
#ec2 = boto3.client('ec2')  

#ImageId='ami-04d29b6f966df1537',    the old image

instances = ec2.create_instances(
     ImageId='ami-0ab4d1e9cf9a1215a',   # Current new Free Tier
     MinCount=1,
     MaxCount=1,
     InstanceType='t2.micro',
     KeyName='rwakiPython_v2',
     TagSpecifications=[
        {
          'ResourceType': 'instance',
          'Tags': [
            {
              'Key': 'Name',
              'Value': 'Linux 2 AMI (HVM) v3'
            },
            {
              'Key': 'owner',
              'Value': 'me'
            },
          ]
        },
      ],
 )

