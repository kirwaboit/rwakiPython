mport boto3
import os

# Create an S3 client
s3 = boto3.client('s3')
bucket_name = os.environ['rwaki-practice-bucket-1'] # Supplied by Function service-discovery wire

def handler(message, context):

# Add a file to your Object Store
    response = s3.put_object(
    Bucket=bucket_name,
    Key='randomTextFile2.txt',
    Body='Sample Text',
    ACL='public-read'
    )
    return response