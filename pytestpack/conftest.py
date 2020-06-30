import pytest


@pytest.yield_fixture()
def setUp():
    
    print("Conftest method setUp")
    yield
    print("Conftest method tearDown")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):

    print("Conftest one time method setUp")
    if browser == 'firefox':
        value = 10
        print("Tests are running on FireFox browser")
    else:
        value = 20
        print("Tests are running on Chrome browser")
    if request.cls is not None:
        request.cls.value = value
    yield
    print("Conftest one time method tearDown")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of OS")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
