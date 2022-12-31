import pytest


@pytest.fixture(scope="module")
def module_setup():
    """
    default scope=function/method
    :return:
    """
    print("Setup web browser")
    yield
    print("close web browser")