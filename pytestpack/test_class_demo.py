import pytest
from pytestpack.class_to_test import ClassForTest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestClassDemo:

    @pytest.fixture(autouse=True)
    def classsetup(self, oneTimeSetUp):
        self.abc = ClassForTest(self.value)

    def test_methodA(self, classsetup):
        result = self.abc.sumnumbers(2, 8)
        assert result == 20
        print("Test method A is running")
        
    def test_methodB(self, classsetup):
        print("Test method B is running")
