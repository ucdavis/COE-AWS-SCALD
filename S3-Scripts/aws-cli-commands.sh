# AWS Command Line Interface (AWS CLI) Commands

# Instructions for Installing the AWS CLI
# https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

# After Installation Configure Profile with Credentials Received from AWS Account Admin
# Set Region: us-west-2
# Output option: json
aws configure

# Setting Default Region and Output Options If You Missed It During Setup
aws configure set region us-west-2
aws configure set output json

# Configure a Named Profile
aws configure --profile deanbunn

# Show Configured Profiles
aws configure list-profiles

# Show Configuration Settings for Default Profile
aws configure list

# Show Configuration Settings for Named Profile
aws configure list --profile deanbunn

# List S3 Buckets
aws s3 ls

# View Content of a Bucket
aws s3 ls s3://engr-dev-db/

# Upload a Single File to the Bucket
aws s3 cp c:\path\to\local\Website-Demo\index.html s3://engr-dev-db

# Sync a Folder to a Bucket (Will Remove s3 Files Not Found in Local Folder)
aws s3 sync c:\path\to\local\Website-Demo s3://engr-dev-db --delete 

# Do a Dry Run of Sync'n a Folder to a Bucket
aws s3 sync c:\path\to\local\Website-Demo s3://engr-dev-db --delete --dryrun



