from typing import Any
import warnings

import httpx

from .types import APIVersion


class LightspeedX(object):
    """
    A Python client for interacting with the Lightspeed X-Series API.

    Args:
        personal_token (str): Your Lightspeed personal access token.
        domain_prefix (str): Your Lightspeed store domain prefix.
        debug (bool, optional): Whether to enable debug logging. Defaults to False.
    """

    def __init__(self, personal_token: str, domain_prefix: str, debug=False) -> None:
        """
        Initializes a new LightspeedX client.

        Args:
            personal_token (str): Your Lightspeed personal access token.
            domain_prefix (str): Your Lightspeed store domain prefix.
            debug (bool, optional): Whether to enable debug logging. Defaults to False.
        """
        self._personal_token = personal_token
        self.domain_prefix = domain_prefix
        self.debug = debug

        self._client = httpx.Client(
            headers={"Authorization": f"Bearer {self._personal_token}"}
        )

    def __repr__(self) -> str:
        """
        Returns a string representation of the LightspeedX client.

        Returns:
            str: A string representation of the client.
        """
        return f"Lightspeed(domain_prefix={self.domain_prefix})"

    @property
    def personal_token(self) -> str:
        """
        Gets the personal access token used for authentication.

        Returns:
            str: The personal access token.
        """
        return self._personal_token

    @personal_token.setter
    def personal_token(self, value: str) -> None:
        """
        Sets the personal access token used for authentication.

        Args:
            value (str): The new personal access token.
        """
        self._personal_token = value
        self._client.headers["Authorization"] = f"Bearer {value}"

    def request(
        self,
        method: str,
        path: str,
        params: Any = None,
        data: Any = None,
        api_version: APIVersion = "2.0",
    ) -> Any:
        """
        Performs an HTTP request to the Lightspeed eCom API.

        Args:
            method (str): The HTTP method to use (e.g., "GET", "POST", "PUT", "DELETE").
            path (str): The API endpoint path.
            params (Any, optional): A dictionary of query parameters. Defaults to None.
            data (Any, optional): The request body data. Defaults to None.
            api_version (str, optional): The API version to use. Defaults to "2.0".

        Returns:
            Any: The JSON-parsed response from the API.

        Raises:
            httpx.HTTPStatusError: If the API request fails.
        """
        if api_version == "0.9":
            warnings.warn(
                "API Version 0.9 is depreciated. Consider using Version 2.0 instead."
            )

        if not path.startswith("/"):
            path = "/" + path

        url = f"https://{self.domain_prefix}.vendhq.com/api/{api_version}{path}"
        res = self._client.request(method, url, params=params, json=data)

        if self.debug:
            print(f"Request URL: {res.request.url}")

        res.raise_for_status()
        return res.json()

    def get(
        self,
        path: str,
        params: Any = None,
        data: Any = None,
        api_version: APIVersion = "2.0",
    ) -> Any:
        """
        Performs a GET request to the Lightspeed eCom API.

        Args:
            path (str): The API endpoint path.
            params (Any, optional): A dictionary of query parameters. Defaults to None.
            data (Any, optional): The request body data. Defaults to None.
            api_version (str, optional): The API version to use. Defaults to "2.0".

        Returns:
            Any: The JSON-parsed response from the API.

        Raises:
            httpx.HTTPStatusError: If the API request fails.
        """
        return self.request("GET", path, params, data, api_version)

    def post(
        self,
        path: str,
        params: Any = None,
        data: Any = None,
        api_version: APIVersion = "2.0",
    ) -> Any:
        """
        Performs a POST request to the Lightspeed eCom API.

        Args:
            path (str): The API endpoint path.
            params (Any, optional): A dictionary of query parameters. Defaults to None.
            data (Any, optional): The request body data. Defaults to None.
            api_version (str, optional): The API version to use. Defaults to "2.0".

        Returns:
            Any: The JSON-parsed response from the API.

        Raises:
            httpx.HTTPStatusError: If the API request fails.
        """
        return self.request("POST", path, params, data, api_version)

    def put(
        self,
        path: str,
        params: Any = None,
        data: Any = None,
        api_version: APIVersion = "2.0",
    ) -> Any:
        """
        Performs a PUT request to the Lightspeed eCom API.

        Args:
            path (str): The API endpoint path.
            params (Any, optional): A dictionary of query parameters. Defaults to None.
            data (Any, optional): The request body data. Defaults to None.
            api_version (str, optional): The API version to use. Defaults to "2.0".

        Returns:
            Any: The JSON-parsed response from the API.

        Raises:
            httpx.HTTPStatusError: If the API request fails.
        """
        return self.request("PUT", path, params, data, api_version)

    def delete(
        self,
        path: str,
        params: Any = None,
        data: Any = None,
        api_version: APIVersion = "2.0",
    ) -> Any:
        """
        Performs a DELETE request to the Lightspeed eCom API.

        Args:
            path (str): The API endpoint path.
            params (Any, optional): A dictionary of query parameters. Defaults to None.
            data (Any, optional): The request body data. Defaults to None.
            api_version (str, optional): The API version to use. Defaults to "2.0".

        Returns:
            Any: The JSON-parsed response from the API.

        Raises:
            httpx.HTTPStatusError: If the API request fails.
        """
        return self.request("DELETE", path, params, data, api_version)
