import pytest


@pytest.yield_fixture()
def setUp():
    print("Conftest demo1 method setUp")
    yield
    print("Conftest demo1 method tearDown")


@pytest.yield_fixture(scope="module")
def oneTimeSetUp():
    print("Conftest demo1 one time method setUp")
    yield
    print("Conftest demo1 one time method tearDown")
