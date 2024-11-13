import pytest
import Source.Shapes as shapes

@pytest.fixture
def my_square():
    return shapes.square(10)

def test_area(my_square):
    assert my_square.area() == 100
@pytest.mark.parametrize("side, expected_area", [(5,25),(10,100),(2,4)])
def test_multiple_areas(side, expected_area):
    assert shapes.square(side).area() == expected_area

@pytest.mark.parametrize("side, expected_perimeter",[(2,8),(3,12),(4,16),(5,20)])
def test_multiple_perimeters(side, expected_perimeter):
    assert shapes.square(side).perimeter() == expected_perimeter