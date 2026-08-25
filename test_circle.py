import pytest
import source.shapes as shapes
import math

class TestCircle:
    def setup_method(self, method):
        print(f"Setting up {method}")
        self.circle = shapes.Circle(5)
    
    
    def teardown_method(self, method):
        print(f"Tearing down {method}")
        del self.circle

    def test_area(self):
        assert self.circle.area() == math.pi  * self.circle.radius ** 2

    def test_perimeter(self):
        res = self.circle.perimeter()
        expected = 2 * math.pi * self.circle.radius
        assert res == expected

    def test_not_same_area_rectangle(self, myrec):
        assert self.circle.area() != myrec.area()
