import pytest

@pytest.fixture()
def setup():
    print ('\n Setup')

# below setup fixture gets called before test1 executes
# This is because we passed setup as parameter to out test1() function
def test1(setup):
    print ('Executing test1')
    assert True

# below setup fixture doesn't gets called before test2 executes
def test2():
    print ('Executing test2')
    assert True

# below setup fixture gets called before test1 executes
# This is because we passed setup via decorator using below syntax.
@pytest.mark.usefixtures("setup")
def test3():
    print ('Executing test3')
    assert True

""" 
Note - It would be cumbersome to pass fixture to each test manually.
Instead, we use autouse functionality so that fixture gets called before each test.
Eg - 
    @pytest.fixture(autouse=True)
    def setup():
        print ('\n Setup')
"""

