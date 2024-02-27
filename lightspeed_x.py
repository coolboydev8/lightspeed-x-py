from typing import Any

import httpx


class LightspeedX(object):
    def __init__(self, personal_token: str, domain_prefix: str, debug=False) -> None:
        self._personal_token: str = personal_token
        self.domain_prefix: str = domain_prefix
        self.debug: bool = debug

        self._client = httpx.Client(
            headers={
                "Authorization": f"Bearer {self._personal_token}",
            }
        )

    def __repr__(self) -> str:
        return f"Lightspeed(domain_prefix={self.domain_prefix})"

    @property
    def personal_token(self) -> str:
        return self._personal_token

    @personal_token.setter
    def personal_token(self, value: str) -> None:
        self._personal_token = value
        self._client.headers["Authorization"] = f"Bearer {value}"

    def request(
        self,
        method: str,
        path: str,
        params: Any = None,
        data: Any = None,
        api_version="2.0",
    ) -> Any:
        if not path.startswith("/"):
            path = "/" + path

        url = f"https://{self.domain_prefix}.vendhq.com/api/{api_version}{path}"
        res = self._client.request(method, url, params=params, json=data)

        if self.debug:
            print(f"Request URL: {res.request.url}")

        res.raise_for_status()
        return res.json()

    def get(
        self, path: str, params: Any = None, data: Any = None, api_version="2.0"
    ) -> Any:
        return self.request("GET", path, params, data, api_version)

    def post(
        self, path: str, params: Any = None, data: Any = None, api_version="2.0"
    ) -> Any:
        return self.request("POST", path, params, data, api_version)

    def put(
        self, path: str, params: Any = None, data: Any = None, api_version="2.0"
    ) -> Any:
        return self.request("PUT", path, params, data, api_version)

    def delete(
        self, path: str, params: Any = None, data: Any = None, api_version="2.0"
    ) -> Any:
        return self.request("DELETE", path, params, data, api_version)
