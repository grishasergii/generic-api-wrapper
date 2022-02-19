# Generic API wrapper

version=0.1.0

`wrapy` is a generic REST API python wrapper. It comes with an AWS IAM authenticator out of the box. 

# Getting started

## Install
`pip install wrapy`

## Usage

### Basic usage
```python
from wrapy import Api


# To create an API wrapper object provide base url
# Let's take Github for example
api = Api("https://api.github.com")

# Get repos of a user
# This is equivalent to sending a GET request to
# https://api.github.com/users/grishasergii/repos
repos = api.users.grishasergii.repos()

# If a resource name violates Python attributes syntax then use __getitem__
# This is equivalent to sending a GET request to
# https://api.i-do-not-exist.com/resources/imaginary-resource
imaginary_api = Api("https://api.i-do-not-exist.com")
resource = api.resources["imaginary-resource"]()

# provide data for POST request
imaginary_api.resources.post(data={"name": "resource-name"})
```

### Authentication
- AWS IAM authnetication
```python
from wrapy import Api, AwsIamAuth


api_url = "https://api.aws-powered-api.com"

# AWS IAM authentication. Credentials and AWS region are inferred by boto3 from the app environment
auth = AwsIamAuth(api_url).auth

# Create an API wrapper object that is authenticated to call an API configured with an AWS IAM authorizer
api = Api(api_url, auth)
```
- custom authenticator: create a custom authenticator that fits your requirements 
and provide it to the `Api` constructor, it will be passed to the `session` object when sending a request.

# License

Free software: MIT license

# Credits

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

- Cookiecutter: https://github.com/audreyr/cookiecutter
- `audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
