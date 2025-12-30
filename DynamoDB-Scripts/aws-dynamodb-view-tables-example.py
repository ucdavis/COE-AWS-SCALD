""" 
Title: aws-dynamodb-view-tables-example.py
Authors: Dean Bunn and Ben Clark
Last Edit: 2025-12-30
"""

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


