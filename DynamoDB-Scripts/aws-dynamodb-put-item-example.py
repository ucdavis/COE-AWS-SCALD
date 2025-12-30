""" 
Title: aws-dynamodb-put-item-example.py
Authors: Dean Bunn and Ben Clark
Last Edit: 2025-12-30
"""

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





