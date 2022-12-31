import pytest


@pytest.fixture()
def setup():
    print("setup method")


def test_one(setup):
    print("test_one")


def test_two(setup):
    print("test_two")



