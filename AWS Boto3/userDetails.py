import boto3

iam_client = boto3.client('iam')
iam_resource = boto3.resource('iam')

# This script would get IAM users details

# Dictionary to get all iam users
user_details={}
iam_account_details = iam_client.get_account_authorization_details()

#print(iam_account_details)

# Create through the list and add specified details in dictionary format
for user in iam_account_details['UserDetailList']:
    username = user['UserName']
    policies = user['AttachedManagedPolicies']

    user_details[username] = {
            'userId': user['UserId'],
            'arn': user['Arn'],
            'groups': user['GroupList'],
            'policies': policies,
            'createDate': user['CreateDate'],
        }


#LastUsedDate
#PasswordLastUsed
for key in user_details:
    print('Username:', key)
    print('User ID: ',     user_details[key]['userId'])
    print('arn: ',         user_details[key]['arn'])
    print('groups: ',      user_details[key]['groups'])
    print('policies: ',    user_details[key]['policies'])
    print('Create Date: ', user_details[key]['createDate'])
    print('Last Activity: ', user_details[key]['lastActivity'])
    user = iam_resource.User(key)
    print('Password last usedS: ', user.password_last_used)
    print("\n")
