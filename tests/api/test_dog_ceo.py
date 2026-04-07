"""Module with tests for https://dog.ceo/dog-api/ api."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING
from typing import Any

import pytest
from requests.exceptions import HTTPError
from webob.exc import HTTPBadRequest
from webob.exc import HTTPOk

from src.api.dog_ceo import dog_request
from src.api.dog_ceo import list_all_breeds
from src.api.dog_ceo import random_image
from src.api.dog_ceo import random_image_by_breed


if TYPE_CHECKING:
    from requests import Response


logger = logging.getLogger(__name__)


@pytest.fixture(scope="module")
def all_breeds() -> Response:
    logger.info("\nGet list all breeds")
    resp = list_all_breeds()
    if resp.ok:
        return resp
    raise HTTPBadRequest


@pytest.fixture(scope="module")
def some_breeds(all_breeds: Response) -> set[str]:
    all_breeds_json = all_breeds.json()
    breeds = {
        "bakharwal",
        "brabancon",
        "malinois",
        "mastiff",
        "segugio",
        "setter",
        "terrier",
    }
    for breed in breeds:
        assert all_breeds_json["message"].get(breed) is not None, \
            f"Breed - {breed} is not in all_breeds."
    return breeds


@pytest.mark.positive
def test_list_all_breeds_positive(session: Any, all_breeds: Response) -> None:
    assert all_breeds.ok, \
        "Request 'list_all_breeds' has status != 200"

    assert all_breeds.status_code == HTTPOk.code, \
        "Request 'list_all_breeds' has status != 200"

    all_breeds_resp_json = all_breeds.json()

    assert all_breeds_resp_json.get("message") is not None, \
        "Request 'list_all_breeds' hasn't attr 'message'"

    assert all_breeds_resp_json.get("status") == "success" , \
        "Request 'list_all_breeds' hasn't status 'success'"

    assert "beagle" in all_breeds_resp_json["message"], \
        "Request 'list_all_breeds' hasn't beagle in message"


@pytest.mark.positive
@pytest.mark.parametrize("count", [0, 1, 5, "0", "4"])
def test_random_image_positive(session: Any, count: int | str) -> None:
    image_resp = random_image(count)
    assert image_resp.ok, \
        "Request 'random_image' has status != 200"

    assert image_resp.status_code == HTTPOk.code, \
        "Request 'random_image' has status != 200"

    image_resp_json = image_resp.json()

    assert image_resp_json.get("message") is not None, \
        "Request 'random_image' hasn't attr 'message'"

    assert image_resp_json.get("status") == "success" , \
        "Request 'random_image' hasn't status 'success'"


@pytest.mark.positive
@pytest.mark.parametrize("count", [0, 1, 3, "0", "4"])
def test_random_image_by_breed_positive(
    session: Any,
    some_breeds: set[str],
    count: int | str,
) -> None:
    for breed in some_breeds:
        image_resp = random_image_by_breed(breed, count)
        assert image_resp.ok, \
            "Request 'random_image_by_breed' has status != 200"

        assert image_resp.status_code == HTTPOk.code, \
            "Request 'random_image_by_breed' has status != 200"

        image_resp_json = image_resp.json()

        assert image_resp_json.get("message") is not None, \
            "Request 'random_image_by_breed' hasn't attr 'message'"

        assert image_resp_json.get("status") == "success" , \
            "Request 'random_image_by_breed' hasn't status 'success'"


def test_list_all_breeds_negative(session: Any) -> None:
    resp = dog_request("breeds/list/all", "POST")
    assert not resp.ok, "Request 'list_all_breeds' has status 200"

    with pytest.raises(HTTPError):
        resp.raise_for_status()

    resp_json = resp.json()
    assert resp_json.get("status") != "success", \
        "Request 'list_all_breeds' has status 'success'"


@pytest.mark.parametrize("count", ["a", {"a": 1}, 3.4, {"d"}])
def test_random_image_count_negative(session: Any, count: int | str) -> None:
    with pytest.raises(HTTPBadRequest):
        random_image(count)


@pytest.mark.parametrize(
    ("breed", "count"),
    [
        ("bakharwal", "a"),
        ("bakharwal", {"a": 1}),
        ("bakharwal", 3.4),
        ("bakharwal", {"d"}),
        ("a", {"a": 1}),
        (3.4, {"d"}),
        ("abcd", {"a": 1}),
        (3.4, 4),
    ],
)
def test_random_image_by_breed_negative(
    session: Any,
    breed: str,
    count: int | str,
) -> None:
    with pytest.raises(HTTPBadRequest):
        random_image_by_breed(breed, count)
