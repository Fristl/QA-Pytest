"""Module with https://www.openbrewerydb.org/ api."""

from __future__ import annotations

from typing import TYPE_CHECKING
from typing import Any

from src.api.base import Request
from src.api.base import check_integer_param
from src.api.base import check_string_param


if TYPE_CHECKING:
    from requests import Response


brewery_request = Request("https://api.openbrewerydb.org/v1/breweries/")


def list_breweries(**kwargs: Any) -> Response:
    return brewery_request("", params=kwargs)


def random_brewery(count: int = 1) -> Response:
    check_integer_param(count)
    return brewery_request("random", params={"size": count})


def single_brewery(brewery_id: str) -> Response:
    check_string_param(brewery_id)
    return brewery_request(brewery_id)


def search_brewery(q: str = "", page: int = 1) -> Response:
    check_string_param(q)
    check_integer_param(page)
    return brewery_request("search", params={"query": q, "page": page})
