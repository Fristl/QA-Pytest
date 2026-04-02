"""Conftest with fixtures for figures."""
import pytest


@pytest.fixture(scope="module")
def session():
    print("\nCreate session")
    yield
    print("\nRollback data")
    print("Close session")


@pytest.fixture(scope="module")
def cache(session):
    print("\nInit Cache")
    yield
    print("\nDrop cache")
