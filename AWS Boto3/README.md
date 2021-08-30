# Setting up your account to use Boto3 Python Library  

## About Credentials

- When you create a user , you get credentials that identify them, those creds are what you input into aws cli to access your AWS account using boto3 
- After you download amazon cli and configure it, make sure to ensure you have a .aws file in your "user" directory, and that file has your latest "active" credentials.Make sure it has your 2 config files and that both have your credentials identified  
- Boto3 uses credentials set up on your machine when you ran AWS-configure, the creds are updated and stored in user/.aws folder

Config file (does not have an extension)

                [default]   s
                region = us-east-1  
                output = json  

Credentials file  (does not have an extension) 

                [default]  
                aws_access_key_id = XXXXXX  
                aws_secret_access_key = XXXXXXXXXX  



## IAM  
- Stands for Identity Access Management. It is global, you don't need to specify a region, applies to users and groups  
- A group simply is a place to store users.Users in a group inherit all the permissions within it.  
- To set permissions for a group, you need to apply a policy to that group
- NB the "Last Activity" updates every 4 hours*


## Key Pairs  
- These are particular to the region you created them in e.g N. Virginia i.e us-east-1  
- The keypair is used to access i.e login to your aws servers/EC2 instances
- when you create an EC2 you need to attach a keypair to it. It will prompt you to attach an existing one or create a new one  



## Cloud Watch  
- For setting up alarms related to billing


## TODO
- make the last use code take timezone  from local pc  
- create users and assign policy  
- query state of assets/resources  in AWS go off of this : https://stackoverflow.com/questions/53185119/aws-python-script-to-retrieve-list-of-resources-are-currently-in-use  
- access s3  
- use a lambda on an s3  
- configure elastic load balancer 
- understand pagination tokens  
- understand this code https://aws.amazon.com/blogs/architecture/how-to-efficiently-extract-and-query-tagged-resources-using-the-aws-resource-tagging-api-and-s3-select-sql/ 

