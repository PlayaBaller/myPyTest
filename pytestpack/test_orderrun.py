import pytest


@pytest.mark.run(order=2)
def test_run_order_methodA(oneTimeSetUp, setUp):
    print("Method A is running")


@pytest.mark.run(order=1)
def test_run_order_methodB(oneTimeSetUp, setUp):
    print("Method B is running")


@pytest.mark.run(order=4)
def test_run_order_methodC(oneTimeSetUp, setUp):
    print("Method C is running")


@pytest.mark.run(order=3)
def test_run_order_methodD(oneTimeSetUp, setUp):
    print("Method D is running")


@pytest.mark.run(before='test_run_order_methodF')
def test_run_order_methodE(oneTimeSetUp, setUp):
    print("Method E is running")


@pytest.mark.run(after='test_run_order_methodE')
def test_run_order_methodF(oneTimeSetUp, setUp):
    print("Method F is running")

