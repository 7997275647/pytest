import pytest
import math
from Source import Shapes

class TestCIRCLE:
    def setup_method(self,method):
        print(f"setting up {method}")
        self.Circle = Shapes.circle(10,20)

    def teardown_method(self,method):
        print(f"tearing down {method}")
    def test_area(self):
        assert self.Circle.area() == math.pi * self.Circle.radius ** 2

    def test_perimeter(self):
        assert self.Circle.perimeter() == 2 * math.pi * self.Circle.radius
