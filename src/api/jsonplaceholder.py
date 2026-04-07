"""Module with https://www.openbrewerydb.org/ api."""

from __future__ import annotations

from typing import TYPE_CHECKING
from typing import Any

from src.api.base import Request
from src.api.base import check_integer_param


if TYPE_CHECKING:
    from requests import Response


placeholder_request = Request("https://jsonplaceholder.typicode.com/")
placeholder_request_create = Request(
    "https://jsonplaceholder.typicode.com/",
    "POST",
    headers={"Content-type": "application/json; charset=UTF-8"},
)
placeholder_request_update = Request(
    "https://jsonplaceholder.typicode.com/",
    "PUT",
    headers={"Content-type": "application/json; charset=UTF-8"},
)
placeholder_request_delete = Request(
    "https://jsonplaceholder.typicode.com/",
    "DELETE",
)


def create_resource(kind: str, body: dict) -> Response:
    return placeholder_request_create(kind, body=body)


def read_resource(
    kind: str,
    item_id: int | None = None,
    **kwargs: Any,
) -> Response:
    url = kind
    if item_id:
        check_integer_param(item_id)
        url += f"/{item_id}"
    return placeholder_request(url, params=kwargs)


def update_resource(kind: str, item_id: int, body: dict) -> Response:
    check_integer_param(item_id)
    url = kind + f"/{item_id}"
    return placeholder_request_update(url, body=body)


def delete_resource(kind: str, item_id: int) -> Response:
    check_integer_param(item_id)
    url = kind + f"/{item_id}"
    return placeholder_request_update(url)
