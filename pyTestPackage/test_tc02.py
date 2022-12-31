import pytest

"""
@pytest.fixture() provide configuration to run setup() in before test method
Note: you must provide @pytest.fixture() method name as parameter in test method 
"""
@pytest.fixture()
def setup():
    print("setup method")


def test_one(setup):
    print("test_one")


def test_two():
    print("test_two")



