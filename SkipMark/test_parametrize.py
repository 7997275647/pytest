import pytest
import math
@pytest.mark.parametrize("input_value",[89,34,76,65])
def test_parameter01(input_value):
    assert input_value > 30
@pytest.mark.parametrize("input,output",[(2,8),(3,27),(4,64)])
def test_parameter02(input,output):
    assert input**3 == output
data = [
    ([1,2,3],"sum",6),([1,2,3],"prod",6)
]
@pytest.mark.parametrize("a,b,c",data)
def test_parameter03(a,b,c):
    if b== "sum":
        assert sum(a) ==6
    elif b=="prod":
        assert math.prod(a)==6


