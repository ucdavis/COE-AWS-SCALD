""" 
Title: aws-dynamodb-create-table-example.py
Authors: Dean Bunn and Ben Clark
Last Edit: 2025-12-30
"""

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