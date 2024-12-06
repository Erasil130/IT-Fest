import os

class Config:
    S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME", "qwerty123456")
    S3_REGION = os.getenv("S3_REGION", "us-east-1")
    AWS_ACCESS_KEY = os.getenv("dgdQFSLrxHqjWPdRVPERPp")
    AWS_SECRET_KEY = os.getenv("4rpzWaQ1a4URRuf4bypWogQqdZYfWHk6Fc6twDtjEjBq")
    CONFIG_FILE_NAME = "config.bin"
