import pytest

@pytest.fixture()
def setup1():
    print ('\n Setup 1')
    yield
    print ('\n Teardown 1')


@pytest.fixture()
def setup2(request):
    print ('\n Setup 2')

    def teardown_2_a():
        print ('\n Teardown 2A called')

    def teardown_2_b():
        print ('\n Teardown 2B called')

    request.addfinalizer(teardown_2_a)
    request.addfinalizer(teardown_2_b)

@pytest.mark.usefixtures("setup1")
def test1():
    print ('Executing test1')
    assert True

@pytest.mark.usefixtures("setup2")
def test2():
    print ('Executing test2')
    assert True

