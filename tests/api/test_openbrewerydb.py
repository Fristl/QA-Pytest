"""Module with tests for https://www.openbrewerydb.org/ api."""

from __future__ import annotations

import logging
from typing import Any

import pytest
from webob.exc import HTTPOk

from src.api.openbrewerydb import list_breweries
from src.api.openbrewerydb import random_brewery
from src.api.openbrewerydb import single_brewery


logger = logging.getLogger(__name__)


def parameter_mapper(parameter: str) -> str | None:
    return {
        "by_city": "city",
        "by_country": "country",
        "by_name": "name",
        "by_state": "state",
        "by_postal": "postal_code",
        "by_type": "brewery_type",
    }.get(parameter)


@pytest.mark.positive
@pytest.mark.parametrize(
    ("param_key", "param_value"),
    [
        ("by_city", "Norman"),
        ("by_country", "United States"),
        ("by_state", "Mississippi"),
        ("by_type", "bar"),
        ("by_type", "brewpub"),
    ],
)
def test_list_breweries_positive(
    session: Any,
    param_key: str,
    param_value: Any,
) -> None:
    resp = list_breweries(**{param_key: param_value})

    assert resp.ok, \
        "Request 'list_breweries' has status != 200"

    assert resp.status_code == HTTPOk.code, \
        "Request 'list_breweries' has status != 200"

    resp_json = resp.json()

    assert resp_json is not None, \
        "Request 'list_breweries' is None'"

    assert len(resp_json) > 0 , \
        "Request 'list_breweries' is empty"

    for item in resp_json:
        assert item.get(parameter_mapper(param_key)) == param_value, \
            f"Brewery {item} doesn't have parameter key - {param_key}"


@pytest.mark.positive
@pytest.mark.parametrize("count", [1, 5, 12])
def test_list_random_brewery_positive(session: Any, count: int) -> None:
    resp = random_brewery(count)

    assert resp.ok, \
        "Request 'random_brewery' has status != 200"

    assert resp.status_code == HTTPOk.code, \
        "Request 'random_brewery' has status != 200"

    resp_json = resp.json()

    assert resp_json is not None, \
        f"Request 'random_brewery' len must be {count}"


@pytest.mark.positive
@pytest.mark.parametrize("count", [1, 5, 12])
def test_random_brewery_positive(session: Any, count: int) -> None:
    resp = random_brewery(count)

    assert resp.ok, \
        "Request 'random_brewery' has status != 200"

    assert resp.status_code == HTTPOk.code, \
        "Request 'random_brewery' has status != 200"

    resp_json = resp.json()

    assert resp_json is not None, \
        f"Request 'random_brewery' len must be {count}"


@pytest.mark.positive
def test_single_brewery_positive(session: Any) -> None:
    _random_brewery = random_brewery(1).json()[0]
    brewery_id = _random_brewery["id"]
    brewery_resp = single_brewery(brewery_id)

    assert brewery_resp, \
        (
            f"Request 'single_brewery' with brewery_id - {brewery_id}"
            f" has status != 200",
        )

    assert brewery_resp.status_code == HTTPOk.code, \
        (
            f"Request 'single_brewery' with brewery_id - {brewery_id}"
            f" has status != 200",
        )

    resp_json = brewery_resp.json()

    assert resp_json is not None, \
        f"Request 'single_brewery' with brewery_id - {brewery_id} is None"

    assert resp_json["id"] == brewery_id, \
        (
            f"Request 'single_brewery' with brewery_id - {brewery_id} "
            f"must has key id with value - {brewery_id}",
        )


@pytest.mark.parametrize(
    ("param_key", "param_value"),
    [
        ("by_city", ("Cincinnati", "Minsk")),
        ("by_cities", "Cincinnati"),
        ("by_country", "United States, Russia"),
        ("by_type", "bar, brewpub"),
        ("error_type", ("bar", "brewpub")),
    ],
)
def test_list_breweries_negative(
    session: Any,
    param_key: str,
    param_value: Any,
) -> None:
    resp = list_breweries(**{param_key: param_value})

    resp_json = resp.json()

    for item in resp_json:
        assert item.get(parameter_mapper(param_key)) != param_value, \
            (
                f"Brewery {item} have parameter key - {param_key}"
                f"and value = {param_value}",
            )
