## COE AWS SCALD

A demonstration project showcasing AWS S3, CloudFront, API Gateway, Lambda, and DynamoDB.

Project overview: CloudFront delivers the site and static assets hosted in S3. Client-side requests are routed through API Gateway to Lambda functions that handle CRUD operations on DynamoDB tables.

### AWS Command Line Interface (AWS CLI) Configuration and Usage

[Instructions for Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

After installation, configure AWS profile with credentials received from AWS account admin.
```bash
aws configure
# Set Region: us-west-2
# Output option: json
```
Setting Default Region and Output options If you missed during setup.
```bash
aws configure set region us-west-2
aws configure set output json
```
Configure a named profile
```bash
aws configure --profile deanbunn
```
Show configured profiles
```bash
aws configure list-profiles
```
Show configuration settings for default profile
```bash
aws configure list
```
Show configuration settings for named profile
```bash
aws configure list --profile deanbunn
```
List S3 buckets
```bash
aws s3 ls
```
View content of a bucket
```bash
aws s3 ls s3://engr-dev-db/
```
Upload a single file to the bucket
```bash
aws s3 cp c:\path\to\local\Website-Demo\index.html s3://engr-dev-db
```
Sync a folder to a bucket. Will remove s3 files not found in local folder.
```bash
aws s3 sync c:\path\to\local\Website-Demo s3://engr-dev-db --delete 
```
Do a dry run of sync'n a folder to a bucket
```bash
aws s3 sync c:\path\to\local\Website-Demo s3://engr-dev-db --delete --dryrun
```

### IAM Policies for S3 and DynamioDB

The first example IAM policy allows the group it's assigned to list all the S3 buckets but only modify the bucket related to their website. The second configures restricted access to a specific DynamoDB table. 
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "s3:ListAllMyBuckets",
            "Resource": "*"
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": [
                "s3:ListBucketMultipartUploads",
                "s3:ListBucket",
                "s3:GetBucketLocation"
            ],
            "Resource": "arn:aws:s3:::engr-dev-db"
        },
        {
            "Sid": "VisualEditor2",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObjectAcl",
                "s3:GetObject",
                "s3:AbortMultipartUpload",
                "s3:DeleteObjectVersion",
                "s3:PutObjectVersionAcl",
                "s3:GetObjectVersionAcl",
                "s3:DeleteObject",
                "s3:PutObjectAcl",
                "s3:GetObjectVersion"
            ],
            "Resource": "arn:aws:s3:::engr-dev-db/*"
        }
    ]
}
```
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Statement1",
            "Effect": "Allow",
            "Action": [
                "dynamodb:GetItem",
                "dynamodb:Query",
                "dynamodb:Scan",
                "dynamodb:PutItem"
            ],
            "Resource": [
                "arn:aws:dynamodb:us-west-2:<account-number>:table/COE-IT-Kudos",
                "arn:aws:dynamodb:us-west-2:<account-number>:table/COE-IT-Kudos/index/*"
            ]
        }
    ]
}
```

### DynamoDB Example Scripts (Local)

These Python scripts require the [boto3 library](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html) be installed. 

Creating a table with a local secondary index. 
```python
import boto3

#Create AWS Session Using Specific Profile (Not Default) and Region Location
session = boto3.Session(profile_name="deanbunn",region_name="us-west-2")

#Initiate DynamioDB Resource for Tasks
dynamodb = session.resource('dynamodb')

#Create New Table for COE IT Staff Voting
new_coetable = dynamodb.create_table(
    TableName="COE-IT-Kudos",
    KeySchema=[
        {"AttributeName": "email_address", "KeyType":"HASH"},
        {"AttributeName": "submitted_on", "KeyType": "RANGE"}
    ],
    AttributeDefinitions=[
        {"AttributeName": "email_address", "AttributeType": "S"},
        {"AttributeName": "submitted_on", "AttributeType": "S"},
        {"AttributeName": "submitter", "AttributeType": "S"}
    ],
    LocalSecondaryIndexes=[
        {
            "IndexName": "lsi_by_submitter",
            "KeySchema":[
                {"AttributeName": "email_address", "KeyType": "HASH"},
                {"AttributeName": "submitter", "KeyType": "RANGE"}
            ],
            "Projection":{
                "ProjectionType": "ALL",
            }
        }
    ],
    TableClass="STANDARD",
    BillingMode="PAY_PER_REQUEST"
)

#Wait for Table Creation Process
new_coetable.wait_until_exists()

#Display Newly Created Table Name
print("Created:", new_coetable.table_name)
```
Adding an item to a table
```python
import boto3
from datetime import datetime

#Create AWS Session Using Specific Profile (Not Default) and Region Location
session = boto3.Session(profile_name="deanbunn",region_name="us-west-2")

#Initiate DynamioDB Resource for Tasks
dynamodb = session.resource('dynamodb')

#Var for Kudo Timestamp
kudo_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#Dict for Put Item Function
coe_kudo = { "email_address": "",
             "submitted_on": "",
             "submitter": "",
             "kudo": ""
           }

#Load Required Values into Dict
coe_kudo["email_address"] = "benclark@ucdavis.edu"
coe_kudo["submitted_on"] = kudo_timestamp
coe_kudo["submitter"] = "dbunn@ucdavis.edu"
coe_kudo["kudo"] = "Ben rocked out my cert issue"

#Retrieve Table to Put Item into
coe_table = dynamodb.Table("COE-IT-Kudos")

#Put Item into Table
coe_response = coe_table.put_item(Item=coe_kudo)

#View Put Call Response
print(coe_response)
```
View all items in a table
```python
import boto3

#Create AWS Session Using Specific Profile (Not Default) and Region Location
session = boto3.Session(profile_name="deanbunn",region_name="us-west-2")

#Initiate DynamioDB Resource for Tasks
dynamodb = session.resource('dynamodb')

#View All Tables
for table in dynamodb.tables.all():
   print(table.name)


#Pull a Table by Name
coe_table = dynamodb.Table("COE-IT-Kudos")

#Retrieve All Items in a Table
coe_tblscan = coe_table.scan()

#View All Those Table Items
for item in coe_tblscan['Items']:
    print(item)
```