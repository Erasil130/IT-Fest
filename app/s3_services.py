import boto3
from botocore.exceptions import BotoCoreError, ClientError
from config import Config

def download_config_file(local_path: str):
    s3 = boto3.client(
        "s3",
        region_name=Config.S3_REGION,
        aws_access_key_id=Config.AWS_ACCESS_KEY,
        aws_secret_access_key=Config.AWS_SECRET_KEY,
    )
    try:
        s3.download_file(Config.S3_BUCKET_NAME, Config.CONFIG_FILE_NAME, local_path)
        return True
    except (BotoCoreError, ClientError) as e:
        print(f"Error downloading file: {e}")
        return False
