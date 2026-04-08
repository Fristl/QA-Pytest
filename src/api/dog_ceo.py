"""Module with https://dog.ceo/dog-api/ api."""

from __future__ import annotations

from typing import TYPE_CHECKING

from src.api.base import Request
from src.api.base import check_alpha_param
from src.api.base import check_number_param


if TYPE_CHECKING:
    from requests import Response


dog_request = Request("https://dog.ceo/api/")


def list_all_breeds() -> Response:
    return dog_request("breeds/list/all")


def random_image(count: int | str = 1) -> Response:
    check_number_param(count)
    return dog_request(f"breeds/image/random/{count}")


def random_image_by_breed(breed: str, count: int | str = 1) -> Response:
    check_alpha_param(breed)
    check_number_param(count)
    return dog_request(f"breed/{breed}/images/random/{count}")
