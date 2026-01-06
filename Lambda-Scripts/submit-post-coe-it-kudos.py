import json
import boto3

#Create AWS Session with Specific Region Location
session = boto3.Session(region_name="us-west-2")

#Initiate DynamioDB Resource for Tasks
dynamodb = session.resource('dynamodb')


def lambda_handler(event, context):
    
    #Var for Return Status
    rtn_status = ""

    if(len(event) == 4):
        coe_kudo = { "email_address": "","submitted_on": "","submitter": "","kudo": ""}
        coe_kudo["email_address"] = str(event['email_address'])
        coe_kudo["submitted_on"] = str(event['submitted_on'])
        coe_kudo["submitter"] = str(event['submitter'])
        coe_kudo["kudo"] = str(event['kudo'])
        coe_table = dynamodb.Table("COE-IT-Kudos")
        coe_response = coe_table.put_item(Item=coe_kudo)
        rtn_status = "Success"

    else:
        rtn_status = "Invalid Submission"




    return rtn_status