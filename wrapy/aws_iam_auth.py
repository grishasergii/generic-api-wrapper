from urllib.parse import urlparse

import boto3
from aws_requests_auth.boto_utils import BotoAWSRequestsAuth


class AwsIamAuth:
    """AWS IAM authenticator."""

    def __init__(self, api_url):
        api_host = urlparse(api_url).netloc

        aws_session = boto3.session.Session()
        aws_region = aws_session.region_name

        self._auth = BotoAWSRequestsAuth(
            aws_host=api_host, aws_region=aws_region, aws_service="execute-api"
        )

    @property
    def auth(self):
        """auth object."""
        return self._auth
