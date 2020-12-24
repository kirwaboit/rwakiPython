import boto3
import json

'''
1. Create a Lambda function that triggers the Lambda function and prints the name of the bucket and the
name of file when you upload a file to a S3 bucket
'''

s3 = boto3.resource('s3')
#get the bucket name
def lambda_handler(event, context):

    #1. Get the bucket name
    bucket = event['Records'][0]['s3']['bucket']['name']   #dictionary lookup notation

    #get the file/key name
    Key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding ='utf-8')

    try:
        #fetch the file from s3
        response = s3.get_object(Bucket=bucket, Key=key)
        #deserialize the file content
        text = response["Body"].read().decode()
        data = json.loads(text)

        #print the content
        print(data)

        #parse and print the transcation
        transcations = data['transactions']
        for record in transcations:
            print(record['transType'])
        return 'Success!'

    except Exception as e:
        print (e)
        raise e