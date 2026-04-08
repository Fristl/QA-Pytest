"""Conftest with fixtures for figures."""
from typing import Any

import pytest


@pytest.fixture(scope="module")
def session() -> Any:
    print("\nCreate session")
    yield
    print("\nRollback data")
    print("Close session")


@pytest.fixture(scope="module")
def cache(session) -> Any:
    print("\nInit Cache")
    yield
    print("\nDrop cache")
