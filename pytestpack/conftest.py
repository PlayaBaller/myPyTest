import pytest


@pytest.yield_fixture()
def setUp():
    print("Conftest method setUp")
    yield
    print("Conftest method tearDown")


@pytest.yield_fixture(scope="module")
def oneTimeSetUp(browser, osType):
    print("Conftest one time method setUp")
    if browser == 'firefox':
        print("Tests are running on FireFox browser")
    elif browser == 'chrome':
        print("Tests are running on Chrome browser")
    else:
        print("Please, define a browser which tests would run")
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
