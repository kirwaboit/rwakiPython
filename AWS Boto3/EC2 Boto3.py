import boto3
ec2 = boto3.resource('ec2')


instances = ec2.create_instances(
     ImageId='ami-04d29b6f966df1537',
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
              'Value': 'janevieve_MatakoYakeX3'
            },
            {
              'Key': 'owner',
              'Value': 'me'
            },
          ]
        },
      ],
 )

