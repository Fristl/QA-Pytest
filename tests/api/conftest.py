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
