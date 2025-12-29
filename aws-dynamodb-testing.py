""" 
Title: aws-dynamodb-testing.py
Authors: Dean Bunn and Ben Clark
Last Edit: 2025-12-29
"""

import boto3

#Create AWS Session Using Specific Profile (Not Default)
session = boto3.Session(profile_name="deanbunn",region_name="us-west-2")

#Initiate DynamioDB Resource for Tasks
dynamodb = session.resource('dynamodb')

#Create New Table for COE IT Staff Voting
new_coetable = dynamodb.create_table(
    TableName="COE-IT-Kudos",
    KeySchema=[
        {"AttributeName": "email_address", "KeyType":"HASH"},
        {"AttributeName": "submitted_on", "KeyType": "RANGE"},
    ],
    AttributeDefinitions=[
        {"AttributeName": "email_address", "AttributeType": "S"},
        {"AttributeName": "submitted_on", "AttributeType": "S"}, 
        {"AttributeName": "kudo", "AttributeType": "S"},
        {"AttributeName": "submitter", "AttributeType": "S"},
    ],
    LocalSecondaryIndexes=[
        {
            "IndexName": "lsi_by_submitter",
            "KeySchema":[
                {"AttributeName": "email_address", "KeyType": "HASH"},
                {"AttributeName": "submitter", "KeyType": "RANGE"},
            ],
            "Projection":{
                "ProjectionType": "INCLUDE",
                "NonKeyAttributes": ["submitted_on","kudo"],
            }
        },
    ],
    TableClass='STANDARD',
)

new_coetable.wait_until_exists()

print("Created:", new_coetable.table_name)









"""
#View All Tables
for table in dynamodb.tables.all():
   print(table.name)

"""

"""
coe_table = dynamodb.Table('COE-DevOps')

coe_tblscan = coe_table.scan()

for item in coe_tblscan['Items']:
    print(item['EmailAddress'])

"""

"""
{'EmailAddress': 'benclark@ucdavis.edu', 'DisplayName': 'Ben Clark', 'ServiceYears': Decimal('12'), 'StaffId': '534510'}
{'EmailAddress': 'dbunn@ucdavis.edu', 'DisplayName': 'Dean Bunn', 'ServiceYears': Decimal('20'), 'StaffId': '12803'}
{'EmailAddress': 'ecblosch@ucdavis.edu', 'DisplayName': 'Eric Blosch', 'ServiceYears': Decimal('10'), 'StaffId': '831158'}

"""