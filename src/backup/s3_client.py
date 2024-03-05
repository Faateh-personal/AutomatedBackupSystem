import boto3


def upload_to_s3(file_path, bucket, object_name):
    """Uploads a file to an S3 bucket."""
    s3_client = boto3.client('s3')
    s3_client.upload_file(file_path, bucket, object_name)
