import pytest


@pytest.fixture()
def setup():
    """
    @pytest.fixture() provide configuration to run setup() in before test method
    Note: you must provide @pytest.fixture() method name as parameter in test method
    """
    print("Setup web browser")
    yield
    print("close web browser")


def test_one(setup):
    print("test_one")


def test_two():
    print("test_two")

