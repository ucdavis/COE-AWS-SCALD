""" 
Script: aws-testing.py
"""

import boto3

session = boto3.Session(profile_name="deanbunn",region_name="us-west-2")

s3 = session.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)

