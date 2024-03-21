import os
from dotenv import load_dotenv
import boto3


load_dotenv()

profile = os.getenv('AWS_PROFILE')

sess = boto3.Session(profile_name=profile)

s3_client = sess.client('s3')

print(s3_client.list_buckets())