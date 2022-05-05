# A lot of this code from https://gist.github.com/leongjinqwen/9d9a2d58bf2fb923658820559a88a5ec
# and StackOverflow https://stackoverflow.com/questions/36272286/getting-access-denied-when-calling-the-putobject-operation-with-bucket-level-per

import boto3
import botocore
import logging
from botocore.exceptions import ClientError
import os
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

load_dotenv()


s3 = boto3.client(
    "s3",
    aws_access_key_id=os.environ.get('AWS_ACCESS_KEY'),
    aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY')
)


def upload_file_to_s3(file, acl="public-read"):
    filename = secure_filename(file.filename)
    try:
        s3.upload_fileobj(
            file,
            os.environ.get('AWS_BUCKET_NAME'),
            file.filename,
            ExtraArgs={
                # "ACL": acl,
                "ContentType": file.content_type
            }
        )

    except Exception as e:
        # This is a catch all exception, edit this part to fit your needs.
        print("Something Happened: ", e)
        return e

    try:
        response = s3.generate_presigned_url('get_object',
                                             Params={'Bucket': os.environ.get('AWS_BUCKET_NAME'),
                                                     'Key': file.filename})
    except ClientError as e:
        logging.error(e)
        return None

    file_package = [file.filename, response]

    # The response contains the presigned URL
    return file_package
