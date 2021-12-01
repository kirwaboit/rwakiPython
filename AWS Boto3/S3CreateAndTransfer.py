import boto3
import logging
from botocore.exceptions import ClientError
'''
Create a BOTO3 Python script that takes in access_key/secret_key/region and do the following.
a. List all the buckets in your account
b. Create a new bucket using BOTO3 script
c. Copy a file from one bucket to another
# s3 = boto3.client('s3')
'''

# Retrieve the list of existing buckets
s3 = boto3.client('s3')
response = s3.list_buckets()

# Output the bucket names
print('Existing buckets:') 
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')

s3 = boto3.client('s3')
s3.create_bucket(Bucket='yo-buckit')
# BUCKET_NAME = 'rwaki-practice-bucket-1'
# BUCKET_FILE_NAME = 's3boto3TestFile.txt'
# LOCAL_FILE_NAME = 's3CopyYay.txt'
# def download_s3_file():
#     s3 = boto3.client('s3')
#     s3.download_file(BUCKET_NAME, BUCKET_FILE_NAME, LOCAL_FILE_NAME)

# download_s3_file()




# s3 = boto3.resource('s3')
# source= {​​​​​​​​ 'Bucket' : 'argwack','Key':'barbie_key'}​​​​​​​​
# dest ={​​​​​​​​ 'Bucket' : 'boto3demo-bucket','Key':'barbie_key'}​​​​​​​​
# s3.meta.client.copy(source,dest)
 
# s3 = boto3.resource('s3')
# copy_source = {'Bucket':'rwaki-practice-bucket-2','Key':'copyTextYay.txt'}

# s3.meta.client.copy(copy_source,'rwaki-practice-bucket-1','s3boto3TestFile.txt')


s3 = boto3.resource('s3')
copy_source = {
    'Bucket': 'rwaki-practice-bucket-1',  #Source Bucket
    'Key': 's3boto3TestFile.txt'    #file in source bucket to copy
}
bucket = s3.Bucket('rwaki-practice-bucket-2') #Destination Bucket
obj = bucket.Object('copyTextYay.txt')   #you can change this and name your file anything you want in the destination bucket
#obj.copy(copy_source)


