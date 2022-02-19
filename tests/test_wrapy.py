import os

import pytest
from requests.exceptions import HTTPError

from wrapy.wrapy import Api


@pytest.mark.parametrize("url", ["https://api.github.com", "https://api.github.com/"])
def test_github_api_existing_path_returns_valid_data(url):
    github = Api(url)
    repos = github.users.grishasergii.repos()
    assert repos


def test_github_api_path_does_not_exist_returns_not_found():
    github = Api("https://api.github.com")
    with pytest.raises(HTTPError):
        response = github.users.agvekgvace757362fgvj23yt.repos()
        pass


def test_getitem_and_getattr_returns_valid_response(api_server):
    api = Api(os.environ["API_SERVER_URL"])
    resource_id = "test-resource-1"
    response = api.tests[resource_id]()

    assert response["data"] == resource_id
