from Application.PythonSnippets import *
import pytest
#@pytest.fixture
def test_setup():
    print("Test setup start")
    #yield 'test running'
    print("Test teardown")

@pytest.mark.parametrize('input,expOutput',[(5,[2,4]),(8,[2,4,6,8])])
def test_1(input,expOutput):
    actual_output = GenEvenNums(input)
    assert actual_output==expOutput

@pytest.mark.parametrize('input,expOutput',[(2,True),(3,True),(10,False),(7,True),(17,True)])
def test_2(input,expOutput):
    status = check_prime(input)
    assert status==expOutput

@pytest.mark.xfail
def test_3():
    pytest.skip
    with pytest.raises(customException,match="input should be an integer"):
        check_prime('naveen')
    assert False


