"""Module with pytest custom addoptions."""
import pytest
import requests


@pytest.fixture
def base_url(pytestconfig):
    return pytestconfig.getoption("--url")


@pytest.fixture
def status_code(pytestconfig):
    return pytestconfig.getoption("--status_code")


def test_set_addoption_url(base_url: str) -> None:
    resp = requests.get(base_url, timeout=10)
    assert resp.ok, f"Request to {base_url} is not OK"


@pytest.mark.parametrize("url", ["https://ya.ru", "https://mail.ru"])
def test_set_addoption_status_code(url: str, status_code: str) -> None:
    resp = requests.get(url, timeout=10)
    assert resp.status_code == int(status_code), \
        f"Request to {url} has status_code = {resp.status_code}"


def test_set_addoptions(base_url: str, status_code: str) -> None:
    resp = requests.get(base_url, timeout=10)
    assert resp.ok, f"Request to {base_url} is not OK"
    assert resp.status_code == int(status_code), \
        f"Request to {base_url} has status_code = {resp.status_code}"
