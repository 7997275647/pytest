import pytest

def test_area(my_rectangle):
    assert my_rectangle.area() == 10*20

def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == 2 * (10 + 20)

def test_not_equal(my_rectangle,other_rectangle):
    assert my_rectangle !=other_rectangle