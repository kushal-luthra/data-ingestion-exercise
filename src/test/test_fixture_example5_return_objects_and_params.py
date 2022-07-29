import pytest

@pytest.fixture(params=[1,2,3])
def setup(request):
    return_val = request.param
    print ('\n Setup return_val = {}'.format(return_val))

    return return_val

# Note: we didn't use  @pytest.mark.usefixtures("setup") here as we needed to access value of setup fixture.
def test1(setup):
    print ('Executing test1')
    print ('Setup return value inside test function = ',format(setup))
    assert True

