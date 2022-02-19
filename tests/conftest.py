import time

import docker
import pytest


@pytest.fixture(autouse=True)
def testing_env(monkeypatch):
    """Set ENV variables for testing."""
    monkeypatch.setenv("API_SERVER_PORT", "5002")
    monkeypatch.setenv("API_SERVER_URL", "http://127.0.0.1:5002")


@pytest.fixture(scope="module")
def api_server():
    """Starts a mock api server in a docker container."""
    image_name = "wrapy-test-api-server-fixture"
    client = docker.from_env()
    client.images.build(path="tests/api_server", tag=image_name)
    container = client.containers.run(
        image=image_name,
        auto_remove=True,
        detach=True,
        ports={5000: 5002},
        name=image_name,
    )

    time.sleep(2)

    yield

    container.kill()
