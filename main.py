import os
from dotenv import load_dotenv
import boto3

# Load the .env variables to this project to be fetched.
load_dotenv()

# Fetch variables from .env, the string inside os.getenv() is the variable name inside .env file.
profile = os.getenv('AWS_PROFILE')

# Because I have defined the profile, I don't need to configure anything else on the boto3.
sess = boto3.Session(profile_name=profile)

s3_client = sess.client('s3')

print(s3_client.list_buckets())