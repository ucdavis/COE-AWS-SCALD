import json
import boto3

#Create AWS Session with Specific Region Location
session = boto3.Session(region_name="us-west-2")

#Initiate DynamioDB Resource for Tasks
dynamodb = session.resource('dynamodb')

def lambda_handler(event, context):
    
    #Report Object
    coerpt = {'status':'green','data':[]}

    #Pull Kudos Table
    coe_table = dynamodb.Table("COE-IT-Kudos")
    
    #Retrieve All Items from Table
    coe_tblscan = coe_table.scan()

    #Loop Through Items and Add Them to Return Object
    for item in coe_tblscan['Items']:
        coerpt['data'].append(item)


    #Return Report Object
    return coerpt