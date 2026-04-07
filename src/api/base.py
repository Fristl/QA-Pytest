"""Module with base functionality."""

from __future__ import annotations

from typing import Any
from urllib.parse import urljoin

from requests import Response
from requests import request
from webob.exc import HTTPBadRequest


class Request:
    """Custom request class."""

    def __init__(
        self,
        domain: str,
        method: str = "GET",
        params: dict | None = None,
        headers: dict | None = None,
        body: dict | None = None,
    ):
        self.domain = domain
        self.method = method
        self.params = params
        self.headers = headers
        self.body = body

    def __call__(
        self,
        url: str,
        method: str | None = None,
        params: dict | None = None,
        headers: dict | None = None,
        body: dict | None = None,
    ) -> Response:
        """Make a request."""
        _method = method or self.method
        _params = params or self.params
        _headers = headers or self.headers
        _body = body or  self.body
        _url = urljoin(self.domain, url)
        return request(
            _method,
            _url,
            params=params,
            headers=_headers,
            json=_body,
            timeout=10,
        )


def check_integer_param(param: Any) -> None:
    try:
        if not isinstance(param, int):
            raise TypeError  # noqa: TRY301
    except TypeError as exc:
        raise HTTPBadRequest from exc


def check_number_param(param: int | str) -> None:
    try:
        _param = str(param)
        if not _param.isdigit():
            raise ValueError  # noqa: TRY301
    except (TypeError, ValueError) as exc:
        raise HTTPBadRequest from exc


def check_string_param(param: Any) -> None:
    try:
        _param = str(param)
    except TypeError as exc:
        raise HTTPBadRequest from exc


def check_alpha_param(param: Any) -> None:
    try:
        _param = str(param)
        if _param.isalpha():
            raise ValueError  # noqa: TRY301
    except (TypeError, ValueError) as exc:
        raise HTTPBadRequest from exc



