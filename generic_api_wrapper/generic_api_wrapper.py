"""Main module."""
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class RetrySession:  # pylint: disable=too-few-public-methods
    """Session object with retry capabilities."""

    def __init__(self):
        self.session = None

    def _requests_retry_session(
        self, retries=5, backoff_factor=2, status_forcelist=(500, 502, 503, 504)
    ):
        """Returns a retriable session."""
        if self.session:
            return self.session

        session = requests.Session()
        retry = Retry(
            total=retries,
            read=retries,
            connect=retries,
            backoff_factor=backoff_factor,
            status_forcelist=status_forcelist,
            allowed_methods={"GET"},
        )
        adapter = HTTPAdapter(max_retries=retry)
        session.mount("https://", adapter)

        self.session = session

        return self.session

    def get(self, url, **kwargs):
        """GET method forwarded to a session object."""
        return self._requests_retry_session().get(url, **kwargs)

    def post(self, url, **kwargs):
        """POST method forwarded to a session object."""
        return self._requests_retry_session().post(url, **kwargs)

    def delete(self, url, **kwargs):
        """DELETE method forwarded to a session object."""
        return self._requests_retry_session().delete(url, **kwargs)


class Api:
    """Api wrapper object."""

    def __init__(self, base_url, auth=None):
        """Creates an API wrapper object.

        Args:
            base_url: string
            auth: Auth tuple or callable to enable authentication, passed to the session
        """
        self.base_url = base_url.rstrip("/")
        self._session = RetrySession()
        self.parent = None
        self._auth = auth

    @classmethod
    def _from_parent(cls, url, parent):
        api = cls(url)
        api.parent = parent
        return api

    def __getattr__(self, item):
        new_base = f"{self.base_url}/{item}"
        return self.__class__._from_parent(new_base, self)

    def __getitem__(self, item):
        new_base = f"{self.base_url}/{item}"
        return self.__class__._from_parent(new_base, self)

    def __call__(self, **kwargs):
        return self.get(**kwargs)

    @property
    def session(self):
        if self.parent:
            return self.parent.session
        return self._session

    @property
    def auth(self):
        if self.parent:
            return self.parent.auth
        return self._auth

    def _make_request(self, method, **kwargs):
        session_method = getattr(self.session, method)
        response = session_method(self.base_url, auth=self.auth, **kwargs)

        response.raise_for_status()
        if response.text:
            return response.json()
        return {}

    def get(self, **kwargs):
        """GET request."""
        return self._make_request("get", **kwargs)

    def post(self, **kwargs):
        """POST request."""
        return self._make_request("post", **kwargs)

    def put(self, **kwargs):
        """PUT request."""
        return self._make_request("post", **kwargs)

    def delete(self, **kwargs):
        """DELETE request."""
        return self._make_request("delete", **kwargs)
