""" 
Title: aws-s3-view-buckets-example.py
Authors: Dean Bunn and Ben Clark
Last Edit: 2025-12-29
"""

import boto3

#Create AWS Session Using Specific Profile (Not Default)
session = boto3.Session(profile_name="deanbunn",region_name="us-west-2")

#Initiate S3 Session
s3 = session.resource('s3')

#View All Buckets
for bucket in s3.buckets.all():
    print(bucket.name)


