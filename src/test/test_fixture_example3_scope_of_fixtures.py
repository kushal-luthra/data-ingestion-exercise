import pytest

@pytest.fixture(scope='session', autouse=True)
def setupSession():
    print ("\n Setup Session")

    yield
    print("\n Teardown Session")


@pytest.fixture(scope='module', autouse=True)
def setupModule():
    print ("\n Setup Module")

    yield
    print("\n Teardown Module")


@pytest.fixture(scope='function', autouse=True)
def setupFunction():
    print ("\n Setup Function")

    yield
    print("\n Teardown Function")

def test1():
    print ('Executing Test 1')
    assert True

def test2():
    print ('Executing Test 2')
    assert True