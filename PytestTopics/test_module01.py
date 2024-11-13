
import pytest
from Source.source01 import *
import math

def test_add():
    print("This is my first test")
    assert add(5,10)==15
    assert divide(5,10)==0.5
    assert math.sqrt(4)==2
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)






