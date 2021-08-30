import boto3

#ec2_resource = boto3.resource('ec2', region_name='ap-southeast-2')
ec2_resource = boto3.resource('ec2')

#instance = ec2_resource.Instance('i-0b2b7ca94e00cfb8c')
instance = ec2_resource.Instance(IncludeAllInstances=True)
print(instance.state['Name'])



# if instance.state['Name'] == 'running':
#     print('It is running')
# if instance.state['Name'] == 'stopping':
#     print('It is stopping')
# if instance.state['Name'] == 'stopped':
#     #print('It is stopped')