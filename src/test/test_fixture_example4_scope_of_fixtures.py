import pytest

@pytest.fixture(scope='module', autouse=True)
def setupModule():
    print ("\n Setup Module2")

    yield
    print("\n Teardown Module2")


@pytest.fixture(scope='class', autouse=True)
def setupClass():
    print ("\n Setup Class2")

    yield
    print("\n Teardown Class2")

@pytest.fixture(scope='function', autouse=True)
def setupFunction():
    print ("\n Setup Function2")

    yield
    print("\n Teardown Function2")

class TestClass:
    def test1(self):
        print ('Executing Test 1')
        assert True

    def test2(self):
        print ('Executing Test 2')
        assert True