import boto3

iam_client = boto3.client('iam')


response = iam_client.generate_service_last_accessed_details(
    Arn='string',
    Granularity='SERVICE_LEVEL'|'ACTION_LEVEL'
)


print(response)