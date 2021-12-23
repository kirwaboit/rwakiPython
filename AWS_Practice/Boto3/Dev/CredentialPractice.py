import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')
response = ec2.create_key_pair(KeyName='rwakiNewKeyPair24')
print(response)