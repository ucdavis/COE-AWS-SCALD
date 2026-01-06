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

