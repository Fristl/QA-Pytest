"""Conftest with fixtures for figures."""
import logging
from typing import Any

import pytest


logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")


@pytest.fixture(scope="module")
def session() -> Any:
    logger.error("\nCreate session")
    yield
    logger.error("Close session")


def pytest_addoption(parser) -> None:
    parser.addoption(
        "--url",
        default="https://ya.ru",
        help="Set url for request",
    )
    parser.addoption(
        "--status_code",
        default="200",
        help="Expect this status code for request",
    )
