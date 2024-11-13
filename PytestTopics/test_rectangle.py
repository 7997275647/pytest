import pytest

import Source.Shapes as shapes
@pytest.fixture
def  my_rectangle():
    return shapes.rectangle(10,20)
@pytest.fixture
def other_rectangle():
    return shapes.rectangle(5,6)

def test_area(my_rectangle):
    assert my_rectangle.area() == 10*20

def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == 2 * (10 + 20)

def test_not_equal(my_rectangle,other_rectangle):
    assert my_rectangle !=other_rectangle