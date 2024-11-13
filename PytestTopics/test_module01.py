import pytest
import time
from Source.source01 import *
import math

def test_add():
    print("This is my first test")
    assert add(5,10) == 15

def test_divide():
    print("This is my second test")
    assert divide(5,10) == 0.5
@pytest.mark.xfail(reason="This teat going to fail")
def test_divide_zero():
    assert divide(10,0) ==1
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
@pytest.mark.slow
def test_slow():
    assert add(5,10) == 15
@pytest.mark.skip(reason= "This feature is not yet implemented")
def test_mul():
    assert mul(5,10) == 150
