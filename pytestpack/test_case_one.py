import pytest


@pytest.fixture()
def setUp():
    print("I am a Pytest fixture. I'm setting up before method, in which this one is set up as an argument")


def test_methodA(setUp):
    print("Method A is running")


def test_methodB(setUp):
    print("Method B is running")
