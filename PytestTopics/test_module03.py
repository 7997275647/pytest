import pytest
def testCase1():
    with pytest.raises(ZeroDivisionError):
        assert(1/0)
def testCase2():
    with pytest.raises(AssertionError):
        assert(3>3)
def testCase3():
    with pytest.raises(Exception) as excinfo:
        assert (1,2,3)==(1,2,4)
    print(str(excinfo))
def function():
    raise ValueError("Exception Function Raised")   #function raises ValueError whenever it is called
def testCase4():
    with pytest.raises(Exception) as exceptioninfo:
        function()    #function raises ValueError exception as defined above
    print(str(exceptioninfo))
    assert str(exceptioninfo.value)=="Exception Function Raised"
