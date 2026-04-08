"""Module with tests for https://jsonplaceholder.typicode.com/ api."""

from __future__ import annotations

import logging
from typing import Any

import pytest
from requests.exceptions import HTTPError
from webob.exc import HTTPBadRequest
from webob.exc import HTTPCreated
from webob.exc import HTTPOk

from src.api.jsonplaceholder import create_resource
from src.api.jsonplaceholder import delete_resource
from src.api.jsonplaceholder import read_resource
from src.api.jsonplaceholder import update_resource


logger = logging.getLogger(__name__)


@pytest.mark.positive
@pytest.mark.parametrize(
    ("kind", "body"),
    [
        ("posts", {"title": "foo", "body": "bar", "userId": 1}),
        ("users", {
            "name": "Leanne Graham",
            "username": "Bret",
            "email": "Sincere@april.biz",
        }),
        ("albums", {"userId": 1, "title": "quidem molestiae enim"}),
    ],
)
def test_create_resource_positive(
    session: Any,
    kind: str,
    body: dict,
) -> None:
    resp = create_resource(kind, body)

    assert resp.ok, \
        "Request 'create_resource' has status is not OK status"

    assert resp.status_code == HTTPCreated.code, \
        "Request 'create_resource' has status != 201"


@pytest.mark.positive
@pytest.mark.parametrize(
    ("kind", "item_id"),
    [
        ("posts", 1),
        ("posts", 10),
        ("users", 3),
        ("users", 10),
        ("albums", 5),
        ("albums", 7),
    ],
)
def test_read_resource_positive(
    session: Any,
    kind: str,
    item_id: int,
) -> None:
    resp = read_resource(kind, item_id)

    assert resp.ok, \
        "Request 'read_resource' has status != 200"

    assert resp.status_code == HTTPOk.code, \
        "Request 'read_resource' has status != 200"

    resp_json = resp.json()

    assert resp_json["id"] == item_id, \
        f"Resource {kind} with id - {resp_json['id']} must has id = {item_id}"


@pytest.mark.positive
@pytest.mark.parametrize(
    ("kind", "item_id", "body"),
    [
        ("posts", 5, {"title": "bar", "body": "bar", "userId": 1}),
        ("users", 2, {"name": "Graham", "username": "Alan"}),
        ("albums", 6, {"userId": 5, "title": "quidem molestiae enim"}),
    ],
)
def test_update_resource_positive(
    session: Any,
    kind: str,
    item_id: int,
    body: dict,
) -> None:
    resp = update_resource(kind, item_id, body)

    assert resp.ok, \
        "Request 'update_resource' has status is not OK status"

    assert resp.status_code == HTTPOk.code, \
        "Request 'update_resource' has status != 200"

    resp_json = resp.json()

    assert resp_json["id"] == item_id, \
        f"Resource {kind} with id - {resp_json['id']} must has id = {item_id}"

    for key, value in body.items():
        assert resp_json[key] == value, \
            (
                f"Resource {kind} with id - {resp_json['id']} "
                f"must has attr {key} = {value}",
            )


@pytest.mark.positive
@pytest.mark.parametrize(
    ("kind", "item_id"),
    [
        ("posts", 1),
        ("posts", 10),
        ("users", 3),
        ("users", 10),
        ("albums", 5),
        ("albums", 7),
    ],
)
def test_delete_resource_positive(
    session: Any,
    kind: str,
    item_id: int,
) -> None:
    resp = delete_resource(kind, item_id)

    assert resp.ok, \
        "Request 'delete_resource' has status != 200"

    assert resp.status_code == HTTPOk.code, \
        "Request 'delete_resource' has status != 200"


@pytest.mark.parametrize(
    ("kind", "item_id"),
    [
        ("posts", 1.1),
        ("posts", "4"),
        ("users", "a"),
        ("users", {"a"}),
        ("albums", []),
        ("albums", {"a": "3"}),
    ],
)
def test_delete_resource_negative(
    session: Any,
    kind: str,
    item_id: int,
) -> None:
    with pytest.raises((HTTPError, HTTPBadRequest)):
        delete_resource(kind, item_id).raise_for_status()
