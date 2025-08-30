import boto3
from botocore.config import Config

ap_arn = "arn:aws:s3-object-lambda:us-east-1:211125589793:accesspoint/tutorial-object-lambda-accesspoint"
bucket_name = "tutorial-object-lambda-bucket-211125589793-new"

my_config = Config(
    region_name='us-east-1',
    signature_version='s3v4',
)
s3 = boto3.client('s3', config=my_config)

def getObject(bucket, key):
    objectBody = s3.get_object(Bucket = bucket, Key = key)
    print(objectBody["Body"].read().decode("utf-8"))

print('Original object from the S3 bucket:')
getObject(bucket=bucket_name, key="tutorial.txt")


# getObject(
#     bucket=ap_arn,
#     key="tutorial.txt"
#     )


