import pytest
import source.shapes as shapes

@pytest.mark.parametrize("side, expected_area", [(5, 25), (4, 16), (9, 81)])
def test_mult_square_area(side, expected_area):
    assert shapes.Square(side).area() == expected_area


@pytest.mark.parametrize("side, expected_perimeter", [(5, 20), (4, 16), (9, 36)])
def test_mult_square_perimeter(side, expected_perimeter):
    assert shapes.Square(side).perimeter() == expected_perimeter